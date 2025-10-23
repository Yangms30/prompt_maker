import streamlit as st
from langchain_core.messages.chat import ChatMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_teddynote.prompts import load_prompt
import glob
from dotenv import load_dotenv

# Create a LANGSMITH_API_KEY in Settings > API Keys
from langsmith import Client

load_dotenv()

client = Client()
prompt = client.pull_prompt("hardkothari/prompt-maker", include_model=True)
print(prompt)
st.title("My Own ChatGPT")

# 처음 대화를 시작할때 messages라는 대화를 담을 리스트 생성
if "messages" not in st.session_state:
    st.session_state["messages"] = []

with st.sidebar:
    clear_btn = st.button("대화 초기화")
    task_input = st.text_input("TASK 입력", "")


def print_messages():
    for chat_message in st.session_state["messages"]:
        st.chat_message(chat_message.role).write(chat_message.content)


def add_message(role, message):
    st.session_state["messages"].append(ChatMessage(role=role, content=message))


def create_chain(prompt,task=""):

    if task:
        prompt = prompt.partial(task=task)

    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
    parser = StrOutputParser()

    chain = prompt | llm | parser
    return chain


if clear_btn:
    st.session_state["messages"] = []

print_messages()

user_input = st.chat_input("무엇이든 물어보세요!")
if user_input:
    st.chat_message("user").write(user_input)
    chain = create_chain(prompt,task=task_input)
    response = chain.stream({"lazy_prompt": user_input})
    with st.chat_message("assistant"):
        container = st.empty()

        ai_answer = ""
        for token in response:
            ai_answer += token
            container.markdown(ai_answer)

    add_message("user", user_input)
    add_message("assistant", ai_answer)
