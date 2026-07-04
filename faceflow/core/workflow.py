from typing import List, Dict, Any
from .step import Step

class Workflow:
    def __init__(self, name: str):
        self.name = name
        self.steps: List[Step] = []
    
    def add_step(self, step: Step) -> 'Workflow':
        self.steps.append(step)
        return self  # chainable
    
    def run(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        data = dict(input_data)  # shallow copy
        for step in self.steps:
            print(f"[FaceFlow] Running: {step}")
            data = step.process(data)
        return data
