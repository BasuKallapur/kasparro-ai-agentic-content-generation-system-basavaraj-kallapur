# Project Documentation

## Problem Statement

Design and implement a modular agentic automation system that takes product data and automatically generates structured, machine-readable content pages. The system must demonstrate multi-agent workflows, automation graphs, reusable content logic, template-based generation, and structured JSON output.

## Solution Overview

The solution implements a multi-agent architecture where each agent has a single responsibility and clear input/output boundaries. The system processes product data through a pipeline of specialized agents to generate FAQ, product description, and comparison pages in JSON format.

## Scopes & Assumptions

### Scope

- Process single product dataset (GlowBoost Vitamin C Serum)
- Generate 3 types of content pages: FAQ, Product Description, Comparison
- Output machine-readable JSON format
- Demonstrate agent orchestration and modular design

### Assumptions

- No external data sources or research allowed
- System must work with similar product data structures
- Fictional comparison product can be generated based on domain patterns
- Content quality focuses on structure and logic, not marketing copy

## System Design

### Architecture Overview

The system follows a pipeline architecture with the following agents:

```
Raw Product Data → Data Parser Agent → Structured Product Model
                                    ↓
Question Categories ← Question Generator Agent ← Product Model
                                    ↓
Content Blocks ← Content Logic Agent ← Product Model + Questions
                                    ↓
JSON Pages ← Template Engine Agent ← Content Blocks + Templates
                                    ↓
Final Output ← Orchestrator Agent (coordinates entire flow)
```

### Agent Responsibilities

1. **Data Parser Agent**

   - Input: Raw product JSON data
   - Output: Structured ProductModel object
   - Responsibility: Data validation and normalization

2. **Question Generator Agent**

   - Input: ProductModel
   - Output: Categorized questions list
   - Responsibility: Generate 15+ questions across categories (Informational, Safety, Usage, Purchase, Comparison)

3. **Content Logic Agent**

   - Input: ProductModel + Questions
   - Output: Content blocks (benefits, usage, safety, etc.)
   - Responsibility: Apply transformation rules to create reusable content components

4. **Template Engine Agent**

   - Input: Content blocks + Template definitions
   - Output: Structured page data
   - Responsibility: Assemble content using predefined templates

5. **Orchestrator Agent**
   - Input: Configuration and raw data
   - Output: Final JSON files
   - Responsibility: Coordinate agent execution and manage data flow

### Data Flow

1. **Input Processing**: Raw product data is parsed into a structured model
2. **Question Generation**: System generates categorized questions based on product attributes
3. **Content Block Creation**: Reusable logic blocks transform data into content components
4. **Template Assembly**: Templates combine content blocks into structured pages
5. **Output Generation**: Final JSON files are written to output directory

### Template System

Templates define the structure and rules for each page type:

- **FAQ Template**: Question-answer pairs with categorization
- **Product Template**: Comprehensive product information layout
- **Comparison Template**: Side-by-side product comparison structure

### Content Logic Blocks

Reusable functions that apply specific transformation rules:

- `generate_benefits_block()`: Extracts and formats product benefits
- `generate_usage_block()`: Creates usage instructions
- `generate_safety_block()`: Processes side effects and warnings
- `generate_ingredients_block()`: Formats ingredient information
- `generate_comparison_block()`: Creates comparative analysis

### Extensibility

The modular design allows for:

- Adding new agent types
- Extending template definitions
- Creating new content logic blocks
- Supporting additional product data formats
- Scaling to multiple products
