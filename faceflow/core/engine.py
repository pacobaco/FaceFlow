from typing import Dict, Any
from .workflow import Workflow

class FaceFlowEngine:
    def __init__(self):
        self.workflows: Dict[str, Workflow] = {}
    
    def register_workflow(self, workflow: Workflow):
        self.workflows[workflow.name] = workflow
    
    def execute(self, workflow_name: str, input_data: Dict[str, Any]) -> Dict[str, Any]:
        if workflow_name not in self.workflows:
            raise ValueError(f"Workflow '{workflow_name}' not registered")
        return self.workflows[workflow_name].run(input_data)
