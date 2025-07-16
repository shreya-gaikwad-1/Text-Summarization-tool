# Text-Summarization-tool
Company: CODTECH IT SOLUTIONS | Name: Shreya Sandesh Gaikwad | Intern ID: CT08DN1787 | Domain: Artificial Intelligence | Duration: 8 weeks | Mentor: Neela Santosh

An AI-powered text summarization tool built with Hugging Face Transformers using the BART model. It reads text from a file and generates concise summaries. Developed in Python and tested locally using VS Code.

How It Works
- Reads input text from a file named input.txt.
- Applies the facebook/bart-large-cnn model for summarization.
- Saves the summarized output to a file named summary_output.txt.
- Also prints the summary to the terminal for quick viewing.

Files:
- NLPmodel.py: The main Python script that performs summarization.
- input.txt: The file containing the original article or paragraph to summarize.
- summary_output.txt: The file where the summarized result is saved.

Requirements:
- Python 3.7+
- Hugging Face Transformers library

Usage:
- Add your text content to input.txt.
- Run the script: python NLPmodel.py
- View your summary in: Terminal output or summary_output.txt


