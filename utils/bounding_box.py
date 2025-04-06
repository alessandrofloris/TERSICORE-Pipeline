import cv2
from config.config import PADDING_BB_X, PADDING_BB_Y

def padding_box_function(box, image):
    '''
        Maps a bounding box to a new box with padding.

        Args: 
            box: Bounding box coordinates (x1, y1, x2, y2).
            image: Image containing the bounding box.

        Returns:
            A new bounding box with a padding.
    '''

    x1, y1, x2, y2 = map(int, box) # Extract coordinates
        
    # Calculate padding
    width = x2 - x1 # Width of the box
    height = y2 - y1 # Height of the box
    x_padding = int(width * PADDING_BB_X)
    y_padding = int(height * PADDING_BB_Y)

    # Apply padding
    x1 = max(0, x1 - x_padding)
    y1 = max(0, y1 - y_padding)
    x2 = min(image.shape[1], x2 + x_padding)  # Fits to image width
    y2 = min(image.shape[0], y2 + y_padding)  # Fits to image height

    return (x1, y1, x2, y2)

def padding_bounding_boxes(boxes, image):
    """
        Maps each box to a new box with a padding.

        Args:
            boxes: List of bounding boxes.
            image: Image containing the bounding boxes. 

        Returns:
            A new list of boxes with a padding.
    """

    return [padding_box_function(box, image) for box in boxes]