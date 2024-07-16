import streamlit as st
from utils.BotPage import BotPage
from utils.crud_bots import get_bots

st.set_page_config(page_title="Multi Chatbot", layout="wide")
custom_css = """
<style>
    p{
        font-size: 18px !important;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)


def get_pages():
    bots = get_bots()
    pages = {
        bot["name"]: BotPage(bot["name"], bot["context"], bot["description"])
        for bot in bots
    }
    return pages


pages = get_pages()

selected_bot_name = st.sidebar.selectbox(
    "Select your chat bot", options=list(pages.keys())
)

if selected_bot_name:
    selected_page = pages[selected_bot_name]
    selected_page.display()
