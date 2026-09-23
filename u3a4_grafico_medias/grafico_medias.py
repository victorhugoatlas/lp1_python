import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")
df = sns.load_dataset('tips')

plt.figure(figsize=(8, 5))
sns.barplot(x='time', y='total_bill', data=df, estimator=sum, errorbar=None, palette="Set2")
plt.xlabel('Período (Time)')
plt.ylabel('Total de Gastos')
plt.title('Total de Gastos por Período (Almoço ou Jantar)')
plt.show()

plt.figure(figsize=(8, 5))
sns.barplot(x='time', y='total_bill', data=df)
plt.xlabel('Período (Time)')
plt.ylabel('Média de Gastos')
plt.title('Média de Gastos por Período (Almoço ou Jantar)')
plt.show()

plt.figure(figsize=(8, 5))
sns.barplot(x='time', y='tip', data=df, palette="Set3")
plt.xlabel('Período (Time)')
plt.ylabel('Média da Gorjeta')
plt.title('Média da Gorjeta por Período (Almoço ou Jantar)')
plt.show()