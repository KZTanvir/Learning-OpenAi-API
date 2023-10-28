import os
import openai
import conf as config

from docx import Document
def conv_doc(docx_path):
    doc = Document(docx_path)
    paragraphs = [p.text for p in doc.paragraphs]
    text = '\n'.join(paragraphs)
    return text

# Load your API key from an environment variable or secret management service
openai.api_key = config.MY_API

def send_message(messages):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',  # Use GPT-3.5 Turbo engine
        messages=messages, # Adjust as needed
        temperature=0.7,  # Adjust as needed
        n=1,
        stop=None,
        timeout=30,
    )

    if response and response.choices:
        #return response.choices[0].message['content']
        return response
    
    return None

messages = []
messages.append({"role": "assistant",
                 "content": "You are an ai that will act like a jarvis ai from iron man even if you dont have that much power."})
messages.append({"role": "assistant",
                 "content": "Now When Someone asks about you, just reply with your name that is jarvis."})
messages.append({"role": "assistant",
                 "content": "You can start the conversation by typing your message."})



print("Welcome to the JarvisGPT !")
print("You can start the conversation by typing your message.")
print("You can also use 'system' messages to provide context or instructions.")
while True:
    user_input = input("\nYou: ")
    if user_input == "quit":
        break
    elif user_input == "docx":
        doc_file = input("Enter the path of the docx file: ")
        scrapped_text = conv_doc(doc_file)
        scrapped_text = scrapped_text + "now explain in english in easy words"
        messages.append({"role": "user", "content": scrapped_text})
        response = send_message(messages)


    # Add user message to the conversation
    if user_input != "docx":
        messages.append({"role": "user", "content": user_input})
        # Send messages to the chatbot
        response = send_message(messages)

    if response:
        # Print chatbot response
        reply = response.choices[0].message['content']
        
        print("\n=================JarvisGPT=======================\n")
        print(reply)
        print("\n=================JarvisGPT=======================\n")
        
        # Add chatbot response to the conversation
        messages.append({"role": "assistant", "content": reply})
        messages.pop(2)
        messages.pop(2)
    else:
        print("Sorry, I didn't understand that. Can you please rephrase?")