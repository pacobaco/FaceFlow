import cv2
import mediapipe as mp
from typing import Dict, Any, List
from ..core.step import Step

class MediaPipeFaceMesh(Step):
    def __init__(self, max_num_faces: int = 10):
        self.mp_face_mesh = mp.solutions.face_mesh
        self.mesh = self.mp_face_mesh.FaceMesh(
            static_image_mode=True,
            max_num_faces=max_num_faces,
            refine_landmarks=True,
            min_detection_confidence=0.5
        )
    
    def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        image = data.get('image')
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.mesh.process(rgb)
        
        all_landmarks: List[List] = []
        if results.multi_face_landmarks:
            for face_lm in results.multi_face_landmarks:
                landmarks = [(lm.x, lm.y, lm.z) for lm in face_lm.landmark]
                all_landmarks.append(landmarks)
        data["landmarks"] = all_landmarks
        return data
