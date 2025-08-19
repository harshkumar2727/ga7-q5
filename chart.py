import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)
categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Sports & Outdoors', 'Toys & Games', 'Beauty']
means = [4.1, 3.7, 4.3, 3.9, 4.0, 4.2]
sizes = [120, 100, 90, 80, 60, 65]

# Generate synthetic data
data = []
for cat, mean, n in zip(categories, means, sizes):
    scores = np.random.normal(mean, 0.15, n)
    scores = np.clip(scores, 1, 5)
    for score in scores:
        data.append({'Product Category': cat, 'Customer Satisfaction': score})

df = pd.DataFrame(data)

sns.set_style("whitegrid")
sns.set_context("talk")
plt.figure(figsize=(8, 8))
ax = sns.barplot(
    data=df, 
    x='Product Category', 
    y='Customer Satisfaction', 
    ci='sd', 
    palette='Set2',
    edgecolor='black'
)
ax.set_title('Average Customer Satisfaction by Product Category', fontsize=18, weight='bold', pad=20)
ax.set_xlabel('Product Category', fontsize=14)
ax.set_ylabel('Avg. Customer Satisfaction (1-5)', fontsize=14)
plt.xticks(rotation=20, ha='right')
plt.ylim(3.0, 4.6)
plt.tight_layout()
plt.savefig('chart.png', dpi=64, bbox_inches='tight')
plt.close()
