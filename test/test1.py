from langchain_community.document_loaders import CSVLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_deepseek import ChatDeepSeek
from langchain.schema.output_parser import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
# from config.settings import Config


RECOMMEND_PROMPT = ChatPromptTemplate.from_template(
    """
    你是一位专业体检规划师，根据其他患者体检情况、医学知识和用户信息推荐体检项目。
    
    <其他患者体检情况>
    {context1}
    </其他患者体检情况>

    <医学知识>
    {context2}
    </医学知识>

    <用户信息>
    - 性别：{gender}
    - 年龄：{age}
    - 身高：{height}cm
    - 体重：{weight}kg
    - 病史：{medical_history}
    - 症状：{symptoms}
    </用户信息>

    请按以下格式输出且不要输出总结语
    1. 推荐项目：按优先级列出5-8个项目
    2. 推荐理由：结合用户情况说明
    3. 注意事项：检查前准备事项
    """
    )


# # 处理CSV数据
# csv_loader = CSVLoader("D:/Desktop/AGENT/HCR/data/raw/health_check_data.csv",encoding="utf-8")
# csv_docs = csv_loader.load()

# # 处理PDF数据
# pdf_loader = PyPDFLoader("D:/Desktop/AGENT/HCR/data/raw/symptoms.pdf")
# pdf_pages = pdf_loader.load_and_split()

# # # 合并文档
# # all_docs = csv_docs + pdf_pages
# # print(all_docs)

# # 文档分割
# text_splitter = RecursiveCharacterTextSplitter(
#     chunk_size=200,
#     chunk_overlap=40
# )
# splits1 = text_splitter.split_documents(csv_docs)
# splits2 = text_splitter.split_documents(pdf_pages)

# # print(splits1)
# # print(splits2)





# 嵌入模型
embeddings = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
    # model_name = "hfl/chinese-bert-wwm-ext",
    # model_name = "BAAI/bge-base-zh-v1.5",
    model_kwargs = {'device': 'cuda'},
    # model_kwargs = {'device': 'cpu'},
    encode_kwargs = {'normalize_embeddings': True}
)

# 创建向量存储库
# vectorstore1 = Chroma.from_documents(
#     documents=splits1,
#     embedding=embeddings,
#     persist_directory="D:/Desktop/AGENT/HCR/vectordb/vector_db_1"
# )
# vectorstore2 = Chroma.from_documents(
#     documents=splits2,
#     embedding=embeddings,
#     persist_directory="D:/Desktop/AGENT/HCR/vectordb/vector_db_2"
# )

# vectorstore1 = FAISS.from_documents(
#     documents=splits1,
#     embedding=embeddings,
# )
# vectorstore1.save_local("D:/Desktop/AGENT/HCR/vectordb/vector_db_1")
# vectorstore2 = FAISS.from_documents(
#     documents=splits2,
#     embedding=embeddings,
# )
# vectorstore2.save_local("D:/Desktop/AGENT/HCR/vectordb/vector_db_2")





# 加载向量存储库
v1 = FAISS.load_local(
    folder_path="D:/Desktop/AGENT/HCR/vectordb/vector_db_1",
    embeddings=embeddings,
    allow_dangerous_deserialization=True
)
v2 = FAISS.load_local(
    folder_path="D:/Desktop/AGENT/HCR/vectordb/vector_db_2",
    embeddings=embeddings,
    allow_dangerous_deserialization=True
)

# docs1=v1.similarity_search("高血压",k=2)
# # print(docs1)
# docs2=v2.similarity_search("糖尿病",k=2)
# # print(docs2)

# def format_docs(docs, title="搜索结果"):
#     output = [f"\n{'='*30} {title} {'='*30}"]
#     for i, doc in enumerate(docs, 1):
#         output.append(f"\n文档 {i}:")
#         output.append(f"内容：{doc.page_content}")
#         if 'source' in doc.metadata:
#             output.append(f"来源：{doc.metadata['source']}")
#         if 'page' in doc.metadata:
#             output.append(f"页码：{doc.metadata['page']}")
#     return "\n".join(output)

# print(format_docs(docs1, "高血压相关结果"))
# print(format_docs(docs2, "糖尿病相关结果"))

# from langchain_core.prompts import ChatPromptTemplate
# ret1 = v1.as_retriever(search_kwargs={"k": 3})
# ret2 = v2.as_retriever(search_kwargs={"k": 3})
# text = "{context}"
# prompt = ChatPromptTemplate.from_template(text)
# output1 =ret1|prompt
# output2 =ret2|prompt
# print(output1.invoke({"context": "高血压"}))
# print(output2.invoke({"context": "糖尿病"}))  



llm = ChatDeepSeek(
        model="deepseek-chat",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        api_key="",
        # other params...
    )

def build_chain():
    return (RECOMMEND_PROMPT | llm | StrOutputParser())

def user_info_to_str(user_info):
    # 处理基本信息部分
    parts = []
    # 构建性别和年龄描述
    demographic = []
    gender = user_info.get("gender")
    age = user_info.get("age")
    if gender:
        demographic.append(f"{gender}性")
    if age:
        demographic.append(f"{age}岁")
    parts.append("一位" + "".join(demographic) if demographic else "一位用户")
    # 构建身体数据部分
    body_data = []
    height = user_info.get("height")
    weight = user_info.get("weight")
    if height:
        body_data.append(f"身高{height}厘米")
    if weight:
        body_data.append(f"体重{weight}公斤")
    if body_data:
        parts.append("，".join(body_data))
    # 处理病史
    medical_history = user_info.get("medical_history")
    if medical_history:
        parts.append(f"既往病史：{medical_history}")
    else:
        parts.append("无既往病史")
    # 处理当前症状
    symptoms = user_info.get("symptoms")
    if symptoms:
        parts.append(f"当前症状：{symptoms}")
    else:
        parts.append("未报告明显症状")
    # 组合所有部分并添加句号
    return "，".join(parts) + "。"

def format_docs(docs):
    formatted = []
    for i, doc in enumerate(docs):
        # 提取文档内容和元数据
        content = doc.page_content
        # 格式化字符串
        doc_str = f"""[{i+1}]\n{content}"""
        formatted.append(doc_str)
    return "\n".join(formatted)


def run_chain(user_info):
    user_info_str = user_info_to_str(user_info)
    docs1=v1.similarity_search(user_info_str,k=3)
    docs2=v2.similarity_search(user_info_str,k=5)
    docs1_str = format_docs(docs1)
    docs2_str = format_docs(docs2)
    print("=======================")    
    print(docs1_str)
    print("=======================")
    print(docs2_str)
    print("=======================")
    result = build_chain().invoke({
        "context1": docs1_str,
        "context2": docs2_str,
        "gender": str(user_info["gender"]),
        "age": str(user_info["age"]),
        "height": str(user_info["height"]),
        "weight": str(user_info["weight"]),
        "medical_history": str(user_info["medical_history"]),
        "symptoms": str(user_info["symptoms"]),
    })
    return result


user={
    "gender": "男",
    "age": "30",
    "height": "180",
    "weight": "70",
    "medical_history": "高血压",
    "symptoms": "头痛、胸闷"
}

print(run_chain(user))
