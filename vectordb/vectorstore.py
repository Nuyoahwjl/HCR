import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.insert(0, project_root)

from langchain_community.document_loaders import CSVLoader, PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config.settings import Config
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def process_data():
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
    
    # 嵌入模型
    embeddings = HuggingFaceEmbeddings(
        # model_name = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
        # model_name = "hfl/chinese-bert-wwm-ext",
        model_name = "BAAI/bge-base-zh-v1.5",
        # model_kwargs = {'device': 'cuda'},
        model_kwargs = {'device': 'cpu'},
        encode_kwargs = {'normalize_embeddings': True}
    )

    # 创建向量存储库
    # vectorstore1 = Chroma.from_documents(
    #     documents=splits1,
    #     embedding=embeddings,
    #     persist_directory=Config.VECTORSTORE1_PATH
    # )
    # vectorstore2 = Chroma.from_documents(
    #     documents=splits2,
    #     embedding=embeddings,
    #     persist_directory=Config.VECTORSTORE2_PATH
    # )
    vectorstore1 = FAISS.from_documents(
        documents=splits1,
        embedding=embeddings,
    )
    vectorstore1.save_local(folder_path=project_root+Config.VECTORSTORE1_PATH)
    vectorstore2 = FAISS.from_documents(
        documents=splits2,
        embedding=embeddings,
    )
    vectorstore2.save_local(folder_path=project_root+Config.VECTORSTORE2_PATH)

    return vectorstore1, vectorstore2

if __name__ == "__main__":
    process_data()