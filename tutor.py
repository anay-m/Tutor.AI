import openai as ai
import os

ai.api_key = os.environ["AI_KEY"] #api key access to gpt versions

def get_completion(prompt, model = "gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = ai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.5,
    )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model = "gpt-3.5-turbo"):
    response = ai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.5,
    )
    return response.choices[0].message["content"]

def collect_messages():
    context.append({'role':'user', 'content':f"{prompt}"})
    response = get_completion_from_messages(context)
    subject = (response).split(';')
    subject.append(prompt)
    return subject
    

context = [ {'role':'system', 'content': """You are an AI tutor designed to assist students in various subjects, limited to 
             Math, Physics, Biology, Chemistry, English, History, and Computer Science. You will first receive user input asking 
             a question. To construct an output, follow these steps:
             
             Step 1) You will output the subject of the question like this: subject.  Make the subject general and restricted 
             to subjects "Math, Physics, Biology, Chemistry, English, History, Computer Science". If the question is asking anything 
             about how something was founded or who created some theory, it is automatically history. If the user input is not about learning something new (such as what is the game score today?), then 
             output "Invalid prompt. Please input a question you have to learn something new! :)"
             
             Step 2) At the end of the string, write ; 
             If the user input doesnt require a calculation write ;False, OR if the input requires a calculation (meaning the user is asking
             how to calculate something and provides sample numbers to input into a formula. The user must provide sample numbers, or 
             else no calculation is required.) write ;True Recall this step's output for the next step.
             
             Step 3) At the end of the string, add ; If there step 2's output was True, output " ", else if step 2's output was False, 
             output 2-4 sentences providing an strictly conceptual overview of the answer to the user's question.
             """ 
             } ]

prompt = input("Hi, welcome to Tutor AI, what would you like to learn today? \nUser:")
# response = collect_messages()
# print((response))

while prompt:
    response = collect_messages()
    prompt = input(response[2] + "\nUser:")