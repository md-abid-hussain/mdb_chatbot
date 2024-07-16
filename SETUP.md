# Project setup

## Ollama mistral setup

- Install Ollama [Link](https://ollama.com/)
- Download Mistral model after installing ollama by running
  `ollama run mistral`

## Mindsdb setup

- Run docker compose up
- Follow the instruction to install dependencies if needed [Link](https://docs.mindsdb.com/setup/self-hosted/docker#install-dependencies)
- Open mindsdb editor and run the command from mdb.sql one by one
- Make sure ollama is running

## Project setup

- create virtual environment `python3 -m venv .ven`
- Activate virtual environment `source .venv/bin/activate`
- Install requirements files `pip install -r requirements.txt`
- Install json-server `npm install -g json-server`
- Run json-server with db.json `json-server db.json --watch`
- Run streamlit using `streamlit run Home.py`
