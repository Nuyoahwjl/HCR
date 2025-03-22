# Description: This file contains the configuration settings for the application.
import os
from dotenv import load_dotenv

load_dotenv('.env')

class Config:
    # DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
    DEEPSEEK_API_KEY = "sk-ffc5fcb4ba8e4f96a646753274c0c0c4"
    VECTORSTORE1_PATH = "/vectordb/vector_db_1"
    VECTORSTORE2_PATH = "/vectordb/vector_db_2"
    DATA = {
        "csv": "/data/health_check_data.csv",
        "pdf": "/data/symptoms.pdf"
    }