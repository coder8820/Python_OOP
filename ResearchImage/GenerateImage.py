import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB

# -----------------------------
# 1. Load Dataset
# -----------------------------
# Download dataset: https://archive.ics.uci.edu/ml/datasets/phishing+websites
# Assume file is "phishing.csv"
data = pd.read_csv("phishing.csv")

# Features and target
X = data.drop("Result", axis=1)   # "Result" is target column
y = data["Result"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# -----------------------------
# 2. Train Models
# -----------------------------
models = {
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(random_state=42, n_estimators=100),
    "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
    "Naïve Bayes": GaussianNB()
}

results = {"Algorithm": [], "Accuracy": [], "Precision": [], "Recall": [], "F1-score": []}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    results["Algorithm"].append(name)
    results["Accuracy"].append(round(accuracy_score(y_test, y_pred) * 100, 2))
    results["Precision"].append(round(precision_score(y_test, y_pred, average="weighted") * 100, 2))
    results["Recall"].append(round(recall_score(y_test, y_pred, average="weighted") * 100, 2))
    results["F1-score"].append(round(f1_score(y_test, y_pred, average="weighted") * 100, 2))

# Convert to DataFrame
results_df = pd.DataFrame(results)
print(results_df)

# -----------------------------
# 3. Save Accuracy Bar Chart
# -----------------------------
plt.figure(figsize=(7,5))
plt.bar(results_df["Algorithm"], results_df["Accuracy"], color="skyblue")
plt.title("Accuracy Comparison of Algorithms")
plt.ylabel("Accuracy (%)")
plt.ylim(80, 100)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.savefig("accuracy.png")
plt.close()

# -----------------------------
# 4. Save Precision/Recall/F1 Chart
# -----------------------------
x = np.arange(len(results_df["Algorithm"]))
width = 0.25

plt.figure(figsize=(9,6))
plt.bar(x - width, results_df["Precision"], width, label="Precision")
plt.bar(x, results_df["Recall"], width, label="Recall")
plt.bar(x + width, results_df["F1-score"], width, label="F1-score")

plt.xticks(x, results_df["Algorithm"])
plt.title("Precision, Recall, and F1-score Comparison")
plt.ylabel("Percentage (%)")
plt.ylim(80, 100)
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.savefig("metrics.png")
plt.close()

# -----------------------------
# 5. Save Workflow Diagram
# -----------------------------
fig, ax = plt.subplots(figsize=(10,4))

box_style = dict(boxstyle="round,pad=0.5", facecolor="skyblue", edgecolor="black")

steps = ["Dataset", "Preprocessing", "ML Models", "Evaluation", "Results"]
positions = [0.1, 0.3, 0.5, 0.7, 0.9]

# Draw boxes
for step, pos in zip(steps, positions):
    ax.text(pos, 0.5, step, ha="center", va="center", fontsize=12, bbox=box_style)

# Draw arrows
for i in range(len(positions)-1):
    ax.annotate("", xy=(positions[i+1]-0.05, 0.5), xytext=(positions[i]+0.05, 0.5),
                arrowprops=dict(arrowstyle="->", lw=2))

ax.set_axis_off()
plt.title("Workflow of Phishing Website Detection Research", fontsize=14)
plt.savefig("workflow.png")
plt.close()
