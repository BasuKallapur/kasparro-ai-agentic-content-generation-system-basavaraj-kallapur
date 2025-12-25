# Kasparro AI Agentic Content Generation System

A modular multi-agent system for automated content generation from product data, designed to demonstrate production-style agentic workflows, automation graphs, and template-based content generation.

## Quick Start

```bash
python main.py
```

This will process the GlowBoost Vitamin C Serum data and generate:

- `output/faq.json` - FAQ page with 15+ categorized questions
- `output/product_page.json` - Complete product description page
- `output/comparison_page.json` - Product comparison with fictional competitor

## System Architecture

### Multi-Agent Pipeline Flow

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Raw Product   │───▶│  Data Parser     │───▶│ Structured      │
│   Data (JSON)   │    │  Agent           │    │ Product Model   │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                                         │
                                                         ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ 15+ Categorized │◀───│  Question        │◀───│ Product Model   │
│ Questions       │    │  Generator Agent │    │                 │
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │                                               │
         ▼                                               ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Content Blocks  │◀───│  Content Logic   │◀───│ Questions +     │
│ (Reusable)      │    │  Agent           │    │ Product Data    │
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │
         ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Final JSON      │◀───│  Template Engine │◀───│ Content Blocks  │
│ Pages (3)       │    │  Agent           │    │ + Templates     │
└─────────────────┘    └──────────────────┘    └─────────────────┘
         ▲
         │
┌─────────────────┐
│  Orchestrator   │
│  Agent          │
│ (Coordinates    │
│  All Agents)    │
└─────────────────┘
```

### Agent Responsibilities

| Agent                  | Input                      | Output                       | Responsibility                      |
| ---------------------- | -------------------------- | ---------------------------- | ----------------------------------- |
| **Data Parser**        | Raw JSON data              | ProductModel                 | Data validation & normalization     |
| **Question Generator** | ProductModel               | 15+ Questions (6 categories) | Generate categorized user questions |
| **Content Logic**      | ProductModel + Questions   | Content Blocks               | Apply transformation rules          |
| **Template Engine**    | Content Blocks + Templates | Structured Pages             | Assemble final content              |
| **Orchestrator**       | Configuration              | JSON Files                   | Coordinate entire workflow          |

### Content Logic Blocks (Reusable Components)

- `generate_benefits_block()` - Extracts and formats product benefits
- `generate_usage_block()` - Creates usage instructions
- `generate_safety_block()` - Processes side effects and warnings
- `generate_ingredients_block()` - Formats ingredient information
- `generate_comparison_block()` - Creates comparative analysis
- `generate_faq_block()` - Structures Q&A content

### Template System

```
Templates Define:
├── Structure (JSON schema)
├── Required Content Blocks
├── Formatting Rules
└── Field Mappings

Available Templates:
├── FAQ Template
├── Product Template
└── Comparison Template
```

## System Features

### Multi-Agent Workflow

- Clear agent boundaries with single responsibilities
- No hidden global state
- Defined input/output contracts

### Automation Graph

- Pipeline orchestration through OrchestratorAgent
- Sequential processing with data flow validation
- Error handling and logging at each stage

### Reusable Content Logic

- Modular content transformation functions
- Composable content blocks
- Template-agnostic content generation

### Machine-Readable Output

- Clean JSON structure for all pages
- Metadata inclusion for traceability
- Consistent formatting across outputs

## Configuration

System behavior is controlled via `config.json`:

```json
{
  "agents": {
    "question_generator": {
      "min_questions_per_category": 2,
      "categories": [
        "informational",
        "safety",
        "usage",
        "purchase",
        "comparison",
        "ingredients"
      ]
    }
  }
}
```

## Testing

```bash
python test_system.py
```

Validates:

- Complete pipeline execution
- Required file generation
- JSON structure correctness
- Content block integration

## Project Structure

```
├── main.py                     # Entry point
├── config.json                 # System configuration
├── src/
│   ├── models.py              # Data models
│   ├── agents/                # Agent implementations
│   │   ├── base_agent.py      # Abstract base class
│   │   ├── orchestrator_agent.py
│   │   ├── data_parser_agent.py
│   │   ├── question_generator_agent.py
│   │   ├── content_logic_agent.py
│   │   └── template_engine_agent.py
│   ├── content_logic/         # Reusable content blocks
│   │   └── content_blocks.py
│   └── templates/             # Template definitions
│       └── template_definitions.py
├── output/                    # Generated JSON files
├── logs/                      # System logs
└── docs/                      # Detailed documentation
    └── projectdocumentation.md
```

## Design Principles

1. **Modularity**: Each agent has a single, well-defined responsibility
2. **Extensibility**: Easy to add new agents, templates, or content types
3. **Reusability**: Content logic blocks work across different templates
4. **Composability**: Templates can combine multiple content blocks
5. **Maintainability**: Clear separation of concerns and logging

## Extensibility Examples

### Adding New Agent

```python
class NewAgent(BaseAgent):
    def process(self, input_data):
        # Implementation
        return output_data
```

### Adding New Template

```python
def get_new_template():
    return PageTemplate(
        template_type="new_type",
        required_blocks=["block1", "block2"],
        structure={...}
    )
```

### Adding New Content Block

```python
@staticmethod
def generate_new_block(product):
    return ContentBlock(
        block_type="new_block",
        content={...}
    )
```

## Requirements Met

- Multi-agent workflows with clear boundaries
- Automation graphs and orchestration
- Reusable content logic blocks
- Template-based generation system
- Structured JSON output (machine-readable)
- System abstraction and documentation
- 15+ categorized questions generation
- 3 required page types (FAQ, Product, Comparison)
- No external dependencies (Python stdlib only)

## Documentation

See `docs/projectdocumentation.md` for comprehensive system design, architecture details, and implementation decisions.
