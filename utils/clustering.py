from shapely.geometry import box

def boxes_intersect(box1, box2):
    """
        Check if two bounding boxes intersect.
        
        Args:
            box1: First bounding box.
            box2: Second bounding box.
        
        Returns:
            True if boxes intersect, False otherwise.
    """
    x1_1, y1_1, x2_1, y2_1 = box1
    x1_2, y1_2, x2_2, y2_2 = box2
    return not (x2_1 < x1_2 or x2_2 < x1_1 or y2_1 < y1_2 or y2_2 < y1_1)

def merge_boxes(box1, box2):
    """
        Merge two bounding boxes into one.
        
        Args:
            box1: First bounding box.
            box2: Second bounding box.
        
        Returns:
            Merged bounding box.
    """
    x1 = min(box1[0], box2[0])
    y1 = min(box1[1], box2[1])
    x2 = max(box1[2], box2[2])
    y2 = max(box1[3], box2[3])
    return (x1, y1, x2, y2)

def cluster_boxes(boxes):
    """
        Cluster bounding boxes that intersect.
        
        Args:
            boxes: List of bounding boxes.
        
        Returns:
            List of merged bounding boxes.
    """
    merged = True
    while merged:
        merged = False
        new_boxes = []
        used = set()
        
        for i in range(len(boxes)):
            if i in used:
                continue
            current_box = boxes[i]
            
            for j in range(i + 1, len(boxes)):
                if j in used:
                    continue
                if boxes_intersect(current_box, boxes[j]):
                    current_box = merge_boxes(current_box, boxes[j])
                    used.add(j)
                    merged = True
            
            new_boxes.append(current_box)
            used.add(i)
        
        boxes = new_boxes
    
    return boxes