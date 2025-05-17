import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')
path_file = "1000_ml_jobs_us.csv"
df = pd.read_csv(path_file)

company_address = df['company_address_region'].value_counts()
comp_addr = company_address[company_address >= 10]

colors = plt.cm.tab20.colors
bar_colors = colors[:len(comp_addr)]

gr = comp_addr.plot(kind='bar', color=bar_colors)
plt.title("Regions on the US that search more ML Jobs")
plt.xlabel("Regions")
plt.ylabel("Searched Jobs")
plt.xticks(rotation=45, ha='right', fontsize=9)

for i, v in enumerate(comp_addr):
    gr.text(i, v+5, str(v), ha='center', fontsize=8)

max_deger = comp_addr.max()
plt.ylim(0, max_deger * 1.2)
plt.tight_layout()
plt.show()
print('Chart Display End...')
