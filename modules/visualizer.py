import matplotlib.pyplot as plt
import seaborn as sns

def plot_risk_distribution(risk_report):
    labels = risk_report['labels']
    scores = risk_report['scores']
    
    plt.figure(figsize=(8,4))
    sns.barplot(x=labels, y=scores, palette="viridis")
    plt.title("Contract Clause Risk Distribution")
    plt.ylabel("Confidence Score")
    plt.xlabel("Risk Labels")
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.savefig("assets/risk_plot.png")  # Save plot to assets
    return "assets/risk_plot.png"

