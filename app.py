import os
import warnings
import streamlit as st

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_classic.memory import ConversationBufferMemory
from langchain_classic.chains import LLMChain

# ---------------------------------
# Configuration
# ---------------------------------
warnings.filterwarnings("ignore")
load_dotenv()

st.set_page_config(
    page_title="Zomi | AI Food Assistant",
    page_icon="🍽️",
    layout="centered"
)

st.title("🍽️ Zomi")
st.caption("Your AI-powered food & restaurant assistant")

# ---------------------------------
# API Key
# ---------------------------------
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    st.error("❌ GROQ_API_KEY not found.")
    st.stop()

# ---------------------------------
# Conversation Memory
# ---------------------------------
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(
        memory_key="history",
        return_messages=True
    )

# ---------------------------------
# Chat History
# ---------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------------------
# Load Prompt Template
# ---------------------------------
try:
    with open("templete.txt", "r", encoding="utf-8") as file:
        prompt_template = file.read()
except FileNotFoundError:
    st.error("❌ templete.txt file not found.")
    st.stop()

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", prompt_template),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ]
)

# ---------------------------------
# Load LLM
# ---------------------------------
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=groq_api_key
)

chain = LLMChain(
    llm=llm,
    prompt=prompt,
    memory=st.session_state.memory
)

# ---------------------------------
# Sidebar
# ---------------------------------
with st.sidebar:
    st.header("🍴 Zomi")
    st.write(
        """
        Ask me about:
        - Restaurant recommendations
        - Food suggestions
        - Diet preferences
        - Zomato features
        - Cuisine ideas
        """
    )

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.session_state.memory = ConversationBufferMemory(
            memory_key="history",
            return_messages=True
        )
        st.rerun()

# ---------------------------------
# Display Previous Messages
# ---------------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------------------------
# Chat Input
# ---------------------------------
user_input = st.chat_input("Ask Zomi anything about food...")

if user_input:

    # User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # Assistant Response
    with st.chat_message("assistant"):
        with st.spinner("🍕 Cooking up the best answer..."):

            try:
                result = chain.invoke(
                    {
                        "input": user_input
                    }
                )

                response = result["text"]

            except Exception:
                response = (
                    "😔 Sorry! I'm unable to answer right now. "
                    "Please try again in a moment."
                )

            st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

