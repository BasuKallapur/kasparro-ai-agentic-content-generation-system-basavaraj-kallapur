"""Orchestrator Agent - Coordinates the entire multi-agent workflow."""

import json
import os
from typing import Dict, Any
from datetime import datetime
from .base_agent import BaseAgent
from .data_parser_agent import DataParserAgent
from .question_generator_agent import QuestionGeneratorAgent
from .content_logic_agent import ContentLogicAgent
from .template_engine_agent import TemplateEngineAgent
from ..models import ProductModel


class OrchestratorAgent(BaseAgent):
    """Main orchestrator that coordinates all agents in the pipeline."""
    
    def __init__(self):
        super().__init__("Orchestrator")
        
        # Initialize all agents
        self.data_parser = DataParserAgent()
        self.question_generator = QuestionGeneratorAgent()
        self.content_logic = ContentLogicAgent()
        self.template_engine = TemplateEngineAgent()
    
    def process(self, input_data: Dict[str, Any]) -> Dict[str, str]:
        """Execute the complete multi-agent pipeline."""
        self.log_processing("Starting multi-agent pipeline")
        
        # Step 1: Parse raw product data
        product = self.data_parser.process(input_data['product_data'])
        
        # Step 2: Generate comparison product (fictional)
        comparison_product = self._create_fictional_comparison_product()
        
        # Step 3: Generate questions
        questions = self.question_generator.process(product)
        
        # Step 4: Generate content blocks
        content_input = {
            'product': product,
            'questions': questions,
            'comparison_product': comparison_product
        }
        content_blocks = self.content_logic.process(content_input)
        
        # Step 5: Generate pages using templates
        template_input = {
            'content_blocks': content_blocks,
            'product': product,
            'comparison_product': comparison_product
        }
        generated_pages = self.template_engine.process(template_input)
        
        # Step 6: Write output files
        output_files = self._write_output_files(generated_pages)
        
        self.log_processing("Pipeline completed successfully")
        return output_files
    
    def _create_fictional_comparison_product(self) -> ProductModel:
        """Create a fictional comparison product."""
        fictional_data = {
            'name': 'RadiantGlow Vitamin C Serum',
            'concentration': '15% Vitamin C',
            'skin_type': 'All skin types, Sensitive',
            'key_ingredients': 'Vitamin C, Niacinamide, Vitamin E',
            'benefits': 'Anti-aging, Brightening, Hydrating',
            'usage_instructions': 'Apply 3-4 drops in the evening after cleansing',
            'side_effects': 'Rare allergic reactions in very sensitive individuals',
            'price': '₹899'
        }
        
        return ProductModel.from_raw_data(fictional_data)
    
    def _write_output_files(self, generated_pages: Dict[str, Any]) -> Dict[str, str]:
        """Write generated pages to JSON files."""
        # Create output directory if it doesn't exist
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)
        
        output_files = {}
        
        # Map page types to required filenames
        filename_mapping = {
            'faq': 'faq.json',
            'product': 'product_page.json',
            'comparison': 'comparison_page.json'
        }
        
        for page_type, page in generated_pages.items():
            filename = filename_mapping.get(page_type, f"{page_type}.json")
            filepath = os.path.join(output_dir, filename)
            
            # Convert GeneratedPage to dict for JSON serialization
            page_data = {
                "page_type": page.page_type,
                "content": page.content,
                "metadata": page.metadata
            }
            
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(page_data, f, indent=2, ensure_ascii=False)
            
            output_files[page_type] = filepath
            self.log_processing(f"Written {page_type} page", filepath)
        
        return output_files