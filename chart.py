import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Simulate product categories
categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Sports & Outdoors', 'Toys & Games', 'Beauty']

# Generate realistic average customer satisfaction scores (scale 1-5)
scores = [
    np.random.normal(loc=4.1, scale=0.15, size=120), # Electronics
    np.random.normal(loc=3.7, scale=0.17, size=100), # Clothing
    np.random.normal(loc=4.3, scale=0.12, size=90),  # Home & Kitchen
    np.random.normal(loc=3.9, scale=0.2, size=80),   # Sports & Outdoors
    np.random.normal(loc=4.0, scale=0.13, size=60),  # Toys & Games
    np.random.normal(loc=4.2, scale=0.14, size=65),  # Beauty
]

# Create DataFrame
cat_list = []
score_list = []
for idx, cat in enumerate(categories):
    cat_list.extend([cat] * len(scores[idx]))
    score_list.extend(scores[idx])
    
data = pd.DataFrame({'Product Category': cat_list, 'Customer Satisfaction': score_list})

# Truncate scores between 1 and 5
data['Customer Satisfaction'] = data['Customer Satisfaction'].clip(1, 5)

# Seaborn professional styling
sns.set_style('whitegrid')
sns.set_context('talk')
palette = sns.color_palette('Set2')

plt.figure(figsize=(8, 8))
bar = sns.barplot(
    data=data,
    x='Product Category',
    y='Customer Satisfaction',
    ci='sd',
    palette=palette,
    edgecolor='black'
)

bar.set_title('Average Customer Satisfaction by Product Category', fontsize=18, weight='bold', pad=20)
bar.set_xlabel('Product Category', fontsize=14)
bar.set_ylabel('Avg. Customer Satisfaction (1-5)', fontsize=14)

plt.xticks(rotation=20, ha='right')
plt.ylim(3.0, 4.6)
plt.tight_layout()
plt.savefig('chart.png', dpi=64, bbox_inches='tight')
plt.close()
