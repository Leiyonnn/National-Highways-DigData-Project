import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "DigData Step Up.xlsx"
campaigns_data = pd.read_excel(file_path, sheet_name="Campaigns data")
study_data = pd.read_excel(file_path, sheet_name="Study Data")

print("Campaigns Data Preview:")
print(campaigns_data.head())

print("\nStudy Data Preview:")
print(study_data.head())

merged_data = pd.merge(campaigns_data, study_data, on=["study_id", "cell_id"], how="inner")
print("\nMerged Data Preview:")
print(merged_data.head())

winning_data = merged_data[merged_data['is_winner_cell'] == 1]

success_by_region = winning_data['advertiser_region'].value_counts(normalize=True) * 100
success_by_ad_type = winning_data[['is_video', 'is_interactive_ad']].mean() * 100
success_by_vertical = winning_data['vertical'].value_counts(normalize=True) * 10

sns.set(style="whitegrid")

fig, axes = plt.subplots(3, 1, figsize=(10, 8))

sns.barplot(x=success_by_region.index, y=success_by_region.values, palette="viridis", ax=axes[0])
axes[0].set_title("Regional Success Distribution")
axes[0].set_xlabel("Region")
axes[0].set_ylabel("Success Rate (%)")

sns.barplot(x=success_by_ad_type.index, y=success_by_ad_type.values, palette="coolwarm", ax=axes[1])
axes[1].set_title("Ad Type Success Distribution")
axes[1].set_xlabel("Ad Type")
axes[1].set_ylabel("Percentage of Winning Campaigns (%)")
axes[1].set_xticklabels(["Video", "Interactive Ad"])

top_verticals = success_by_vertical.head(10)
sns.barplot(y=top_verticals.index, x=top_verticals.values, palette="magma", ax=axes[2])
axes[2].set_title("Top 10 Advertiser Success Distribution")
axes[2].set_xlabel("Success Rate (%)")
axes[2].set_ylabel("")

plt.tight_layout()
plt.show()
