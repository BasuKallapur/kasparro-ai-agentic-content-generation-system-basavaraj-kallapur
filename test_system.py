"""Simple test to verify the multi-agent system works correctly."""

import json
import os
from src.agents.orchestrator_agent import OrchestratorAgent


def test_system():
    """Test the complete system pipeline."""
    print("Testing Multi-Agent Content Generation System")
    
    # Test data
    product_data = {
        'Product Name': 'GlowBoost Vitamin C Serum',
        'Concentration': '10% Vitamin C',
        'Skin Type': 'Oily, Combination',
        'Key Ingredients': 'Vitamin C, Hyaluronic Acid',
        'Benefits': 'Brightening, Fades dark spots',
        'How to Use': 'Apply 2–3 drops in the morning before sunscreen',
        'Side Effects': 'Mild tingling for sensitive skin',
        'Price': '₹699'
    }
    
    # Run system
    orchestrator = OrchestratorAgent()
    input_data = {'product_data': product_data}
    output_files = orchestrator.process(input_data)
    
    # Verify outputs
    assert len(output_files) >= 2, "Should generate at least 2 pages"
    
    # Check that required files exist with correct names
    expected_files = ['faq.json', 'product_page.json', 'comparison_page.json']
    for expected_file in expected_files:
        expected_path = os.path.join('output', expected_file)
        assert os.path.exists(expected_path), f"Required file {expected_path} should exist"
    
    for page_type, filepath in output_files.items():
        assert os.path.exists(filepath), f"Output file {filepath} should exist"
        
        with open(filepath, 'r') as f:
            data = json.load(f)
            assert 'page_type' in data, "Should have page_type field"
            assert 'content' in data, "Should have content field"
            assert 'metadata' in data, "Should have metadata field"
    
    print("All tests passed!")
    return True


if __name__ == "__main__":
    test_system()