import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, project_root)

import streamlit as st
import pandas as pd
from agent.chain import RecommendationChain
import time


def format_user_info(gender, age, height, weight, medical_history, symptoms):
    """格式化用户信息"""
    return {
        "gender": gender,
        "age": age,
        "height": height,
        "weight": weight,
        "medical_history": medical_history,
        "symptoms": symptoms
    }


# 界面布局
st.set_page_config(
    page_title="Recommend",
    page_icon="🥰",
)


re = RecommendationChain()


# st.title("🩺Health Check Recommendation")
# st.markdown("![](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=450&pause=1000&color=000000&center=true&vCenter=true&width=800&lines=Hi+there+👋,+Welcome+to+HCR!;Fill+in+the+following+information+to+get+the+recommendation.)")


st.markdown("""
<div style="text-align: center;">
    <h1>🩺Health Check Recommendation</h1>
</div>
""", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center;">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=450&pause=1000&color=FF4B4BFF&center=true&vCenter=true&width=800&lines=Hi+there+👋,+Welcome+to+HCR!;Fill+in+the+following+information+to+get+the+recommendation." 
         style="display: block; margin: auto; width: 100%; max-width: 800px;">
</div>
""", unsafe_allow_html=True)


col1, col2 = st.columns(2)
with col1:
    gender = st.selectbox(label="Gender", 
                          options=["male", "female", "secret"],
                          format_func = str,
                          help = "if you don't want to tell us, keep secret")
    height = st.slider("Height(cm)", 50, 200, 50)
with col2:
    age = st.number_input("Age", 
                          min_value=0, 
                          max_value=100)
    weight = st.slider("Weight(kg)", 0, 100, 0)
medical_history = st.text_area("Medical History", key="medical", height=100)
symptoms = st.text_area("Symptoms", key="symptoms", height=100)
submitted = st.button("Recommend", icon='✔️', use_container_width=True)


with st.sidebar.expander(label="TEST",expanded=False):
    DeepSeek_API = st.text_input("DeepSeek API Key", type="password")
    if not DeepSeek_API.startswith("sk-"):
        st.warning("Please enter API!", icon="⚠️")


if submitted:
    if height == 50 or age ==0 or weight ==0 or not medical_history.strip() or not symptoms.strip():
        st.error("Please fill in all the information", icon="🚨")
        # st.toast("Please fill in all the information", icon="🚨")
    else:
        user_info = format_user_info(gender, age, height, weight, medical_history, symptoms)
        with st.spinner("analyzing...",show_time=True):
            start = time.time()
            result = re.run_chain(user_info)
            # result = "## 你好"
            with st.sidebar.expander(label="TEST",expanded=True):
                st.success(f"successfully(time:{time.time()-start:.1f}s)")
                st.write(user_info)
            with st.expander("RECOMMENDATIONS", expanded=True):
                st.markdown("## RECOMMENDATIONS")
                st.write(result)
                st.download_button(label="Download", data=result, file_name="Recommendations.md", use_container_width=True, icon="📥")
    







# DeepSeek_API = st.sidebar.text_input("DeepSeek API Key", type="password")
# if not DeepSeek_API.startswith("sk-"):
#     st.warning("Please enter your DeepSeek API key!", icon="⚠️")
# else:
#     re = RecommendationChain(api_key=DeepSeek_API)
#     # re.init_llm(api_key=DeepSeek_API)
#     if submitted:
#         if height == 50 or age ==0 or weight ==0 or not medical_history.strip() or not symptoms.strip():
#             st.error("Please fill in all the information", icon="🚨")
#             # st.toast("Please fill in all the information", icon="🚨")
#         else:
#             user_info = format_user_info(gender, age, height, weight, medical_history, symptoms)
#             with st.spinner("analyzing..."):
#                 start = time.time()
#                 result = re.run_chain(user_info)
#                 # result = "## 你好"
#                 with st.sidebar.expander(label=" ",expanded=True):
#                     st.success(f"successfully(time:{time.time()-start:.1f}s)")
#                     st.write(user_info)
#                 with st.expander("Recommendations", expanded=True):
#                     st.markdown("## RECOMMENDATIONS")
#                     st.write(result)
#                     st.download_button(label="download", data=result, file_name="Recommendations.md")