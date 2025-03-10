from PIL import Image
import requests
import base64
import json



with open("images/C2M2.8_Linux_Installation_2024(1).pdf_page3_1.jpeg", "rb") as image_file:
    image_data = base64.b64encode(image_file.read()).decode()

# Define the prompt for the model
prompt = "Write me a description of the image/diagram and if it contains text convert image to text."

# Prepare the payload for the POST request
payload = {
    "model": "llava",
    "prompt": prompt,
    "images": [image_data]
}

# Send the POST request
response = requests.post(api_endpoint, json=payload)

# Check if the request was successful
if response.status_code == 200:
    generated_text = ""
    for item in response.iter_lines():
        item = json.loads(item)
        generated_text += item.get("response", "")
    # Print the generated text
    print("Generated Text:", generated_text)
else:
    print("Error:", response.text)