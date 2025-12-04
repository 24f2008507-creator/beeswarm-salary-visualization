import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ----------------------------------------------------
# 1. Generate realistic synthetic customer satisfaction data
# ----------------------------------------------------

# Define product categories and a rough "true" mean satisfaction for each
product_categories = [
    "Electronics",
    "Home & Kitchen",
    "Clothing",
    "Beauty & Personal Care",
    "Sports & Outdoors"
]

# Target (true) average satisfaction per category (on a 1–5 scale)
category_means = {
    "Electronics": 3.8,
    "Home & Kitchen": 4.1,
    "Clothing": 3.6,
    "Beauty & Personal Care": 4.3,
    "Sports & Outdoors": 3.9,
}

# Generate synthetic survey responses
np.random.seed(42)  # for reproducibility
records = []

# 50 customers per category (you can adjust this)
n_customers_per_category = 50

for cat in product_categories:
    mean = category_means[cat]
    # Sample around the mean with some noise, clip between 1 and 5
    scores = np.random.normal(loc=mean, scale=0.4, size=n_customers_per_category)
    scores = np.clip(scores, 1.0, 5.0)

    for score in scores:
        records.append({"product_category": cat, "satisfaction_score": score})

df = pd.DataFrame(records)

# ----------------------------------------------------
# 2. Set Seaborn styling for executive-ready appearance
# ----------------------------------------------------
sns.set_style("whitegrid")
sns.set_context("talk")  # larger fonts, good for presentations

# ----------------------------------------------------
# 3. Create barplot of average satisfaction by category
# ----------------------------------------------------
plt.figure(figsize=(8, 8))  # 8 inches x 8 inches; with dpi=64 → 512x512 pixels

ax = sns.barplot(
    data=df,
    x="product_category",
    y="satisfaction_score",
    estimator=np.mean,
    errorbar=("ci", 95),  # 95% confidence intervals
    palette="Blues_d"
)

# Titles and labels
ax.set_title("Average Customer Satisfaction by Product Category", pad=20)
ax.set_xlabel("Product Category")
ax.set_ylabel("Average Satisfaction Score (1–5)")

# Rotate x labels for readability
plt.xticks(rotation=20, ha="right")

# Tight layout to avoid clipping labels
plt.tight_layout()

# ----------------------------------------------------
# 4. Save chart as 512x512 PNG
# ----------------------------------------------------
# 8 inches * 64 dpi = 512 pixels → exactly 512x512
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()

print("chart.png has been generated successfully.")
