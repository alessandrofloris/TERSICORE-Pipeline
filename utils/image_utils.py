import cv2
from config import config

def crop_image(image, box):
    '''
        Crop an image using the given bounding box.

        Args:
            image: The image to crop.
            box (tuple): Bounding box coordinates (x1, y1, x2, y2).

        Returns:
            cropped_image: Cropped image.
    '''

    # Extract box coordinates
    x1, y1, x2, y2 = tuple(box)

    # Crop the image
    cropped_image = image[y1:y2, x1:x2]
    
    return cropped_image

def show_images(images):
    '''
        Display a list of images.

        Args:
            images: A list of images to display.
    '''

    for i, img in enumerate(images):
        cv2.imshow(f"Image {i}", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def save_image(image, output_path):
    '''
        Save an image to a file.

        Args:
            image: Image to save.
            output_path (str): Path to save the image.
    '''

    cv2.imwrite(output_path, image)

def draw_and_save_image_bb(image, image_filename, clustered_boxes):

    image_bb = draw_boxes(image, clustered_boxes)

    image_filename_bb = image_filename.replace(".JPG", "_bb.JPG")
    save_image(image_bb, config.RESULTS_FOLDER_PATH + image_filename_bb)

def draw_boxes(image, boxes):
    '''
        Draw bounding boxes on an image.

        Args:
            image: Image to draw on.
            boxes: List of bounding boxes.

        Returns:
            image: Image with bounding boxes drawn.
    '''

    # Draw bounding boxes
    for box in boxes:
        x1, y1, x2, y2 = box
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

    return image