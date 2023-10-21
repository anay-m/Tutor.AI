import openai as ai



def get_completion(prompt, model = "gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = ai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.5,
    )
    return response.choices[0].message["content"]

def decideUseCase(prompt, response, user_input):
    if(response.lower() == "math" or response.lower() == "computer science"):
        get_wolfram_response(prompt, response, user_input)

    else:
        get_completion()


import requests
def get_wolfram_response(prompt, user_input):
    app_id = '7A8VKL-UJHU527WW4'
    wolfram_url = f"https://api.wolframalpha.com/v2/query?input={user_input}&format=plaintext&output=JSON&appid={app_id}"
    response = requests.get(wolfram_url)
    wolfram_response = response.json()  # Navigate the JSON structure to get the desired result.
    print(wolfram_response)

#get_wolfram_response("Hi", "Provide a step by step solution explaining how to solve x^2 + 5x + 7 = 0 to find the root.")

from xml.etree import ElementTree
def wolframResponse():
    endpoint = "http://api.wolframalpha.com/v2/query"
    params = {
    "input": "x^2 + 2x + 5 = 0",
    "format": "plaintext",
    "appid": "7A8VKL-UJHU527WW4"  # Replace with your AppID
    }
    # Make the API call
    response = requests.get(endpoint, params=params)
    tree = ElementTree.fromstring(response.content)
    for pod in tree.findall(".//pod"):
        if pod.get("title") == "Roots":
            for plaintext in pod.findall(".//plaintext"):
                print(plaintext.text)

wolframResponse()