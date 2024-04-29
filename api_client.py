import requests
import json

def query_api(prompt):
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "mistral", # Change model name here
        # "model": "llama2",
        "prompt": "Answer short, "+prompt
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        complete_response = ""
        for line in response.iter_lines():
            if line:
                json_response = line.decode('utf-8')
                parsed_response = json.loads(json_response)
                complete_response += parsed_response["response"]
                if parsed_response.get("done", False):
                    break
        return complete_response
    else:
        return "Failed to fetch response"

def log_conversation(prompt, response):
    with open("conversation_log.txt", "a") as file:
        file.write(f"Prompt: {prompt}\nResponse: {response}\n\n")

def main():
    while True:
        prompt = input("Enter your prompt (to quit type 'exit'): ")
        if prompt.lower() == 'exit':
            break
        response = query_api(prompt)
        print("Mistral API response:", response)
        log_conversation(prompt, response)

if __name__ == "__main__":
    main()
