"""Main entry point for the multi-agent content generation system."""

import logging
import json
from src.agents.orchestrator_agent import OrchestratorAgent


def setup_logging():
    """Configure logging for the application."""
    import os
    
    # Create logs directory if it doesn't exist
    logs_dir = "logs"
    os.makedirs(logs_dir, exist_ok=True)
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(os.path.join(logs_dir, 'system.log')),
            logging.StreamHandler()
        ]
    )


def load_product_data():
    """Load the GlowBoost product data."""
    return {
        'Product Name': 'GlowBoost Vitamin C Serum',
        'Concentration': '10% Vitamin C',
        'Skin Type': 'Oily, Combination',
        'Key Ingredients': 'Vitamin C, Hyaluronic Acid',
        'Benefits': 'Brightening, Fades dark spots',
        'How to Use': 'Apply 2–3 drops in the morning before sunscreen',
        # 'Side Effects': 'Mild tingling for sensitive skin',
        'Price': '₹699'
    }


def main():
    """Main execution function."""
    # Setup logging
    setup_logging()
    logger = logging.getLogger("Main")
    
    logger.info("Starting Multi-Agent Content Generation System")
    
    try:
        # Load product data
        product_data = load_product_data()
        logger.info("Loaded product data for: %s", product_data['Product Name'])
        
        # Initialize orchestrator
        orchestrator = OrchestratorAgent()
        
        # Execute pipeline
        input_data = {'product_data': product_data}
        output_files = orchestrator.process(input_data)
        
        # Display final results
        print("Content Generation Completed Successfully!")
        print("\nGenerated Files:")
        for page_type, filepath in output_files.items():
            print(f"  {page_type.upper()}: {filepath}")
        
        print(f"\nSystem Performance:")
        print(f"  Total Pages Generated: {len(output_files)}")
        print(f"  Agent Pipeline: Data Parser -> Question Generator -> Content Logic -> Template Engine")
        print(f"  Output Format: Machine-readable JSON")
        
        print("\nNext Steps:")
        print("  Review generated JSON files in the output/ directory")
        print("  Validate content structure and completeness")
        print("  Test system extensibility with additional products")
        
    except Exception as e:
        logger.error("Pipeline execution failed: %s", str(e))
        print(f"Error: {str(e)}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())