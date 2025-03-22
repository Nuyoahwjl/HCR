import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, project_root)

import streamlit as st
import pandas as pd
from agent.chain import RecommendationChain
import time


re=RecommendationChain()


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
    page_title="Recommendation",
    page_icon="🥰",
)
# st.sidebar.header("This project is a health check recommendation "
#                   "system built using LangChain, LangGraph, and DeepSeek LLM. "
#                   "It uses RAG technology to recommend health check packages based on user information.")
st.title("🩺Health Check Recommendation")
st.markdown("![](https://readme-typing-svg.herokuapp.com?color=000000FF&center=true&vCenter=true&width=800&lines=Hi+there+👋,+Welcome+to+HCR!;Please+fill+in+the+following+information+to+get+the+recommendation.+;)")

# with st.form("user_info"):
    # gender = st.selectbox("性别", ["男", "女"])
    # age = st.number_input("年龄", min_value=1, max_value=100)
    # height = st.slider("身高（cm）", 50, 200, 120)
    # weight = st.slider("体重（kg）", 20, 150, 50)
    # medical_history = st.text_area("既往病史", key="medical", height=100)
    # symptoms = st.text_area("当前症状", key="symptoms", height=100)
    # submitted = st.form_submit_button("生成推荐")

col1, col2 = st.columns(2)
with col1:
    gender = st.selectbox(label="Gender", 
                          options=["male", "female", "secret"],
                          format_func = str,
                          help = "if you don't want to tell us, keep secret")
    height = st.slider("Height(cm)", 50, 200, 150)
with col2:
    age = st.number_input("Age", 
                          min_value=1, 
                          max_value=100, 
                          value=15)
    weight = st.slider("Weight(kg)", 20, 100, 50)
medical_history = st.text_area("Medical History", key="medical")
symptoms = st.text_area("Symptoms", key="symptoms", height=100)
submitted = st.button("Recommend")

# res = None

if submitted:
    user_info = format_user_info(gender, age, height, weight, medical_history, symptoms)
    with st.spinner("analyzing..."):
        # time.sleep(2)
        start = time.time()
        result = re.run_chain(user_info)
        # result = "## 你好"
        with st.sidebar.expander(label=" ",expanded=True):
            st.success(f"successfully(time:{time.time()-start:.1f}s)")
            st.write(user_info)
        with st.expander("Recommendations", expanded=True):
            st.markdown("## RECOMMENDATIONS")
            st.write(result)
            st.download_button(
                label="download",
                data=result,
                file_name="Recommendations.md",
            )









# st.balloons()
# st.link_button(
#     label="Streamlit 文档",
#     url="https://docs.streamlit.io",
#     help="查看官方文档",
#     type="primary"
# )
# data = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
# csv_data = data.to_csv(index=False).encode("utf-8")
# st.download_button(
#     label="下载CSV",
#     data=csv_data,
#     file_name="dynamic_data.csv",
#     mime="text/csv"
# )
# code = '''def hello():
#             print("Hello, Streamlit!")'''
# st.code(code, language="python")

# st.time_input("选择时间")
# st.date_input("选择日期")