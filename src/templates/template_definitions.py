"""Template definitions for different page types."""

from typing import Dict, Any
from ..models import PageTemplate


class TemplateDefinitions:
    """Collection of template definitions for page generation."""
    
    @staticmethod
    def get_faq_template() -> PageTemplate:
        """Template for FAQ page generation."""
        structure = {
            "page_type": "faq",
            "title": "{product_name} - Frequently Asked Questions",
            "sections": {
                "overview": {
                    "total_questions": "{total_questions}",
                    "categories": "{categories}"
                },
                "questions": {
                    "by_category": "{questions_by_category}",
                    "featured": "{featured_questions}"
                }
            },
            "metadata": {
                "generated_at": "{timestamp}",
                "source": "automated_generation"
            }
        }
        
        formatting_rules = {
            "question_format": "Q: {question}\nA: {answer}",
            "category_grouping": True,
            "max_featured_questions": 5
        }
        
        return PageTemplate(
            template_type="faq",
            required_blocks=["faq"],
            structure=structure,
            formatting_rules=formatting_rules
        )
    
    @staticmethod
    def get_product_template() -> PageTemplate:
        """Template for product page generation."""
        structure = {
            "page_type": "product",
            "product_info": {
                "name": "{product_name}",
                "concentration": "{concentration}",
                "price": "{price}",
                "skin_types": "{skin_types}"
            },
            "benefits": {
                "primary_benefits": "{primary_benefits}",
                "descriptions": "{benefit_descriptions}"
            },
            "ingredients": {
                "key_ingredients": "{key_ingredients}",
                "descriptions": "{ingredient_descriptions}",
                "active_ingredients": "{active_ingredients}"
            },
            "usage": {
                "instructions": "{instructions}",
                "application_time": "{application_time}",
                "amount": "{amount}"
            },
            "safety": {
                "side_effects": "{side_effects}",
                "warnings": "{warnings}",
                "precautions": "{precautions}"
            },
            "metadata": {
                "generated_at": "{timestamp}",
                "source": "automated_generation"
            }
        }
        
        formatting_rules = {
            "price_format": "currency",
            "ingredient_list_format": "comma_separated",
            "benefit_format": "bulleted_list"
        }
        
        return PageTemplate(
            template_type="product",
            required_blocks=["benefits", "usage", "safety", "ingredients"],
            structure=structure,
            formatting_rules=formatting_rules
        )
    
    @staticmethod
    def get_comparison_template() -> PageTemplate:
        """Template for comparison page generation."""
        structure = {
            "page_type": "comparison",
            "title": "Product Comparison",
            "products": {
                "product_a": {
                    "name": "{product_a_name}",
                    "price": "{product_a_price}",
                    "concentration": "{product_a_concentration}",
                    "key_ingredients": "{product_a_ingredients}",
                    "benefits": "{product_a_benefits}",
                    "skin_types": "{product_a_skin_types}"
                },
                "product_b": {
                    "name": "{product_b_name}",
                    "price": "{product_b_price}",
                    "concentration": "{product_b_concentration}",
                    "key_ingredients": "{product_b_ingredients}",
                    "benefits": "{product_b_benefits}",
                    "skin_types": "{product_b_skin_types}"
                }
            },
            "comparison_analysis": {
                "price_comparison": "{price_difference}",
                "concentration_comparison": "{concentration_difference}",
                "shared_ingredients": "{ingredient_overlap}",
                "unique_benefits": {
                    "product_a": "{unique_benefits_a}",
                    "product_b": "{unique_benefits_b}"
                }
            },
            "recommendation": {
                "summary": "Choose based on your specific skin needs and budget",
                "factors": ["price", "concentration", "skin_type_match", "ingredient_preferences"]
            },
            "metadata": {
                "generated_at": "{timestamp}",
                "source": "automated_generation"
            }
        }
        
        formatting_rules = {
            "comparison_format": "side_by_side",
            "highlight_differences": True,
            "show_recommendations": True
        }
        
        return PageTemplate(
            template_type="comparison",
            required_blocks=["comparison"],
            structure=structure,
            formatting_rules=formatting_rules
        )