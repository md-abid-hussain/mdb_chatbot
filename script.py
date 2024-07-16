from utils.crud_bots import create_bot

bots = [
    {
        "type": "math_bot",
        "name": "Math AI",
        "context": "Only answer math related question",
        "description": "This AI-powered chatbot is designed to assist with a wide range of mathematical queries. Whether you're dealing with algebra, calculus, geometry, or even more advanced topics, Math AI is here to provide explanations, solve equations, and help you understand complex mathematical concepts.",
    },
    {
        "type": "python_bot",
        "name": "Python AI",
        "context": "Only answer Python related question.",
        "description": "Python AI is your go-to source for solving Python programming challenges, understanding concepts, and debugging code.",
    },
    {
        "type": "javascript_and_typescript_bot",
        "name": "JavaScript/TypeScript AI",
        "context": "Only answer JavaScript/TypeScript related question.",
        "description": "JavaScript/TypeScript AI is your go-to source for solving JavaScript/TypeScript programming challenges, understanding concepts, and debugging code.",
    },
    {
        "type": "java_bot",
        "name": "Java AI",
        "context": "Only answer Java related question.",
        "description": "Java AI is your go-to source for solving Java programming challenges, understanding concepts, and debugging code.",
    },
    {
        "type": "php_bot",
        "name": "PHP AI",
        "context": "Only answer PHP related question",
        "description": "PHP AI assists with PHP programming queries, from basic syntax to advanced web development topics.",
    },
    {
        "type": "react_bot",
        "name": "ReactJS AI",
        "context": "Only answer React related question",
        "description": "ReactJS AI helps you navigate the complexities of React development, offering solutions and explanations for your React-related questions.",
    },
]

if __name__ == "__main__":
    for bot in bots:
        create_bot(bot)
