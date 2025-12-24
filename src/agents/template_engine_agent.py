"""Template Engine Agent - Assembles content using predefined templates."""

from typing import Dict, Any
import json
from datetime import datetime
from .base_agent import BaseAgent
from ..models import ContentBlock, PageTemplate, GeneratedPage, ProductModel
from ..templates.template_definitions import TemplateDefinitions


class TemplateEngineAgent(BaseAgent):
    """Agent responsible for assembling content using templates."""
    
    def __init__(self):
        super().__init__("TemplateEngine")
        self.templates = TemplateDefinitions()
    
    def process(self, input_data: Dict[str, Any]) -> Dict[str, GeneratedPage]:
        """Generate pages using templates and content blocks."""
        self.log_processing("Starting template-based page generation")
        
        content_blocks = input_data.get('content_blocks', {})
        product = input_data.get('product')
        comparison_product = input_data.get('comparison_product')
        
        if not isinstance(content_blocks, dict):
            raise ValueError("Invalid content blocks data")
        
        generated_pages = {}
        
        # Generate FAQ page
        if 'faq' in content_blocks:
            generated_pages['faq'] = self._generate_faq_page(
                content_blocks['faq'], product
            )
        
        # Generate product page
        generated_pages['product'] = self._generate_product_page(
            content_blocks, product
        )
        
        # Generate comparison page
        if 'comparison' in content_blocks:
            generated_pages['comparison'] = self._generate_comparison_page(
                content_blocks['comparison'], product, comparison_product
            )
        
        self.log_processing("Page generation completed", 
                          f"Generated {len(generated_pages)} pages")
        return generated_pages
    
    def _generate_faq_page(self, faq_block: ContentBlock, product: ProductModel) -> GeneratedPage:
        """Generate FAQ page using template."""
        template = self.templates.get_faq_template()
        
        # Extract data from content block
        faq_content = faq_block.content
        
        # Populate template
        page_content = {
            "title": f"{product.name} - Frequently Asked Questions",
            "sections": {
                "overview": {
                    "total_questions": faq_content["total_questions"],
                    "categories": faq_content["categories"]
                },
                "questions": {
                    "by_category": faq_content["questions_by_category"],
                    "featured": faq_content["featured_questions"]
                }
            },
            "metadata": {
                "generated_at": datetime.now().isoformat(),
                "source": "automated_generation"
            }
        }
        
        return GeneratedPage(
            page_type="faq",
            content=page_content,
            metadata={"template_used": "faq_template"}
        )
    
    def _generate_product_page(self, content_blocks: Dict[str, ContentBlock], 
                             product: ProductModel) -> GeneratedPage:
        """Generate product page using template."""
        template = self.templates.get_product_template()
        
        # Extract data from content blocks
        benefits_content = content_blocks.get('benefits', ContentBlock("benefits", {})).content
        usage_content = content_blocks.get('usage', ContentBlock("usage", {})).content
        safety_content = content_blocks.get('safety', ContentBlock("safety", {})).content
        ingredients_content = content_blocks.get('ingredients', ContentBlock("ingredients", {})).content
        
        # Populate template
        page_content = {
            "product_info": {
                "name": product.name,
                "concentration": product.concentration,
                "price": product.price,
                "skin_types": product.skin_types
            },
            "benefits": {
                "primary_benefits": benefits_content.get("primary_benefits", []),
                "descriptions": benefits_content.get("benefit_descriptions", {})
            },
            "ingredients": {
                "key_ingredients": ingredients_content.get("key_ingredients", []),
                "descriptions": ingredients_content.get("ingredient_descriptions", {}),
                "active_ingredients": ingredients_content.get("active_ingredients", [])
            },
            "usage": {
                "instructions": usage_content.get("instructions", ""),
                "application_time": usage_content.get("application_time", ""),
                "amount": usage_content.get("amount", "")
            },
            "safety": {
                "side_effects": safety_content.get("side_effects", ""),
                "warnings": safety_content.get("warnings", []),
                "precautions": safety_content.get("precautions", [])
            },
            "metadata": {
                "generated_at": datetime.now().isoformat(),
                "source": "automated_generation"
            }
        }
        
        return GeneratedPage(
            page_type="product",
            content=page_content,
            metadata={"template_used": "product_template"}
        )
    
    def _generate_comparison_page(self, comparison_block: ContentBlock, 
                                product_a: ProductModel, product_b: ProductModel) -> GeneratedPage:
        """Generate comparison page using template."""
        template = self.templates.get_comparison_template()
        
        # Extract data from content block
        comparison_content = comparison_block.content
        
        # Populate template
        page_content = {
            "title": "Product Comparison",
            "products": comparison_content["products"],
            "comparison_analysis": comparison_content["comparison_points"],
            "recommendation": {
                "summary": "Choose based on your specific skin needs and budget",
                "factors": ["price", "concentration", "skin_type_match", "ingredient_preferences"]
            },
            "metadata": {
                "generated_at": datetime.now().isoformat(),
                "source": "automated_generation",
                "note": "Product B is a fictional comparator created to demonstrate comparison logic"
            }
        }
        
        return GeneratedPage(
            page_type="comparison",
            content=page_content,
            metadata={"template_used": "comparison_template"}
        )