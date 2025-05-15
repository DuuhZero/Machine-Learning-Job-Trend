import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
##Need to install matplotlib, python3-tk

matplotlib.use('TkAgg')
path_file = "1000_ml_jobs_us.csv"
df = pd.read_csv(path_file)

#More hired jobs in ML market
company_jobs = df['job_title'].value_counts()
jobs_df = company_jobs[company_jobs >= 5]

gr = jobs_df.plot(kind='bar', color='green')
plt.title('Most Searched Jobs In Machine Learning Market')
plt.xlabel('Jobs')
plt.ylabel('Search Numbers')
plt.xticks(rotation=45, ha='right', fontsize=9)

for i, v in enumerate(jobs_df):
    gr.text(i, v + 10, str(v), ha='center', va='top', fontsize=8)

max_deger = jobs_df.max()
plt.ylim(0, max_deger * 1.2)
plt.tight_layout()
plt.show()
print("Chart Display End...")

