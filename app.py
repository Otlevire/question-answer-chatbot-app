from langchain_openai import OpenAI
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

def get_answer(question):
    llm= OpenAI(model_name="gpt-3.5-turbo-instruct")
    answer = llm.invoke(question)
    return answer

def get_question():
    user_question = st.text_input("You:", key="input")
    return user_question

## Application page title
title = "Grande Sábio"
st.set_page_config(page_title=title, page_icon=":robot:")
st.header(title)


user_question = get_question()
answer = get_answer(user_question)

submit = st.button("Fazer Pergunta")
if submit:
    st.subheader("Resposta:")
    st.write(answer)