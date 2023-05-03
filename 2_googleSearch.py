import langchain
from langchain.agents import load_tools, initialize_agent
from langchain.llms import OpenAI
import os
from info import *

openaikey = getOpenAIkey()
serpapikey = getserpAPIkey()

os.environ["OPENAI_API_KEY"] = openaikey
os.environ["SERPAPI_API_KEY"] = serpapikey


model = OpenAI(temperature=0.7)
tool = load_tools(["serpapi","llm-math"],llm=model)

agent = initialize_agent(tools=tool, llm=model,agent="zero-shot-react-description",verbose=True)


while True:
    prompt = input("Please enter your question : ")
    result = agent.run(prompt)
    print(result)
    print("--------------------------------------------------")