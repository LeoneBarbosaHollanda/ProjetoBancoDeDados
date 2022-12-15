from flask import Flask, render_template
from flask.globals import request

import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='leone16tuf@',
    database='bancodedadosoficial'

)

mycursor = conexao.cursor()


app = Flask(__name__)


def consultaBD(nome, CPF):
    consu = [nome, CPF]
    s = 'SELECT * FROM bancodedadosoficial.pessoa where Nome = %s and CPF = %s;'
    mycursor.execute(s, consu)
    resultado = mycursor.fetchall()
    return resultado


class Dividas:
    def __init__(self, Nome, CPF, Valor):
        self.Nome = Nome
        self.CPF = int(CPF)
        self.Valor = Valor
        pass


class ValorEmprst:
    def __init__(self, valor, prest, data, CPF):
        self.valor = float(valor)
        self.prest = int(prest)
        self.data = data
        self.CPF = int(CPF)
        pass


class classPagar:
    def __init__(self, PREÇO, CPF, data):
        self.PREÇO = int(PREÇO)
        self.data = data
        self.CPF = int(CPF)
        pass


class classReceber:
    def __init__(self, PREÇO, CPF, data):
        self.PREÇO = int(PREÇO)
        self.data = data
        self.CPF = int(CPF)
        pass


class consult:
    def __init__(self, Conta, Nome, Agencia, RG, SaldoConta, Senha, CPF):
        self.Conta = int(Conta)
        self.Nome = str(Nome)
        self.Agencia = int(Agencia)
        self.RG = int(RG)
        self.SaldoConta = int(SaldoConta)
        self.Senha = str(Senha)
        self.CPF = int(CPF)

        pass


class cadastro:
    def __init__(self, CPF, Nome, Senha, RG, SaldoConta, Agencia):
        self.CPF = int(CPF)
        self.Nome = str(Nome)
        self.Senha = str(Senha)
        self.Agencia = int(Agencia)
        self.RG = int(RG)
        self.SaldoConta = int(SaldoConta)
        pass


@app.route('/cadastrar', methods=["POST"])
def cadastrar():
    try:
        p = cadastro(request.form['CPF'], request.form['Nome'],
                     request.form['Senha'], request.form['RG'], SaldoConta=0, Agencia=1)
        lista = [p.Nome, p.Agencia, p.RG, p.SaldoConta, p.Senha, p.CPF]

        sqlIncremento = 'INSERT INTO pessoa (Nome, Agencia, RG, SaldoConta, Senha, CPF) VALUES (%s,%s,%s,%s,%s,%s)'
        mycursor.execute(sqlIncremento, lista)
        conexao.commit()
    except:
        return render_template('ERROR.html')
    return render_template("index.html")


@app.route('/consultar', methods=["POST", "GET"])
def consulta():
    try:
        C = consultaBD(request.form['Nome'], request.form['CPF'])

        a = consult(C[0][0], C[0][1], C[0][2], C[0]
                        [3], C[0][4], C[0][5], C[0][6])

        Lista = []
        Lista.append(a)
        return render_template("/consulta.html", Lista=Lista)
    except:
        return render_template('/ERROR.html')


@app.route('/')
def main():
    return render_template("index.html")


@app.route('/recebimento', methods=["POST", "GET"])
def receber():
    p = classReceber(
        request.form['Valor'], request.form['CPF'], request.form.get('data'))
    lista = []
    try:
        r = [p.PREÇO, p.data, p.CPF]
        lista.append(p)
        notinha = (
            'INSERT INTO bancodedadosoficial.recebimento (`PREÇO`, `dataRecebimento`, `CPF`) VALUES (%s, %s, %s);')
        mycursor.execute(notinha, r)
        u = [p.PREÇO, p.CPF]
        up = 'UPDATE `bancodedadosoficial`.`pessoa` SET `SaldoConta` = %s+SaldoConta WHERE  `CPF` = %s;'
        mycursor.execute(up, u)
        conexao.commit()

    except:
        return render_template('/ERROR.html')

    return render_template('/notinha.html', Lista=lista)


