from transformers import pipeline

# Step 1: Load pre-trained summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Step 2: Read your article text from a file
with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Optional: The model works best on <= 1024 tokens, so you can truncate long texts
max_chunk = 1000  # characters
text = text[:max_chunk]

# Step 3: Generate summary
summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
summary_text = summary[0]['summary_text']

# Step 4: Print summary
print("\n📝 AI-Powered Summary:\n")
print(summary[0]['summary_text'])

# Step 5: Save summary to a new file
with open("summary_output.txt", "w", encoding="utf-8") as f:
    f.write(summary_text)