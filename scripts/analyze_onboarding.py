import pandas as pd

# Load dataset
df = pd.read_csv('data/intern_onboarding.csv')

# Overview
print("📊 Total Interns:", len(df))
print("✅ Onboarding Completed:", df['onboarding_completed'].value_counts())

# Grouped stats
completion_by_team = df.groupby('team')['onboarding_completed'].value_counts().unstack().fillna(0)
avg_feedback = df.groupby('team')['feedback_score'].mean()

# Save summary
completion_by_team.to_csv('data/onboarding_status_by_team.csv')
avg_feedback.to_csv('data/average_feedback_by_team.csv')

print("✅ Summary files saved in data/")
