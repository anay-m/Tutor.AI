import os
import openai as ai
import json

def lambda_handler(event, context):
    ai.api_key = os.environ["AI_KEY"]  # Set OpenAI API key from environment variable

    instructions = [{'role': 'system', 'content': """You are an AI tutor designed to assist students in various subjects, limited to 
             Math, Physics, Biology, Chemistry, English, History, and Computer Science. You will first receive user input asking 
             a question. To construct an output, follow these steps:
             
             Step 1) You will output the subject of the question like this: subject.  Make the subject general and restricted 
             to subjects "Math, Physics, Biology, Chemistry, English, History, Computer Science". If the question is asking anything 
             about how something was founded or who created some theory, it is automatically history. If the user input is not about learning something new (such as what is the game score today?), then 
             output "Invalid prompt. Please input a question you have to learn something new! :)"
             
             Step 2) At the end of the string, write ; 
             If the User explicitely includes a calculation, meaning numbers and a formula is involved where they EXPLICITELY SAY they want it solved; True
             (The user MUST include numbers or a formula and EXPLICITLY STATE they want it solved.) Or else if there is no calculation that is needed to be solved
             for example if a user asks you to teach them a concept but doesn't ask you to solve a problem or calculation then it is; False

             Step 3) At the end of the string, add ; If step 2's output was True, DO NOT SOLVE IT instead output STRICTLY the formula/equation/procedure 
             that needs to be solved/calculated and what needs to be done on that formula/equation/procedure so it can be solved by a separate model that 
             can only handle commands like "Integrate <Formula>" or "Taylor of <Formula>" or "Derivative of <Formula>" Where <Formula> is the formula 
             that was asked to be solved by user. That is STRICTLY ALL you will output if step 2 is True. If it is false you can give a conceptual explanation
             and give a detailed understanding as if you are a tutor teaching the user. 
             
             
             """ }]

    prompt = event["prompt"]

    response = collect_messages(instructions, prompt)
    return {
        'subject': response[0],
        'calculation': bool(response[1]),
        'answer': response[2],
        'prompt': response[3]
    }

def get_completion(prompt, model="gpt-4"):
    messages = [{"role": "user", "content": prompt}]
    response = ai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.5,
    )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-4"):
    response = ai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.5,
    )
    return response.choices[0].message["content"]

def collect_messages(context, prompt):
    context.append({'role': 'user', 'content': f"{prompt}"})
    response = get_completion_from_messages(context)
    subject = (response).split(';')
    subject.append(prompt)
    return subject
