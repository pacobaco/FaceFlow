import cv2
import numpy as np
from typing import Dict, Any, List
from ..core.step import Step

try:
    from deepface import DeepFace
    HAS_DEEPFACE = True
except ImportError:
    HAS_DEEPFACE = False

class DeepFaceEmotionAnalyzer(Step):
    def __init__(self, detector_backend: str = "mediapipe"):
        self.detector_backend = detector_backend
    
    def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        image = data.get('image')
        if image is None:
            raise ValueError("No image provided")
        
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        if HAS_DEEPFACE:
            try:
                results = DeepFace.analyze(
                    img_path=rgb,
                    actions=["emotion"],
                    detector_backend=self.detector_backend,
                    enforce_detection=False
                )
                emotions = []
                for res in results:
                    emotions.append({
                        "dominant_emotion": res.get("dominant_emotion"),
                        "emotion_scores": res.get("emotion", {}),
                        "face_confidence": res.get("face_confidence", 1.0)
                    })
                data["emotions"] = emotions
                return data
            except Exception as e:
                print(f"DeepFace error: {e}. Falling back to mock.")
        
        # Fallback mock (replace with your model)
        faces = data.get("faces", [{"bbox": (0,0,100,100)}])
        data["emotions"] = [
            {
                "dominant_emotion": np.random.choice(
                    ["happy", "sad", "angry", "surprised", "neutral", "fear", "disgust"]
                ),
                "emotion_scores": {},
                "face_confidence": 0.85
            } for _ in faces
        ]
        return data
