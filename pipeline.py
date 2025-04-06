from models import llava, gemini_api, fastrcnn, gpt
from utils import bounding_box, image_utils, clustering
from config import config
from utils import utils
import cv2
import re

def process_image(image_path):
    """
    Main pipeline function.
    """

    # 0. Load the image to process
    image = cv2.imread(image_path)
    image_filename = image_path.split("/")[-1]

    # 1. Detect people in the image and get their bounding boxes
    boxes = fastrcnn.detect_people(image)

    # 2. Padding bounding boxes 
    boxes = bounding_box.padding_bounding_boxes(boxes, image)

    # 3. Cluster bounding boxes
    clustered_boxes = clustering.cluster_boxes(boxes) 
    
    # 3.1 Draw bounding boxes and save the image
    image_utils.draw_and_save_image_bb(image, image_filename, clustered_boxes)

    # 4. Crop images
    cropped_images = []
    for box in clustered_boxes:
        cropped_images.append(image_utils.crop_image(image, box))

    # 5. Generate LLaVA descriptions    
    descriptions = llava.generate_descriptions(cropped_images)

    # 5. Generate GPT descriptions
    descriptions = gpt.generate_descriptions(cropped_images)

    # 6. Merge MLLM outputs
    merged_description = str(descriptions)

    # 7. Get person information from Gemini API
    #person_info = gemini_api.get_person_info(merged_description) 
    
    # 7. Get person information from GPT API
    person_info = gpt.get_person_info(merged_description)

    filename_result = image_filename.replace(".JPG", "_results.json")
    utils.save_results_as_json(config.GPT_PROMPT_IMAGE, config.GPT_PROMPT_DESCRIPTION, merged_description, person_info, config.RESULTS_FOLDER_PATH + filename_result)

if __name__ == "__main__":
    
    for i in range(14, 15):
        image_path = config.IMAGE_FOLDER_PATH + str(i) + ".JPG"
        process_image(image_path)