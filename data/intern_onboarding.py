import pandas as pd
import random
from datetime import datetime, timedelta

# Sample values
teams = ['Data Science', 'Engineering', 'Marketing', 'Product', 'Design']
mentors = ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan']
names = [f"Intern_{i}" for i in range(1, 101)]

data = []

for i, name in enumerate(names, 1):
    intern_id = f"INT{i:03}"
    team = random.choice(teams)
    mentor = random.choice(mentors)
    join_date = datetime(2024, 6, 1) + timedelta(days=random.randint(0, 90))
    onboarding_completed = random.choice(['Yes', 'No'])
    modules_completed = random.randint(0, 5) if onboarding_completed == 'Yes' else random.randint(0, 2)
    first_project_assigned = 'Yes' if modules_completed >= 3 else 'No'
    feedback_score = random.choice([1, 2, 3, 4, 5]) if onboarding_completed == 'Yes' else None

    data.append([
        intern_id, name, team, mentor,
        join_date.strftime('%Y-%m-%d'),
        onboarding_completed, modules_completed,
        first_project_assigned, feedback_score
    ])

# Create DataFrame
columns = [
    'intern_id', 'name', 'team', 'mentor',
    'join_date', 'onboarding_completed',
    'modules_completed', 'first_project_assigned', 'feedback_score'
]

df = pd.DataFrame(data, columns=columns)
df.to_csv("data/intern_onboarding.csv", index=False)
