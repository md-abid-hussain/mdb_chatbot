
-- Create engine for embedding
CREATE ML_ENGINE langchain_embedding
FROM langchain_embedding;

-- Create engine for model
CREATE ML_ENGINE langchain_engine
from langchain;

-- create embedding model using langchain, ollama and mistral
CREATE MODEL embedding_model
PREDICT embeddings
USING
  engine = 'langchain_embedding',
  class = 'OllamaEmbeddings', 
  model = 'mistral',
  base_url= 'http://localhost:11434';

-- Create llm model using langchain, ollama and mistral
CREATE MODEL lom
PREDICT answer 
USING
     engine = 'langchain_engine',       
     provider = 'ollama',               
     model_name = 'mistral',
     base_url= 'http://localhost:11434',             
     mode = 'conversational',           
     user_column = 'question',          
     assistant_column = 'answer',
     verbose = True,
     embedding_model_provider='embedding_model',
     prompt_template = 'Your task is to answer the question based on context. If question is out of context then do not answer.
     Question: {{question}} /
     Context: {{context}}';
