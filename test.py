import openai
import conf as config

# Load your API key from an environment variable or secret management service
openai.api_key = config.MY_API

response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',  # Use GPT-3.5 Turbo engine
        messages= [{"role": "user", "content": "Hello!"}, {"role": "assistant", "content": "Hi, how are you?"}],
        max_tokens=50,  # Adjust as needed
        temperature=0.7,  # Adjust as needed
        n=1,
        stop=None,
        timeout=15,
    )
print(response)