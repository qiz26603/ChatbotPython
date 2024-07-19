import openai
import streamlit as st

view = """
Chào mừng bạn đén với qiBot! Đây là một chatbot có thể hỗ trợ, giúp bạn viết code khiến cho tiến trình viết code của bạn nhanh hơn, bạn đỡ mệt mỏi hơn.
qiBot sẵn sàng để giúp bạn trở thành một coder xịn xò hơn cho dù là người mới hay có nhiều kinh nghiệm,
chatbot này là thứ cần thiết để hỗ trợ bạn bất cứ lúc nào bạn cần.
"""

st.markdown("<h1 style='text-align: center;'>qiBot Code ✨</h1>", unsafe_allow_html=True)
st.markdown("---")

with st.sidebar:
    st.image("friendly-chatbot.jpg")
    st.title("qiBot Code")
    st.caption(f'''{view}''', unsafe_allow_html=False)
   
language=st.selectbox("Choose a language you want to support code:", ("Python", "C++", "Java", "Pascal"))
question=st.text_area("Ask a question under the box:")
button=st.button("Send")

def answer(question):
    openai.api_key="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" # API key của OpenAI
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"""{question} {language}""",
        temperature=0,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
    return response.choices[0].text

if question and button:
    with st.spinner("Wait a minutes !"):
        reply=answer(question)
        st.code(reply)
        button2=st.button("Clear")