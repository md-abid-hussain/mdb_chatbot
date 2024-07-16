import streamlit as st
from mindsdb_sdk import connect

server = connect()
mindsdb = server.get_project("mindsdb")
model = mindsdb.get_model("lom")


class BotPage:
    def __init__(
        self,
        name,
        context,
        description,
    ):
        self.name = name
        self.context = context
        self.description = description
        self.session_name = f"{name}_session"

    def display(self):
        """Display the page content."""
        st.title(self.name)
        st.caption(self.description)

        def get_bot_response(question, context):
            with st.spinner("Waiting for the bot response..."):
                response = model.predict({"question": question, "context": context})
            return response["answer"][0]

        if self.session_name not in st.session_state:
            st.session_state[self.session_name] = [
                {"role": "assistant", "content": "How can I help you?"}
            ]

        for msg in st.session_state[self.session_name]:
            st.chat_message(msg["role"]).write(msg["content"])

        if prompt := st.chat_input():
            st.session_state[self.session_name].append(
                {"role": "user", "content": prompt}
            )
            st.chat_message("user").write(prompt)

            with st.chat_message("assistant"):
                msg = get_bot_response(prompt, self.context)
                st.session_state[self.session_name].append(
                    {"role": "assistant", "content": msg}
                )
                st.write(msg)
