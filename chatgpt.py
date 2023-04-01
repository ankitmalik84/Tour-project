import openai
import time

# Set up OpenAI API credentials
openai.api_key = "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"

# Set up OpenAI API parameters
model_engine = "davinci" # Choose the GPT-3 model to use
temperature = 0.5 # Controls the "creativity" of the chatbot's responses
max_tokens = 150 # Maximum number of tokens (words) to generate per response
stop_sequence = "\n" # Sequence of characters to use as stopping criteria for the API

# Define a function to interact with the OpenAI API
def generate_response(prompt):
    try:
        response = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens,
            stop=stop_sequence
        )
        time.sleep(1) # Pause for 1 second to avoid hitting API rate limit
        return response.choices[0].text.strip()
    except Exception as e:
        print("Error: " + str(e))

# Define a function to start the chatbot
def start_chatbot():
    print("Welcome to the chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        prompt = f"You: {user_input}\nChatbot:"
        response = generate_response(prompt)
        print(f"Chatbot: {response}")

# Start the chatbot
start_chatbot()
