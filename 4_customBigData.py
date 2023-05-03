from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

import os
from info import *

openaikey = getOpenAIkey()
os.environ["OPENAI_API_KEY"] = openaikey
llmModel = OpenAI()

#read raw_text from file cityInfo.txt
with open("cityInfo.txt","r",encoding="utf-8") as file:
    raw_text = file.read()

cts = CharacterTextSplitter(
    separator="\n",
    chunk_size=1000,
    chunk_overlap=200,
    length_function = len,
)

texts = cts.split_text(raw_text)
embeddings = OpenAIEmbeddings()

docSearch = FAISS.from_texts(texts,embeddings)

from langchain.chains.question_answering import load_qa_chain
chain = load_qa_chain(llmModel,chain_type="stuff")

while True:
    query =  input("Please ask your question about a city : ")
    docs = docSearch.similarity_search(query)
    result = chain.run(input_documents=docs,question=query)
    print(result)
    print("--------------------------------------------------")






