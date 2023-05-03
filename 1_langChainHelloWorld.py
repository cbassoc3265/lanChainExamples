import langchain
import openai
from info import *
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

#openai.api_key = getOpenAIkey()
import os
os.environ["OPENAI_API_KEY"] = getOpenAIkey()



llm = OpenAI(temperature=0.5)

#result = llm("Please tell me which places to visit is better in the summer in Antalya")
#print(result)

pTemplate = PromptTemplate(
    input_variables=["place", "season"],
    template="make a list of places to visit in the season of {season} in {place}, only list no description",
)

#print(llm(pTemplate.format(place="New York", season="autumn")))

chain = LLMChain(llm = llm,prompt = pTemplate)

result = chain.run({"place":'Isparta', "season":'winter'})
print(result)

