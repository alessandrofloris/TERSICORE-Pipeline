import detectron2
from detectron2.utils.logger import setup_logger
setup_logger()
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg

def detect_people(image):
    '''
        Detect people in an image using faster-rcnn.

        Args:
            image: Image to process.

        Returns: 
            List of bounding boxes.
    '''

    cfg = get_cfg()
    cfg.merge_from_file(model_zoo.get_config_file("COCO-Detection/faster_rcnn_X_101_32x8d_FPN_3x.yaml"))
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5  
    cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-Detection/faster_rcnn_X_101_32x8d_FPN_3x.yaml")
    predictor = DefaultPredictor(cfg)

    try:

        outputs = predictor(image)    

        instances = outputs["instances"] 
        person_indices = instances.pred_classes == 0  # Get indices of detected people (class 0 in COCO dataset)

        person_instances = instances[person_indices]

        pred_boxes = person_instances.pred_boxes.tensor.cpu().numpy()

        return pred_boxes

    except Exception as e:
        
        print(f"Error processing image in the function 'fastrcnn.detect_people': {e}")