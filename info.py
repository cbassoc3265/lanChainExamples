def getOpenAIkey():
    #get openai key from key.txt in keys folder
    with open("keys/openai.txt", "r") as f:
        key = f.read()
    return key

def getserpAPIkey():
    #get openai key from key.txt in keys folder
    with open("keys/serpapi.txt", "r") as f:
        key = f.read()
    return key


