from openai import OpenAI
import base64
import json
from io import BytesIO
from PIL import Image
from config import config 

def process_image(image_path, client):

    with Image.open(image_path) as img:
        buffer = BytesIO()
        img.save(buffer, format="JPEG")
        buffer.seek(0)
        base64_image = base64.b64encode(buffer.read()).decode("utf-8")
        image_data_uri = f"data:image/jpeg;base64,{base64_image}"

    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=0.2,  
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": config.GPT_PROMPT},
                    {"type": "image_url", "image_url": {"url": image_data_uri}}
                ]
            }
        ]
    )

    gpt_output = response.choices[0].message.content

    result = {
        "gpt_prompt": config.GPT_PROMPT,
        "gpt_output": gpt_output
    }

    # Save JSON 
    filename = image_path.split("/")[-1].replace(".JPG", "_results.json")
    output_path = config.RESULTS_FOLDER_PATH +  filename
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    
    client = OpenAI(api_key=config.GPT_API_KEY)

    for i in range(1, 26):
        image_path = config.IMAGE_FOLDER_PATH + str(i) + ".JPG"
        process_image(image_path, client)