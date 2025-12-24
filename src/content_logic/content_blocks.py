"""Reusable content logic blocks for transforming data into content components."""

from typing import Dict, Any, List
from ..models import ProductModel, Question, ContentBlock


class ContentLogicBlocks:
    """Collection of reusable content transformation functions."""
    
    @staticmethod
    def generate_benefits_block(product: ProductModel) -> ContentBlock:
        """Generate benefits content block."""
        # Fix grammar for benefits
        polished_benefits = []
        polished_descriptions = {}
        
        for benefit in product.benefits:
            if 'fades' in benefit.lower():
                polished = benefit.replace('Fades', 'Fading').replace('fades', 'fading')
                polished_benefits.append(polished)
                polished_descriptions[benefit] = polished
            else:
                polished_benefits.append(benefit)
                polished_descriptions[benefit] = benefit
        
        content = {
            "primary_benefits": polished_benefits,
            "benefit_descriptions": polished_descriptions,
            "skin_type_benefits": {
                skin_type: f"Formulated for {skin_type.lower()} skin"
                for skin_type in product.skin_types
            }
        }
        
        return ContentBlock(
            block_type="benefits",
            content=content,
            dependencies=["product_data"]
        )
    
    @staticmethod
    def generate_usage_block(product: ProductModel) -> ContentBlock:
        """Generate usage instructions content block."""
        content = {
            "instructions": product.usage_instructions,
            "application_time": "morning" if "morning" in product.usage_instructions.lower() else "as directed",
            "amount": "2-3 drops" if "2-3 drops" in product.usage_instructions else "as directed",
            "additional_notes": "Apply before sunscreen" if "sunscreen" in product.usage_instructions.lower() else ""
        }
        
        return ContentBlock(
            block_type="usage",
            content=content,
            dependencies=["product_data"]
        )
    
    @staticmethod
    def generate_safety_block(product: ProductModel) -> ContentBlock:
        """Generate safety information content block."""
        content = {
            "side_effects": product.side_effects,
            "warnings": [],
            "precautions": ["Patch test recommended for sensitive skin"],
            "contraindications": ["Consult healthcare provider if pregnant or nursing"]
        }
        
        # Add specific warnings based on side effects
        if "tingling" in product.side_effects.lower():
            content["warnings"].append("May cause mild tingling sensation")
        
        return ContentBlock(
            block_type="safety",
            content=content,
            dependencies=["product_data"]
        )
    
    @staticmethod
    def generate_ingredients_block(product: ProductModel) -> ContentBlock:
        """Generate ingredients information content block."""
        # Only use benefits that are actually stated in the product data
        ingredient_descriptions = {}
        for ingredient in product.key_ingredients:
            if ingredient == "Vitamin C" and any("brightening" in benefit.lower() or "dark spots" in benefit.lower() for benefit in product.benefits):
                ingredient_descriptions[ingredient] = "Associated with brightening and fading dark spots as stated in product benefits"
            elif ingredient == "Hyaluronic Acid":
                ingredient_descriptions[ingredient] = "Hydrating ingredient"
            else:
                ingredient_descriptions[ingredient] = f"{ingredient} - ingredient in this formulation"
        
        content = {
            "key_ingredients": product.key_ingredients,
            "ingredient_descriptions": ingredient_descriptions,
            "concentration": product.concentration,
            "active_ingredients": [ing for ing in product.key_ingredients if "Vitamin" in ing or "Acid" in ing]
        }
        
        return ContentBlock(
            block_type="ingredients",
            content=content,
            dependencies=["product_data"]
        )
    
    @staticmethod
    def generate_comparison_block(product_a: ProductModel, product_b: ProductModel) -> ContentBlock:
        """Generate comparison content block between two products."""
        content = {
            "products": {
                "product_a": {
                    "name": product_a.name,
                    "price": product_a.price,
                    "concentration": product_a.concentration,
                    "key_ingredients": product_a.key_ingredients,
                    "benefits": product_a.benefits,
                    "skin_types": product_a.skin_types
                },
                "product_b": {
                    "name": product_b.name,
                    "price": product_b.price,
                    "concentration": product_b.concentration,
                    "key_ingredients": product_b.key_ingredients,
                    "benefits": product_b.benefits,
                    "skin_types": product_b.skin_types
                }
            },
            "comparison_points": {
                "price_difference": f"{product_a.price} vs {product_b.price}",
                "concentration_difference": f"{product_a.concentration} vs {product_b.concentration}",
                "ingredient_overlap": list(set(product_a.key_ingredients) & set(product_b.key_ingredients)),
                "unique_benefits_a": list(set(product_a.benefits) - set(product_b.benefits)),
                "unique_benefits_b": list(set(product_b.benefits) - set(product_a.benefits))
            }
        }
        
        return ContentBlock(
            block_type="comparison",
            content=content,
            dependencies=["product_a_data", "product_b_data"]
        )
    
    @staticmethod
    def generate_faq_block(questions: List[Question]) -> ContentBlock:
        """Generate FAQ content block from questions."""
        # Group questions by category
        categorized_questions = {}
        for question in questions:
            category = question.category.value
            if category not in categorized_questions:
                categorized_questions[category] = []
            categorized_questions[category].append({
                "question": question.text,
                "answer": question.answer
            })
        
        content = {
            "total_questions": len(questions),
            "categories": list(categorized_questions.keys()),
            "questions_by_category": categorized_questions,
            "featured_questions": [
                {"question": q.text, "answer": q.answer} 
                for q in questions[:5]  # Top 5 questions
            ]
        }
        
        return ContentBlock(
            block_type="faq",
            content=content,
            dependencies=["questions_data"]
        )