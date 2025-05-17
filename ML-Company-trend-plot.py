import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')
path_file = "1000_ml_jobs_us.csv"
df = pd.read_csv(path_file)

companys = df['company_name'].value_counts()
comp_df = companys[companys >= 10]

#Generate an array that contains different color for each bar in the chart
colors = plt.cm.tab20.colors #ColorMap that have 20 diff colors
bar_colors = colors[:len(comp_df)] #Catch only the necessary number to do it

#Define the chart with the color and kind
gr = comp_df.plot(kind='bar', color=bar_colors)
plt.title("Companys with more number of Posted Jobs")
plt.xlabel("Companys")
plt.ylabel("Posted Jobs")
plt.xticks(rotation=45, ha='right', fontsize=9)

#write the number of posted jobs in the top of each bar company
for i, v in enumerate (comp_df):
    #Insert the numbers with a little of space (v+5)
    gr.text(i, v + 5, str(v), ha='center', va='top', fontsize=8)

max_deger = comp_df.max()
plt.ylim(0, max_deger * 1.2)
plt.tight_layout()
plt.show()
print("Chart Display End...")
