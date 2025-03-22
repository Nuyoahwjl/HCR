import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.insert(0, project_root)

from langchain_community.document_loaders import CSVLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from config.settings import Config

# 处理CSV数据
csv_loader = CSVLoader(project_root+Config.DATA["csv"],encoding="utf-8")
csv_docs = csv_loader.load()

# 处理PDF数据
pdf_loader = PyPDFLoader(project_root+Config.DATA["pdf"])
pdf_pages = pdf_loader.load_and_split()


# 文档分割 
text_splitter1 = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=40
)
text_splitter2 = RecursiveCharacterTextSplitter(
    chunk_size=50,  
    chunk_overlap=0,  
    separators=["\n"], 
)
splits1 = text_splitter1.split_documents(csv_docs)
splits2 = text_splitter2.split_documents(pdf_pages)

# print(splits1)
# print(splits2)




# 嵌入模型
embeddings = HuggingFaceEmbeddings(
    # model_name = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
    # model_name = "hfl/chinese-bert-wwm-ext",
    model_name = "BAAI/bge-base-zh-v1.5",
    model_kwargs = {'device': 'cuda'},
    # model_kwargs = {'device': 'cpu'},
    encode_kwargs = {'normalize_embeddings': True}
)

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


vectorstore1 = FAISS.load_local(
    folder_path=project_root+Config.VECTORSTORE1_PATH,
    embeddings=embeddings,
    allow_dangerous_deserialization=True
)
vectorstore2 = FAISS.load_local(
    folder_path=project_root+Config.VECTORSTORE2_PATH,
    embeddings=embeddings,
    allow_dangerous_deserialization=True
)

docs1=vectorstore1.similarity_search("高血压，糖尿病",k=3)
# print(docs1)
docs2=vectorstore2.similarity_search("哮喘，痛风，肝炎",k=5)
# print(docs2)

def format_docs(docs, title="搜索结果"):
    output = [f"\n{'='*30} {title} {'='*30}"]
    for i, doc in enumerate(docs, 1):
        output.append(f"\nDocument {i}:")
        output.append(f"{doc.page_content}")
        if 'source' in doc.metadata:
            output.append(f"来源：{doc.metadata['source']}")
        # if 'page' in doc.metadata:
        #     output.append(f"页码：{doc.metadata['page']}")
    return "\n".join(output)

print(format_docs(docs1, "高血压，糖尿病相关结果"))
print(format_docs(docs2, "哮喘，痛风，肝炎相关结果"))