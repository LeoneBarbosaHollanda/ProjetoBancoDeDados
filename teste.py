import mysql.connector
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='bancodedadosoficial'
)

mycursor = conexao.cursor()
cpf = [1233]
s = 'SELECT * FROM bancodedadosoficial.pessoa where CPF = %s;'
mycursor.execute(s, cpf)
resultado = mycursor.fetchall()
print(len(resultado))
