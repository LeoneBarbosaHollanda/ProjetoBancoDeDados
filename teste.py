import mysql.connector
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='leone16tuf@',
    database='bancodedadosoficial'

)

mycursor = conexao.cursor()
cpf = [1233]
s = 'SELECT * FROM bancodedadosoficial.pessoa where CPF = %s;'
mycursor.execute(s, cpf)
resultado = mycursor.fetchall()
print(len(resultado))
