import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.insert(0, project_root)

# print(f"Current Dir: {current_dir}")
# print(f"Project Root: {project_root}")
# print(f"Agent exists: {os.path.exists(os.path.join(project_root, 'agent'))}")

# from langchain.chains import RetrievalQA
from langchain.schema.output_parser import StrOutputParser
from langchain_community.vectorstores import Chroma
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from config.settings import Config
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from agent.prompts import RECOMMEND_PROMPT
from langchain_deepseek import ChatDeepSeek
import agent.utils as utils

class RecommendationChain:
    def __init__(self):
        self.llm = ChatDeepSeek(
            model="deepseek-chat",
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
            api_key=Config.DEEPSEEK_API_KEY,
            # other params...
        )

        embeddings=HuggingFaceEmbeddings(
            # model_name = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
            # model_name = "hfl/chinese-bert-wwm-ext",
            model_name = "BAAI/bge-base-zh-v1.5",
            model_kwargs = {'device': 'cuda'},
            # model_kwargs = {'device': 'cpu'},
            encode_kwargs = {'normalize_embeddings': True}
        )
        # self.vectorstore1 = Chroma(
        #     persist_directory=Config.VECTORSTORE1_PATH,
        #     embedding_function=embeddings
        # )
        # self.vectorstore2 = Chroma(
        #     persist_directory=Config.VECTORSTORE2_PATH,
        #     embedding_function=embeddings
        # )
        self.vectorstore1 = FAISS.load_local(
            folder_path=project_root+Config.VECTORSTORE1_PATH,
            embeddings=embeddings,
            allow_dangerous_deserialization=True
        )
        self.vectorstore2 = FAISS.load_local(
            folder_path=project_root+Config.VECTORSTORE2_PATH,
            embeddings=embeddings,
            allow_dangerous_deserialization=True
        )

        
    def build_chain(self):
        # retriever1 = self.vectorstore1.as_retriever(search_kwargs={"k": 3})
        # retriever2 = self.vectorstore2.as_retriever(search_kwargs={"k": 3})

        # retriever = self.vectorstore1.as_retriever(
        #     search_type="mmr",  # 使用最大边际相关性算法
        #     search_kwargs={
        #     "k": 5,          # 召回数量
        #     "score_threshold": 0.7  # 相似度阈值
        #    }
        # )

        # return (
        #     {
        #         "context1": retriever1 | self._format_docs,
        #         "context2": retriever2 | self._format_docs,
        #         "gender": RunnablePassthrough(),
        #         "age": RunnablePassthrough(),
        #         "height": RunnablePassthrough(),
        #         "weight": RunnablePassthrough(),
        #         "medical_history": RunnablePassthrough(),
        #         "symptoms": RunnablePassthrough(),
        #     }
        #     | RECOMMEND_PROMPT
        #     | self.llm
        #     | StrOutputParser()
        # )

        return (RECOMMEND_PROMPT | self.llm | StrOutputParser())
    
    # def _format_docs(self, docs):
    #     return "\n\n".join(d.page_content for d in docs)
    
    def run_chain(self, user_info):
        user_info_str = utils.user_info_to_str(user_info)
        docs1=self.vectorstore1.similarity_search(user_info_str,k=2)
        docs2=self.vectorstore2.similarity_search(user_info_str,k=2)
        docs1_str = utils.format_docs(docs1)
        docs2_str = utils.format_docs(docs2)
        result = self.build_chain().invoke({
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