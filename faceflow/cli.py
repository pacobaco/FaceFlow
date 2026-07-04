import sys
import cv2
from faceflow.core.engine import FaceFlowEngine
# ... import steps and workflow (reuse from examples)

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m faceflow.cli <image_path>")
        return
    # Run default workflow here
    print("FaceFlow CLI ready. Extend as needed.")

if __name__ == "__main__":
    main()
