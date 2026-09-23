import matplotlib.pyplot as plt

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio']
vendas = [12, 15, 18, 14, 16]

plt.bar(meses, vendas, color='royalblue')

plt.xlabel('Mês')
plt.ylabel('Vendas (em unidades)')

plt.title('Vendas Mensais')

plt.show()