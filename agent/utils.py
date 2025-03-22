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