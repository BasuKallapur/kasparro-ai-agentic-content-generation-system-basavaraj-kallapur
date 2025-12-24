"""Data Parser Agent - Converts raw product data into structured model."""

from typing import Dict, Any
from .base_agent import BaseAgent
from ..models import ProductModel


class DataParserAgent(BaseAgent):
    """Agent responsible for parsing and validating raw product data."""
    
    def __init__(self):
        super().__init__("DataParser")
    
    def process(self, raw_data: Dict[str, Any]) -> ProductModel:
        """Convert raw product data into structured ProductModel."""
        self.log_processing("Starting data parsing")
        
        if not self.validate_input(raw_data, dict):
            raise ValueError("Invalid input data format")
        
        # Normalize field names to match expected format
        normalized_data = self._normalize_field_names(raw_data)
        
        # Validate required fields
        self._validate_required_fields(normalized_data)
        
        # Create structured model
        product_model = ProductModel.from_raw_data(normalized_data)
        
        self.log_processing("Data parsing completed", f"Product: {product_model.name}")
        return product_model
    
    def _normalize_field_names(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        """Normalize field names to standard format."""
        field_mapping = {
            'Product Name': 'name',
            'product_name': 'name',
            'Concentration': 'concentration',
            'Skin Type': 'skin_type',
            'skin_type': 'skin_type',
            'Key Ingredients': 'key_ingredients',
            'key_ingredients': 'key_ingredients',
            'Benefits': 'benefits',
            'How to Use': 'usage_instructions',
            'usage_instructions': 'usage_instructions',
            'Side Effects': 'side_effects',
            'side_effects': 'side_effects',
            'Price': 'price'
        }
        
        normalized = {}
        for key, value in raw_data.items():
            normalized_key = field_mapping.get(key, key.lower().replace(' ', '_'))
            normalized[normalized_key] = value
            
        return normalized
    
    def _validate_required_fields(self, data: Dict[str, Any]) -> None:
        """Validate that all required fields are present."""
        required_fields = ['name', 'concentration', 'skin_type', 'key_ingredients', 
                          'benefits', 'usage_instructions', 'side_effects', 'price']
        
        missing_fields = [field for field in required_fields if field not in data]
        
        if missing_fields:
            raise ValueError(f"Missing required fields: {missing_fields}")