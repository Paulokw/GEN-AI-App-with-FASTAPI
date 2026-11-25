from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()
from langchain_core.output_parsers import StrOutputParser
from langserve import add_routes

api_key = os.getenv("OPENAI_API_KEY")

llm=ChatOpenAI(model="gpt-5.5")

prompt=ChatPromptTemplate.from_messages([
    ("system","translate the following into {language}"),
    ("user","{input}")
])

parser=StrOutputParser()
chain= prompt| llm| parser


app=FastAPI(title="langchain server",
            version="1.0",
            description="API server using langchain runnable interfaces")

add_routes(
    app,
    chain,
    path="/chain"
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="localhost",port=8000)