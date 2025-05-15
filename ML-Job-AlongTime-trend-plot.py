import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
##Need to install matplotlib, python3-tk and numpy if you don't have
#Made By DuuhZero
matplotlib.use('TkAgg')
path_file = "1000_ml_jobs_us.csv"
df = pd.read_csv(path_file)

#Jobs Trends in Machine Learning Over Time
#We have the top 10 most posted jobs and will plot the evolution over the years
df['job_posted_date'] = pd.to_datetime(df['job_posted_date'], errors='coerce')
df = df.dropna(subset=['job_posted_date'])
df['month'] = df['job_posted_date'].dt.to_period('M').dt.to_timestamp()

jobs_df = df['job_title'].value_counts().head(10).index
df_filter = df[df['job_title'].isin(jobs_df)]
grouped = df_filter.groupby(['month', 'job_title']).size().reset_index(name='count')

pivot_df = grouped.pivot(index='month', columns='job_title', values='count').fillna(0)

plt.figure(figsize=(14, 7))
colors = plt.cm.Set2(np.linspace(0, 1, len(pivot_df.columns)))

pivot_df.plot(kind='line', marker='o', linewidth=2 ,color=colors)

plt.title('Job Trends in Machine Learning Over Time')
plt.xlabel('Quarter Months')
plt.ylabel('Job Postings')
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(rotation=45)
plt.legend(title='Job Title')
plt.tight_layout()
plt.show()
print("Chart Display End...")


