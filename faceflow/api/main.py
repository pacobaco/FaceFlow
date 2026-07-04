from fastapi import FastAPI, UploadFile, File
import cv2
import numpy as np
from faceflow.core.engine import FaceFlowEngine
# ... import workflows and steps, register defaults

app = FastAPI(title="FaceFlow API")

@app.post("/analyze")
async def analyze(file: UploadFile = File(...), workflow: str = "basic_emotion"):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    result = engine.execute(workflow, {"image": img})
    return result
