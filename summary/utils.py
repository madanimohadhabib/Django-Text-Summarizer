from transformers import pipeline

# Function to generate a summary
def generate_summary(text):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=3500, min_length=30, do_sample=False)
    return summary[0]['summary_text']
