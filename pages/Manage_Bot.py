import streamlit as st
from utils.crud_bots import create_bot, delete_bot, get_bots, update_bot
from streamlit_modal import Modal

st.set_page_config(layout="wide")


# Initialize session state for editing
if "edit_bot_id" not in st.session_state:
    st.session_state.edit_bot_id = None
    st.session_state.bot_name = ""
    st.session_state.bot_context = ""
    st.session_state.bot_description = ""

modal = Modal("Create/Edit Chat Bot", key="create_edit")

st.title("Manage Your Bots Here")
st.divider()

col1, col2 = st.columns([2, 1])
with col1:
    st.subheader("Create ChatBot")

with col2:
    open_modal = st.button("Create")

st.divider()

st.subheader("Existing models")
if open_modal:
    # Reset session state for creating a new bot
    st.session_state.edit_bot_id = None
    st.session_state.bot_name = ""
    st.session_state.bot_context = ""
    st.session_state.bot_description = ""
    modal.open()

# Display existing bots
bots = get_bots()
for bot in bots:
    st.markdown(f"**Name:** {bot['name']}")
    st.markdown(f"**Context:** {bot['context']}")
    st.markdown(f"**Description:** {bot['description']}")
    col1, col2 = st.columns([1, 2])
    with col1:
        if st.button("Edit", key=f"edit_{bot['id']}"):
            # Set session state for editing an existing bot
            st.session_state.edit_bot_id = bot["id"]
            st.session_state.bot_name = bot["name"]
            st.session_state.bot_context = bot["context"]
            st.session_state.bot_description = bot["description"]
            modal.open()
    with col2:
        if st.button("Delete 🗑️", key=f"delete_{bot['id']}", help="Delete"):
            delete_bot(bot["id"])
            st.experimental_rerun()
    st.divider()

if modal.is_open():
    with modal.container():
        with st.form("bot_form"):
            bot_name = st.text_input("Bot Name", value=st.session_state.bot_name)
            bot_context = st.text_input(
                "Bot Context", value=st.session_state.bot_context
            )
            bot_description = st.text_area(
                "Bot Description", value=st.session_state.bot_description
            )
            submitted = st.form_submit_button(
                "Submit" if st.session_state.edit_bot_id is None else "Update"
            )

            if submitted:
                bot_data = {
                    "name": bot_name,
                    "context": bot_context,
                    "description": bot_description,
                }
                if st.session_state.edit_bot_id:
                    update_bot(st.session_state.edit_bot_id, bot_data)
                    modal.close()
                else:
                    create_bot(bot_data)
                    modal.close()
                # Reset session state after submission
                st.session_state.edit_bot_id = None
                st.session_state.bot_name = ""
                st.session_state.bot_context = ""
                st.session_state.bot_description = ""
                st.experimental_rerun()
