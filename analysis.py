
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../data/it_tickets.csv')

print("Total Tickets:", len(df))
print("Avg Resolution Time:", df["Resolution_Time"].mean())

sla = (df["Resolution_Time"] <= 24).mean() * 100
print("SLA Compliance:", sla)

print(df.groupby("Category")["Ticket_ID"].count())

sns.countplot(x="Category", data=df)
plt.show()
