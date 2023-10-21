import openai as ai
import os
import wolframalpha
#ai.api_key = os.environ["AI_KEY"] 

import wolframalpha
import requests

def get_wolfram_response1(input):
    params = {
        "input": input,
        "podstate": "Step-by-step solution",
        "format": "plaintext",
        "appid": "7A8VKL-UJHU527WW4"
    }
    endpoint = f"http://api.wolframalpha.com/v2/query"
    response = requests.get(endpoint, params= params)
    return response.text
    

print(get_wolfram_response1("Taylor of x^2 - 3x - 10 = 0"))