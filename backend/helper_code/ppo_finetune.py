import torch
from transformers import PPOTrainer, PPOConfig
from transformers import AutoTokenizer
import requests
import json

class OllamaEnv:
    def __init__(self, model_name, server_url):
        self.model_name = model_name
        self.server_url = server_url
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

    def get_reward(self, feedback):
        return feedback - 3  # Neutral feedback (3) gives 0 reward

    def generate_response(self, prompt):
        response = requests.post(
            f"{self.server_url}/generate",
            json={"model": self.model_name, "prompt": prompt}
        )
        return response.json()["text"]

    def step(self, prompt, feedback):
        response_text = self.generate_response(prompt)
        reward = self.get_reward(feedback)
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.tokenizer(response_text, return_tensors="pt")
        return reward, inputs, outputs

def fine_tune_model(model_name, server_url, history):
    config = PPOConfig()
    env = OllamaEnv(model_name, server_url)
    trainer = PPOTrainer(model=model_name, config=config)

    for entry in history:
        if entry['role'] == 'assistant':
            prompt = entry['content']
            feedback = entry['feedback']
            reward, inputs, outputs = env.step(prompt, feedback)
            trainer.step(inputs, outputs, reward)

if __name__ == "__main__":
    model_name = "llama3:instruct"
    server_url = "http://127.0.0.1:11434"  # Replace with your actual Ollama server URL
    history = []  # Load your conversation history here

    with open("history.json", "r") as f:
        history = json.load(f)

    fine_tune_model(model_name, server_url, history)
