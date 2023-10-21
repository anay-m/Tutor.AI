import openai as ai
import os

ai.api_key = os.environ["AI_KEY"] #api key access to gpt versions

def get_completion(prompt, model = "gpt-4"):
    messages = [{"role": "user", "content": prompt}]
    response = ai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.5,
    )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model = "gpt-4"):
    response = ai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.5,
    )
    return response.choices[0].message["content"]

def collect_messages():
    context.append({'role':'user', 'content':f"{prompt}"})
    response = get_completion_from_messages(context)
    subject = (response).split('\n')
    subject.append(prompt)
    return subject
    

context = [ {'role':'system', 'content': """You are an AI tutor's assistant designed to assist students in various subjects, limited to Math, 
             Physics, Biology, Chemistry, English, History, and Computer Science. You will first receive user input asking a question. 
             Your job is to generate three titles for 3 different sections to further detail different aspects of the answer, and outputting the detailed content
             for the sections themselves. The breakdown of these secton will depend on the type of question, subject, etc. 
             
             One approach, for example in a math question, might be to provide an introduction to the topic, an insight into the theory/intuition behind it, and 
             a formula for it. For something Computer Science programming related, you may provide an introduction of the topic, the theory/intuition, and an 
             implementation in a certain programming language. For a subject like English/Grammar, you may split it into introduction, rules/how it works, and examples.
             For something history related, you might split it into overview, sides on the matter, specific timeline.
             
             These are JUST EXAMPLES, remember to adapt your sections to each specific question and subject.
             Then, for each title, generate the accompanying description/explanation that will serve to teach the user. It should be descriptive, informative, 
             and detailed enough to fully explain aspects of the topic. Keep it within 8 sentences.
             
             Once you have decided the three sections, output an unnumbered list of the section titles, which should be no more than 3-4 words, along with 
             the content you would include in each model, which should be 250-350 words per section, as follows:
             Title1
             Content1
             Title2
             Content2
             Title3
             Content3""" 
             } ]

prompt = input("Hi, welcome to Tutor AI, what would you like to learn today? \nUser:")
response = collect_messages()
print((response))

# while prompt:
#     response = collect_messages()
#     prompt = input(response + "\nUser:")