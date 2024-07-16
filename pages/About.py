import streamlit as st

# Set page configuration
st.set_page_config(page_title="About", layout="wide")

# Page title
st.title("About This Tool")

# Technology Used Section
st.header("Technology Used")
st.markdown(
    """
- **Python**: The primary programming language used.
- **Streamlit**: For creating the web application.
- **Mindsdb**: For creating and managing Chatbot.
- **Langchain**: As ml engine in mindsdb.
- **Ollama**: For using mistral.
- **Mistral**: As LLM.
- **JSON Server**: As backend server.
"""
)

# About Me Section
st.header("About Me")
st.markdown(
    """
Hello! I'm the developer behind this innovative chatbot management tool. My journey in software development has been driven by a passion for creating intelligent systems that enhance human productivity and creativity. This project is a culmination of my interests in artificial intelligence, web development, and user experience design.

I designed this tool to empower users to seamlessly create, manage, and deploy chatbots for various applications, leveraging cutting-edge technologies like Mindsdb, Langchain, and Streamlit. My goal is to make AI more accessible and to provide a platform where both developers and non-technical users can interact with and benefit from the power of machine learning.

I'm always looking for feedback and ways to improve this tool, so please don't hesitate to reach out with suggestions or questions. Let's push the boundaries of what's possible with AI together!

Feel free to connect with me on my socials or drop me an email. Your insights and connections are invaluable to the continuous improvement and success of this project.
"""
)

# Social Links Section
st.header("Connect with Me")
st.markdown(
    """
- [GitHub](https://github.com/md-abid-hussain)
- [LinkedIn](https://www.linkedin.com/in/md-abid-hussain-52862b229)
- [Hashnode](https://hashnode.com/@mdabidhussain)
"""
)

# Optional: Add images or additional sections as needed
