import cv2
import mediapipe as mp
from typing import Dict, Any, List
from ..core.step import Step

class MediaPipeFaceDetector(Step):
    def __init__(self, min_detection_confidence: float = 0.5):
        self.mp_face_detection = mp.solutions.face_detection
        self.detector = self.mp_face_detection.FaceDetection(
            min_detection_confidence=min_detection_confidence
        )
    
    def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        image = data.get('image')
        if image is None:
            raise ValueError("No image in data")
        
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.detector.process(rgb)
        
        faces: List[Dict] = []
        if results.detections:
            h, w = image.shape[:2]
            for det in results.detections:
                bbox = det.location_data.relative_bounding_box
                x, y = int(bbox.xmin * w), int(bbox.ymin * h)
                w_box, h_box = int(bbox.width * w), int(bbox.height * h)
                faces.append({
                    "bbox": (x, y, w_box, h_box),
                    "confidence": float(det.score[0])
                })
        data["faces"] = faces
        data["num_faces"] = len(faces)
        return data
