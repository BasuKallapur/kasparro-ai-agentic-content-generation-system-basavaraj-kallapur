# Kasparro AI Agentic Content Generation System

A modular multi-agent system for automated content generation from product data.

## Quick Start

```bash
python main.py
```

This will process the GlowBoost Vitamin C Serum data and generate:

- `output/faq.json`
- `output/product_page.json`
- `output/comparison_page.json`

## Architecture

The system uses a multi-agent architecture with clear separation of concerns:

1. **Data Parser Agent** - Converts raw product data into structured internal model
2. **Question Generator Agent** - Creates categorized user questions
3. **Content Logic Agent** - Applies transformation rules to generate content blocks
4. **Template Engine Agent** - Assembles content using predefined templates
5. **Orchestrator Agent** - Coordinates the entire workflow

## Documentation

See `docs/projectdocumentation.md` for detailed system design and architecture.
