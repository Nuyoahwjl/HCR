import streamlit as st

st.set_page_config(page_title="HCR", page_icon="🩺")

st.markdown(
"""
<div style="display: flex; justify-content: center;">
<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/Tarikul-Islam-Anik/Animated-Fluent-Emojis@master/Emojis/Smilies/Face%20with%20Tongue.png" width="10%" />
  <img src="https://cdn.jsdelivr.net/gh/Tarikul-Islam-Anik/Animated-Fluent-Emojis@master/Emojis/Smilies/Face%20with%20Spiral%20Eyes.png" width="10%" />
  <img src="https://cdn.jsdelivr.net/gh/Tarikul-Islam-Anik/Animated-Fluent-Emojis@master/Emojis/Smilies/Relieved%20Face.png" width="10%" />
  <img src="https://cdn.jsdelivr.net/gh/Tarikul-Islam-Anik/Animated-Fluent-Emojis@master/Emojis/Smilies/Astonished%20Face.png" width="10%" />
  <img src="https://cdn.jsdelivr.net/gh/Tarikul-Islam-Anik/Animated-Fluent-Emojis@master/Emojis/Smilies/Beaming%20Face%20with%20Smiling%20Eyes.png" width="10%" />
</p>	
</div>
""", unsafe_allow_html=True)

st.markdown("-------------")

# ![Project Architecture](https://placehold.co/800x200/009688/FFFFFF/png?text=AI+Health+Check+Assistant&font=Lora)

st.markdown(
"""
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
│   │   └── 1_🥰_Recommend.py
│   │   └── 2_🤖_Chatbot.py
│   │   └── 3_🏥_Hospitals.py
│   └── HCR-HOME.py            # Main app
└── requirements.txt           # Dependencies
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

## 🛠️ Tech Stack  

"""
)

st.markdown("""
<div>
<style>
.tech-table {
    width: 100% !important;
    table-layout: fixed;
    border-collapse: collapse;
    margin: auto;
    font-family: Arial, sans-serif;
    background: transparent !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}
.tech-table th,
.tech-table td {
    width: 50% !important;
    padding: 12px;
    text-align: left;
    border-bottom: 2px solid rgba(222, 226, 230, 0.5); /* 半透明边框 */
    word-break: break-word;
    box-sizing: border-box;
    background: transparent !important;
}
.tech-table th {
    border-bottom: 3px solid rgba(73, 80, 87, 0.8); /* 深色半透明边框 */
    font-weight: 600;
}
@media screen and (max-width: 600px) {
    .tech-table {
        font-size: 14px;
        box-shadow: none; /* 小屏幕移除阴影 */
    }
    .tech-table td, 
    .tech-table th {
        padding: 8px;
    }
}
</style>
<table class="tech-table">
    <colgroup>
        <col style="width: 50%;">
        <col style="width: 50%;">
    </colgroup>
    <tr>
        <th>Component</th>
        <th>Technology</th>
    </tr>
    <tr>
        <td><strong>Large Language Model</strong></td>
        <td>DeepSeek API</td>
    </tr>
    <tr>
        <td><strong>Framework</strong></td>
        <td>LangChain</td>
    </tr>
    <tr>
        <td><strong>Vector Database</strong></td>
        <td>FAISS</td>
    </tr>
    <tr>
        <td><strong>Frontend</strong></td>
        <td>Streamlit</td>
    </tr>
    <tr>
        <td><strong>Embeddings</strong></td>
        <td>BAAI/bge-base-zh</td>
    </tr>
    <tr>
        <td><strong>Environment</strong></td>
        <td>Python 3.12.9</td>
    </tr>
</table>
</div>
""", unsafe_allow_html=True)

st.markdown("-------------")

# [![Open in GitHub](https://img.shields.io/badge/GitHub-Repo-blue?logo=github)](https://github.com/Nuyoahwjl/HCR)  

st.warning("Let's build smarter healthcare together! 🌟 ")

st.markdown("""
<div style="text-align: center;">
    <img src="https://placehold.co/800x200/009688/FFFFFF/png?text=AI+Health+Check+Assistant&font=Lora" 
         style="display: block; margin: auto; width: 100%;">
</div>
""", unsafe_allow_html=True)







# st.markdown("""
# 🛠️ Tech Stack  
# | Component                | Technology           |  
# |--------------------------|----------------------|  
# | **Large Language Model** | DeepSeek API         |  
# | **Framework**            | LangChain            |  
# | **Vector Database**      | FAISS                |  
# | **Frontend**             | Streamlit            |  
# | **Embeddings**           | BAAI/bge-base-zh     |  
# | **Environment**          | Python 3.12.9        |            
# ---          
# """)







with st.sidebar:
    st.success("Select one page above")
    # st.markdown("Created by [Chia.le](https://github.com/Nuyoahwjl)")
    # st.markdown("Contact me [📮](chia.le@foxmail.com)")
    # st.markdown(
    # """
    #   <picture>
    #     <img src="https://raw.githubusercontent.com/Nuyoahwjl/Nuyoahwjl/output/github-contribution-grid-snake.svg"/>
    #   </picture>
    # """, unsafe_allow_html=True
    # )
    
