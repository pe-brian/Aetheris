# Aetheris
IA agent capable of navigating digital space to accomplish simple tasks dictated in natural language.

# Steps:

0. Create a browser context with playwright
1. Take a screenshot of the current web page
2. Analyze with OCR and outputs image with bounding boxes and yaml data
3. Use LLM to group paragraphs and tag fields/buttons/links as clickable items
4. Generate RPA instructions
5. Execute RPA instructions in the web page
