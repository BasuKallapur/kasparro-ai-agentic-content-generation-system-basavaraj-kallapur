"""Content Logic Agent - Applies transformation rules to create content blocks."""

from typing import List, Dict, Any
from .base_agent import BaseAgent
from ..models import ProductModel, Question, ContentBlock
from ..content_logic.content_blocks import ContentLogicBlocks


class ContentLogicAgent(BaseAgent):
    """Agent responsible for creating reusable content blocks."""
    
    def __init__(self):
        super().__init__("ContentLogic")
        self.content_blocks = ContentLogicBlocks()
    
    def process(self, input_data: Dict[str, Any]) -> Dict[str, ContentBlock]:
        """Generate content blocks from product data and questions."""
        self.log_processing("Starting content block generation")
        
        product = input_data.get('product')
        questions = input_data.get('questions', [])
        comparison_product = input_data.get('comparison_product')
        
        if not isinstance(product, ProductModel):
            raise ValueError("Invalid product data")
        
        content_blocks = {}
        
        # Generate core content blocks
        content_blocks['benefits'] = self.content_blocks.generate_benefits_block(product)
        content_blocks['usage'] = self.content_blocks.generate_usage_block(product)
        content_blocks['safety'] = self.content_blocks.generate_safety_block(product)
        content_blocks['ingredients'] = self.content_blocks.generate_ingredients_block(product)
        
        # Generate FAQ block if questions provided
        if questions:
            content_blocks['faq'] = self.content_blocks.generate_faq_block(questions)
        
        # Generate comparison block if comparison product provided
        if comparison_product:
            content_blocks['comparison'] = self.content_blocks.generate_comparison_block(
                product, comparison_product
            )
        
        self.log_processing("Content block generation completed", 
                          f"Generated {len(content_blocks)} blocks")
        return content_blocks