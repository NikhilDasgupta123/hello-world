import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage


from dotenv import load_dotenv
load_dotenv()


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.markdown(message.content)
    else:
        with st.chat_message("AI"):
            st.markdown(message.content)


user_query = st.chat_input("Your Message")
if user_query is not None and user_query!="":
    st.session_state.chat_history.append(HumanMessage(user_query))

    with st.chat_message("Human"):
        st.markdown(user_query)

    with st.chat_message("AI"):
        ai_response = "I dont know"
        st.markdown(ai_response)

    st.session_state.chat_history.append(AIMessage(ai_response))
    