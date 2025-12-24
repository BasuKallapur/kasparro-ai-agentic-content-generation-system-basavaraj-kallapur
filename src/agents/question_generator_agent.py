"""Question Generator Agent - Creates categorized user questions."""

from typing import List
from .base_agent import BaseAgent
from ..models import ProductModel, Question, QuestionCategory


class QuestionGeneratorAgent(BaseAgent):
    """Agent responsible for generating categorized questions about products."""
    
    def __init__(self):
        super().__init__("QuestionGenerator")
    
    def process(self, product: ProductModel) -> List[Question]:
        """Generate categorized questions based on product data."""
        self.log_processing("Starting question generation")
        
        if not self.validate_input(product, ProductModel):
            raise ValueError("Invalid product model")
        
        questions = []
        
        # Generate questions for each category
        questions.extend(self._generate_informational_questions(product))
        questions.extend(self._generate_safety_questions(product))
        questions.extend(self._generate_usage_questions(product))
        questions.extend(self._generate_purchase_questions(product))
        questions.extend(self._generate_comparison_questions(product))
        questions.extend(self._generate_ingredient_questions(product))
        
        self.log_processing("Question generation completed", f"Generated {len(questions)} questions")
        return questions
    
    def _generate_informational_questions(self, product: ProductModel) -> List[Question]:
        """Generate informational questions."""
        return [
            Question(
                text=f"What is {product.name}?",
                category=QuestionCategory.INFORMATIONAL,
                answer=f"{product.name} is a {product.concentration} skincare serum designed for {', '.join(product.skin_types).lower()} skin types."
            ),
            Question(
                text=f"What are the main benefits of {product.name}?",
                category=QuestionCategory.INFORMATIONAL,
                answer=f"The main benefits include {', '.join(product.benefits).lower()}."
            ),
            Question(
                text="What skin types is this product suitable for?",
                category=QuestionCategory.INFORMATIONAL,
                answer=f"This product is suitable for {', '.join(product.skin_types).lower()} skin types."
            )
        ]
    
    def _generate_safety_questions(self, product: ProductModel) -> List[Question]:
        """Generate safety-related questions."""
        return [
            Question(
                text="Are there any side effects?",
                category=QuestionCategory.SAFETY,
                answer=product.side_effects
            ),
            Question(
                text="Is this product safe for sensitive skin?",
                category=QuestionCategory.SAFETY,
                answer="Please check the side effects section. If you have sensitive skin, consider doing a patch test first."
            ),
            Question(
                text="Can I use this product during pregnancy?",
                category=QuestionCategory.SAFETY,
                answer="Please consult with your healthcare provider before using any skincare products during pregnancy."
            )
        ]
    
    def _generate_usage_questions(self, product: ProductModel) -> List[Question]:
        """Generate usage-related questions."""
        return [
            Question(
                text="How do I use this product?",
                category=QuestionCategory.USAGE,
                answer=product.usage_instructions
            ),
            Question(
                text="When should I apply this serum?",
                category=QuestionCategory.USAGE,
                answer="Based on the instructions, this should be applied in the morning before sunscreen."
            ),
            Question(
                text="How much product should I use?",
                category=QuestionCategory.USAGE,
                answer="Use 2-3 drops as recommended in the usage instructions."
            )
        ]
    
    def _generate_purchase_questions(self, product: ProductModel) -> List[Question]:
        """Generate purchase-related questions."""
        return [
            Question(
                text="What is the price of this product?",
                category=QuestionCategory.PURCHASE,
                answer=f"The price is {product.price}."
            ),
            Question(
                text="Is this product worth the price?",
                category=QuestionCategory.PURCHASE,
                answer=f"At {product.price}, this product offers {', '.join(product.benefits).lower()} with {product.concentration} active ingredient."
            )
        ]
    
    def _generate_comparison_questions(self, product: ProductModel) -> List[Question]:
        """Generate comparison-related questions."""
        return [
            Question(
                text="How does this compare to other vitamin C serums?",
                category=QuestionCategory.COMPARISON,
                answer=f"This serum contains {product.concentration} and is specifically formulated for {', '.join(product.skin_types).lower()} skin types."
            ),
            Question(
                text="What makes this product unique?",
                category=QuestionCategory.COMPARISON,
                answer=f"The combination of {', '.join(product.key_ingredients)} makes this product effective for {', '.join(product.benefits).lower()}."
            )
        ]
    
    def _generate_ingredient_questions(self, product: ProductModel) -> List[Question]:
        """Generate ingredient-related questions."""
        return [
            Question(
                text="What are the key ingredients?",
                category=QuestionCategory.INGREDIENTS,
                answer=f"The key ingredients are {', '.join(product.key_ingredients)}."
            ),
            Question(
                text="What does Vitamin C do for the skin?",
                category=QuestionCategory.INGREDIENTS,
                answer="Vitamin C is known for its brightening properties and ability to fade dark spots."
            )
        ]