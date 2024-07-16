# Talk with Multiple LLM ChatBot

### Build using

- MindsDB
- Python
- Streamlit
- json-server
- Ollama
- Mistral

## Demo video

[![Multiple chatbot using mindsdb](https://markdown-videos-api.jorgenkh.no/url?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D7qsBVH1eUuQ)](https://www.youtube.com/watch?v=7qsBVH1eUuQ)

## Features
 - Create and edit chatbot
   ![Screenshot from 2024-07-16 17-56-25](https://github.com/user-attachments/assets/831ee40e-df9f-4fa9-a230-7f07b3ab26d4)

- Manage Chatbots
  ![Screenshot from 2024-07-16 17-56-39](https://github.com/user-attachments/assets/f9d7e0b1-5f5d-47f8-b608-e485ded07a56)

- Select and chat with chabot

  ![Screenshot from 2024-07-16 17-27-11](https://github.com/user-attachments/assets/654bb95d-89e7-4429-8e52-c60e427eb786)

- Chatbot respond with context
  ![Screenshot from 2024-07-16 17-09-46](https://github.com/user-attachments/assets/2f5230a9-c0fa-4d02-8eae-0166ddce5b19)
  ![Screenshot from 2024-07-16 17-26-12](https://github.com/user-attachments/assets/c14cd699-c344-4433-913b-cb59f67009ef)

<hr>

## Project setup

### Ollama mistral setup

- Install Ollama [Link](https://ollama.com/)
- Download Mistral model after installing ollama by running
  `ollama run mistral`

### Mindsdb setup

- Run `docker compose up` if you want to run mindsdb with gpu or `docker run --name mindsdb_container -p 47334:47334 -p 47335:47335 mindsdb/mindsdb` to run mindsdb with cpu
- Follow the instruction to install dependencies if needed [Link](https://docs.mindsdb.com/setup/self-hosted/docker#install-dependencies)
- Open mindsdb editor and run the command from mdb.sql one by one
- Make sure ollama is running

### Project setup

- create virtual environment `python3 -m venv .ven`
- Activate virtual environment `source .venv/bin/activate`
- Install requirements files `pip install -r requirements.txt`
- Install json-server `npm install -g json-server`
- Run json-server with db.json `json-server db.json --watch`
- Run streamlit using `streamlit run Home.py`