@app.route('/excluir', methods=['POST', 'GET'])
def apagar():

    cpf = [int(request.form['CPF'])]
    s = 'SELECT * FROM bancodedadosoficial.pessoa where CPF = %s;'
    mycursor.execute(s, cpf)
    resultado = mycursor.fetchall()
    if len(resultado) == 0:
        return render_template('/ERROR.html')
    e = f"DELETE FROM `bancodedadosoficial`.`emprestimo` WHERE (`CPF` = {cpf[0]}) ;"
    mycursor.execute(e)
    p = f"DELETE FROM `bancodedadosoficial`.`pagamento` WHERE (`CPF` = {cpf[0]}) ;"
    mycursor.execute(p)
    a = f"DELETE FROM `bancodedadosoficial`.`recebimento` WHERE (`CPF` = {cpf[0]}) ;"
    mycursor.execute(a)
    b = f"DELETE FROM `bancodedadosoficial`.`pessoa` WHERE `CPF` = {cpf[0]} and `Senha` = '{request.form['Senha']}';"
    mycursor.execute(b)
    conexao.commit()
    return render_template('/excluir.html')


@app.route('/pagamento', methods=["POST", "GET"])
def Pagar():
    try:
        j = classPagar(
            request.form['Valor'], request.form['CPF'], request.form.get('data'))
        lista = []
        a = [j.PREÇO, j.data, j.CPF]
        lista.append(j)
        notinha = 'INSERT INTO bancodedadosoficial.pagamento (`PREÇO`, `dataPagamento`, `CPF`) VALUES (%s, %s, %s);'
        mycursor.execute(notinha, a)
        g = [j.PREÇO, j.CPF]
        down = 'UPDATE `bancodedadosoficial`.`pessoa` SET `SaldoConta` = (SaldoConta-%s) WHERE  `CPF` = %s;'
        mycursor.execute(down, g)
        conexao.commit()
    except:
        return render_template('/ERROR.html')
    return render_template('/notinha.html', Lista=lista)
    # return render_template('/ERROR.html')


@app.route('/emprestimo', methods=['POST', 'GET'])
def emprst():
    try:
        C = consultaBD(request.form['Nome'], request.form['CPF'])
        a = consult(C[0][0], C[0][1], C[0][2], C[0]
                        [3], C[0][4], C[0][5], C[0][6])
        if a.SaldoConta <= 0:
            return render_template('SemEmprestimo.html')
        elif a.SaldoConta > 0:
            return render_template('ComEmprestimo.html')
    except:
        return render_template('/ERROR.html')


@app.route('/emprestimoConfirmado', methods=['POST', 'GET'])
def emprestimoApr():
    a = ValorEmprst(request.form['ValorTotal'], request.form[
        'Parcelas'], request.form['Data'], request.form['CPF'])

    frase = f'INSERT INTO bancodedadosoficial.emprestimo (`VALOR`, `PARCELA`, `dataEmprestimo`, `CPF`) VALUES ({a.valor/a.prest}, {a.prest}, "{a.data}", {a.CPF});'
    mycursor.execute(frase)
    up = F'UPDATE `bancodedadosoficial`.`pessoa` SET `SaldoConta` = {a.valor}+SaldoConta WHERE  `CPF` = {a.CPF};'
    mycursor.execute(up)
    conexao.commit()
    return render_template('/index.html')


@app.route('/consultarDividas', methods=['POST', 'GET'])
def consultarDivida():
    a = 'SELECT Nome,pessoa.CPF,sum(VALOR)*PARCELA as valorTotalEmprestimo FROM bancodedadosoficial.emprestimo, bancodedadosoficial.pessoa where emprestimo.CPF = pessoa.CPF GROUP BY pessoa.CPF ;'
    mycursor.execute(a)
    resultado = mycursor.fetchall()
    lista = []
    for n in resultado:
        lista.append(Dividas(n[0], n[1], n[2]))
    return render_template('/Endividados.html', Lista=lista)


app.run(debug=True)
