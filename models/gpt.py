from openai import OpenAI
from config import config
import base64
import cv2
from PIL import Image
from io import BytesIO

def get_person_info(descriptions):

    client = OpenAI(api_key=config.GPT_API_KEY)

    prompt = config.GPT_PROMPT_DESCRIPTION + descriptions
    
    response = client.responses.create(
        model="gpt-4o",
        temperature=0.2,
        input=prompt
    )

    return response.output_text

def generate_description(image, client):
    
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(image_rgb)

    # Save to BytesIO buffer
    buffer = BytesIO()
    pil_image.save(buffer, format="JPEG")
    buffer.seek(0)

    # Encode as base64
    base64_image = base64.b64encode(buffer.read()).decode("utf-8")
    image_data_uri = f"data:image/JPEG;base64,{base64_image}"

    # API request
    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=0.2,
        messages=[
            {
                "role": "user",
                "content": [
                    { "type": "text", "text": config.GPT_PROMPT_IMAGE },
                    { "type": "image_url", "image_url": { "url": image_data_uri } }
                ]
            }
        ]
    )

    return response.choices[0].message.content

def generate_descriptions(images):

    client = OpenAI(api_key=config.GPT_API_KEY)

    descriptions = []

    for image in images:
        descriptions.append(generate_description(image, client))

    return descriptions

'''
if __name__ == "__main__":
    
    for i in range(1, 26):
        file_path = os.path.join("results/", f"{i}_results.json")
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                data = json.load(file)
                output_raw = data.get("output_raw", "")
                output = get_person_info(output_raw)
                data["output"] = output
            with open(file_path, "w") as file: 
                json.dump(data, file, indent=4)
'''