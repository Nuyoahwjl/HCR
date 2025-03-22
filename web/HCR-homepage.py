import streamlit as st

st.set_page_config(page_title="HCR", page_icon="🩺")


# st.markdown(
# """<h1 style="text-align:center">Welcome to HCR</h1>""", unsafe_allow_html=True)
st.markdown(
"""
<div style="display: flex; justify-content: center;">
<p align="center">
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Face%20with%20Tongue.png" width="10%" />
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Face%20with%20Spiral%20Eyes.png" width="10%" />
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Relieved%20Face.png" width="10%" />
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Astonished%20Face.png" width="10%" />
  <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Beaming%20Face%20with%20Smiling%20Eyes.png" width="10%" />
</p>	
</div>
""", unsafe_allow_html=True)

st.markdown("-------------")

st.markdown(
"""
# 🩺 Health Check Recommendation System  

![Project Architecture](https://placehold.co/800x200/009688/FFFFFF/png?text=AI+Health+Check+Assistant)  
*A smart health checkup advisor powered by RAG and LLMs*

## 📖 Project Overview  
This project is an intelligent **Health Check Recommendation System** that suggests personalized medical examination packages using:  
- 🧠 **RAG (Retrieval-Augmented Generation) technology**  
- ⚡ **DeepSeek-LLM** for natural language processing  
- 🔍 **FAISS** vector database for efficient similarity search  
- 🎯 **LangChain** framework for pipeline orchestration  

Designed to bridge medical knowledge with individual needs through AI-powered analysis.  

---

## 🗂 Project Structure  
```bash
HCR/
├── config/                    
│   └── settings.py            # Project settings
│   └── .env                   # API keys
├── data/                     
│   ├── health_check_data.csv  # Checkup packages
│   └── symptoms.pdf           # Symptom database
├── vectordb/                  
│   ├── vectorstore.py         # DB builder
│   ├── vector_db_1            # FAISS store
│   └── vector_db_2            # FAISS store
├── agent/                     
│   ├── chain.py               # LangChain workflows 
│   └── prompts.py             # LLM prompt templates
├── web/                       
│   ├── pages/                 # Streamlit pages
│   │   └── 1_🥰_Recommendation.py  
│   │   └── 2_🏥_Hospitals.py
│   └── HCR-homepage.py        # Main app
└── requirements.txt           # Dependencies
```

---

## 🛠️ Tech Stack  

| Component                | Technology                          |  
|--------------------------|-------------------------------------|  
| **Large Language Model** | DeepSeek API (Medical QA optimized) |  
| **Framework**            | LangChain                           |  
| **Vector Database**      | FAISS                               |  
| **Frontend**             | Streamlit                           |  
| **Embeddings**           | BAAI/bge-base-zh                    |  
| **Environment**          | Python 3.12.9                       |  

---

## 🚀 Quick Start  

### 1. Installation  
```bash 
pip install -r requirements.txt
```

### 2. Configuration  
```python
# Set API key in .env file
echo "DEEPSEEK_API_KEY=your_api_key" > config/.env
```

### 3. Build Vector Database  
```bash
python vectordb/vectorstore.py  # Creates FAISS indexes from medical data
```

### 4. Launch Application  
```bash
streamlit run web/HCR-homepage.py  # Starts the Streamlit interface
```

---

## ✨ Key Features  
- **Personalized Recommendations**  
  🔍 Analyzes user profile + medical history → suggests tailored checkup packages  

- **Multi-Source Knowledge**  
  📚 Combines structured data (CSV) + unstructured documents (PDF)  

- **Modular Architecture**  
  📢 Separates data processing, AI logic, and UI layers  

- **Medical Accuracy**  
  ✅ Powered by DeepSeek's medically-tuned LLM  

- **User-Friendly Interface**  
  💻 Streamlit web app with guided conversation flow  

---

*Let's build smarter healthcare together!* 🌟  

[![Open in GitHub](https://img.shields.io/badge/GitHub-Repo-blue?logo=github)](https://github.com/Nuyoahwjl/HCR)  
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url.streamlit.app/)
"""
)












with st.sidebar:
    st.success("Select one page above.")
    # st.markdown("Created by [Chia.le](https://github.com/Nuyoahwjl)")
    # st.markdown("Contact me [📮](chia.le@foxmail.com)")
    # st.markdown(
    # """
    #   <picture>
    #     <img src="https://raw.githubusercontent.com/Nuyoahwjl/Nuyoahwjl/output/github-contribution-grid-snake.svg"/>
    #   </picture>
    # """, unsafe_allow_html=True
    # )
    
