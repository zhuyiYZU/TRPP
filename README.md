# TRPP
1. **Reverse_prompt.py**: This script identifies a set of prompts used to generate the target text by utilizing a specific prompt. It then filters these prompts through an agent voting mechanism.

2. **Generate_text.py**: This script takes the filtered prompts and inputs them into a large language model to generate text.

3.1 & 3.2: Using BERT similarity, the script evaluates the similarity between the generated text and the target text. A threshold is set, and if the similarity exceeds this threshold, the text is classified as machine-generated.

4. **Decision.py**: This script combines the results from the TRPP method and other techniques to make a final determination.
