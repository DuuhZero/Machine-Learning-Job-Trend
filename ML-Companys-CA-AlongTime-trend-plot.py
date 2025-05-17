import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.use('TkAgg')
path_file = '1000_ml_jobs_us.csv'
df = pd.read_csv(path_file)

#Divide the date part
df['job_posted_date'] = pd.to_datetime(df['job_posted_date'], errors='coerce')
df = df.dropna(subset=['job_posted_date'])

#Divide the Region part
df = df[df['company_address_region'] == 'CA']


df['month'] = df['job_posted_date'].dt.to_period('M').dt.to_timestamp()
df['CA'] = df['company_address_region']

#Divide de job_title part
jobs_df = df['job_title'].value_counts().head(10).index
df_filter = df[df['job_title'].isin(jobs_df)]

#the group part, bring together everything
grouped = df_filter.groupby(['month', 'CA', 'job_title']).size().reset_index(name='count')
grouped_ca = grouped[grouped['CA'] == 'CA']
pivot_df = grouped_ca.pivot(index='month', columns='job_title', values='count').fillna(0)

plt.figure(figsize=(14,7))
colors = plt.cm.tab20.colors
bar_color = colors[:len(pivot_df)]
pivot_df.plot(kind='line', marker= 'o', linewidth=2, color=colors)

plt.suptitle('Job Trends in ML Over Time on CA')
plt.title("In the State of California")
plt.xlabel('Quarter Months')
plt.ylabel('Job Postings')
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(rotation=45)
plt.legend(title='Job Title')
plt.tight_layout()
plt.show()
print('Chart Display End...')
