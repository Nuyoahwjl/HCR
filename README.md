<!--
<div style="
    color:rgb(238, 22, 44);
    background-color: #f8d7da;
    padding: 12px;
    border: 2px solid #f5c6cb;
    border-radius: 10px;
    margin: 10px 0;
    font-weight: bold;
    display: inline-block;
    ">⚠️该版本已弃用⚠️</div>
-->

> [!important]
> 该版本已弃用

### ![🐬Powered by DeepSeek🐬](https://img.shields.io/badge/Powered_by-DeepSeek-0A0A0A?style=for-the-badge&logo=deepseek)

# 🩺Health Check Recommendation🩺
This project is a health check recommendation system built using LangChain, and DeepSeek LLM. It uses RAG technology to recommend health check packages based on user information.

### 🗂️Folder Structure🗂️

```
HCR/
├── config/
│   └── settings.py
├── data/
│   ├──health_check_data.csv
│   └──symptoms.pdf
├── vectordb/
│   ├── vectorstore.py
│   └── vector_db_1/
│   └── vector_db_2/
├── agent/
│   ├── chain.py
│   └── prompts.py
│   └── utils.py
├── test/
├── web/
│   ├── pages/
│   │   └── 1_🥰_Recommend.py
│   │   └── 2_🤖_Chatbot.py
│   │   └── 3_🏥_Hospitals.py
│   └── 🩺HCR-HOME.py
├── requirements.txt
└── README.md
```
### 🚀How to Run🚀

1. Install dependencies:
```bash
pip install -r requirements.txt
```
2. Build Vector Store:
```bash
python vectordb/vectorstore.py
```
3. Run the Streamlit app:
```bash
streamlit run web/🩺HCR-HOME.py
```

<!--
2. Install faiss-cpu
```bash
conda install pytorch::faiss-cpu=1.10.0
```
-->

### 💻Tech Stack💻

| Component          | Technology Selection     |
|--------------------|--------------------------|
| Large Model        | DeepSeek API             |
| Framework          | LangChain                |
| Vector Database    | FAISS                    |
| Frontend           | Streamlit                |
| Text Embedding     | BAAI/bge-base-zh         |



<!--
1. Configure your DeepSeek API key:
```py
# HCR\config\..:
echo "DEEPSEEK_API_KEY=your_api_key" > .env
```
-->
