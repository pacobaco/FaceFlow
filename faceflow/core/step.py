from abc import ABC, abstractmethod
from typing import Any, Dict

class Step(ABC):
    """Base class for all workflow steps."""
    
    @abstractmethod
    def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Process and return updated data dict."""
        pass
    
    def __repr__(self) -> str:
        return self.__class__.__name__
