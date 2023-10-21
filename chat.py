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
    context = [ {'role':'system', 'content': f"""You are an AI tutor designed to assist students in {subject}. You will first receive user input asking 
             a question. You will then determine the subject of the question.  Make the subject general and restricted 
             to subjects "Math, Physics, Biology, Chemistry, English, History, Computer Science". If the question is asking anything 
             about how something was founded or who created some theory, it is automatically history. Output the subject using the following format, subject )"
             """ 
             } ]
    context.append({'role':'user', 'content':f"{prompt}"})
    context1.append({'role':'user', 'content':f"{prompt}"})
    response = get_completion_from_messages(context)
    if response == subject:
        response = get_completion_from_messages(context1)
        
    else:
        response = f"Please input a question about your current subject {subject}. If you want to change topics, scroll up to the top of the page and generate new modules! :)"
    context1.append({'role':'assistant', 'content':f"{response}"})
    return response

subject = "Math"
context1 = [ {'role':'system', 'content': f"""You are an AI tutor designed to assist students in {subject}. You will first receive user input asking 
             a question. Answer the question in 2-3 sentences.)"
             """ 
             } ]

prompt = input("Any follow up questions? \nUser:")
while prompt:
    response = collect_messages()
    prompt = input(response + "\nUser:")