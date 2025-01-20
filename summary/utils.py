from transformers import pipeline

# Fonction pour générer un résumé
def generate_summary(text):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return summary[0]['summary_text']
