import cv2
import numpy as np
from typing import Dict, Any
from ..core.step import Step

class LoadImageStep(Step):
    def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if 'image' in data:
            return data
        if 'image_path' in data:
            img = cv2.imread(data['image_path'])
            if img is None:
                raise FileNotFoundError(f"Could not load {data['image_path']}")
            data['image'] = img
        return data
