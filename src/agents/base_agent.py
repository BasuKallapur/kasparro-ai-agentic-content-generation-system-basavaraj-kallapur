"""Base agent class for the multi-agent system."""

from abc import ABC, abstractmethod
from typing import Any, Dict, List
import logging


class BaseAgent(ABC):
    """Abstract base class for all agents in the system."""
    
    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self.logger = logging.getLogger(f"Agent.{agent_id}")
        
    @abstractmethod
    def process(self, input_data: Any) -> Any:
        """Process input data and return output."""
        pass
    
    def validate_input(self, input_data: Any, expected_type: type = None) -> bool:
        """Validate input data format."""
        if expected_type and not isinstance(input_data, expected_type):
            self.logger.error(f"Invalid input type. Expected {expected_type}, got {type(input_data)}")
            return False
        return True
    
    def log_processing(self, stage: str, details: str = ""):
        """Log processing stage."""
        self.logger.info("[%s] %s: %s", self.agent_id, stage, details)