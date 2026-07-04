import cv2
from faceflow.core.engine import FaceFlowEngine
from faceflow.core.workflow import Workflow
from faceflow.steps.loader import LoadImageStep
from faceflow.steps.detection import MediaPipeFaceDetector
from faceflow.steps.emotion import DeepFaceEmotionAnalyzer

engine = FaceFlowEngine()

wf = (Workflow("basic_emotion")
      .add_step(LoadImageStep())
      .add_step(MediaPipeFaceDetector())
      .add_step(DeepFaceEmotionAnalyzer(detector_backend="mediapipe")))

engine.register_workflow(wf)

image = cv2.imread("face.jpg")  # or use image_path
result = engine.execute("basic_emotion", {"image": image})
print(result["emotions"])
