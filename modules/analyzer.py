from transformers import pipeline

classifier = pipeline("zero-shot-classification",
                      model="facebook/bart-large-mnli")

def detect_risk(text, candidate_labels=None):
    if candidate_labels is None:
        candidate_labels = ["high liability", "moderate risk", "low risk", "missing clause"]
    result = classifier(text, candidate_labels)
    return result

