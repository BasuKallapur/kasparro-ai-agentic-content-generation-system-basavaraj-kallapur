"""Data models for the content generation system."""

from dataclasses import dataclass
from typing import List, Dict, Any, Optional
from enum import Enum


class QuestionCategory(Enum):
    INFORMATIONAL = "informational"
    SAFETY = "safety"
    USAGE = "usage"
    PURCHASE = "purchase"
    COMPARISON = "comparison"
    INGREDIENTS = "ingredients"


@dataclass
class ProductModel:
    """Structured product data model."""
    name: str
    concentration: str
    skin_types: List[str]
    key_ingredients: List[str]
    benefits: List[str]
    usage_instructions: str
    side_effects: str
    price: str
    
    @classmethod
    def from_raw_data(cls, raw_data: Dict[str, Any]) -> 'ProductModel':
        """Create ProductModel from raw input data."""
        return cls(
            name=raw_data.get('name', ''),
            concentration=raw_data.get('concentration', ''),
            skin_types=[s.strip() for s in raw_data.get('skin_type', '').split(',')],
            key_ingredients=[i.strip() for i in raw_data.get('key_ingredients', '').split(',')],
            benefits=[b.strip() for b in raw_data.get('benefits', '').split(',')],
            usage_instructions=raw_data.get('usage_instructions', ''),
            side_effects=raw_data.get('side_effects', ''),
            price=raw_data.get('price', '')
        )


@dataclass
class Question:
    """Represents a generated question with category."""
    text: str
    category: QuestionCategory
    answer: str = ""


@dataclass
class ContentBlock:
    """Reusable content component."""
    block_type: str
    content: Dict[str, Any]
    dependencies: List[str] = None
    
    def __post_init__(self):
        if self.dependencies is None:
            self.dependencies = []


@dataclass
class PageTemplate:
    """Template definition for page generation."""
    template_type: str
    required_blocks: List[str]
    structure: Dict[str, Any]
    formatting_rules: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.formatting_rules is None:
            self.formatting_rules = {}


@dataclass
class GeneratedPage:
    """Final generated page output."""
    page_type: str
    content: Dict[str, Any]
    metadata: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}