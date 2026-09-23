import sqlite3

conn = sqlite3.connect("funcionarios.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS funcionarios (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        cargo TEXT,
        salario REAL
    )
''')

novo_funcionario = (1, "João", "Analista", 5000.00)
cursor.execute("INSERT INTO funcionarios VALUES (?, ?, ?, ?)", novo_funcionario)
conn.commit()

cursor.execute("SELECT * FROM funcionarios")
funcionarios = cursor.fetchall()
print("Funcionários Cadastrados:")
for funcionario in funcionarios:
    print(funcionario)

atualizacao = ("João Silva", 5500.00, 1)
cursor.execute("UPDATE funcionarios SET nome = ?, salario = ? WHERE id = ?", atualizacao)
conn.commit()

id_funcionario_para_deletar = 1
cursor.execute("DELETE FROM funcionarios WHERE id = ?", (id_funcionario_para_deletar,))
conn.commit()

conn.close()