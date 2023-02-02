import sqlite3
import contaBancaria

banco = '/home/nicolas/DEV/curso_python/DesafioCaixaEletronico/caixaEletronico.db'

class ContasBancariasDB:
    
    def __init__(self, arquivo):
        self.conexao = sqlite3.connect(arquivo)
        self.cursor = self.conexao.cursor()
    
    def salvarContaAoBanco(self, conta):
        consulta = 'INSERT INTO contasBancarias (nomeCompleto, cpf, numeroConta, agencia, saldo, senha) VALUES (?, ?, ?, ?, ?, ?)'
        self.cursor.execute(consulta, (conta.nomeCompleto, conta.cpf, conta.numeroConta, conta.agencia, conta.saldo, conta.senha))
        self.conexao.commit()
    
    def verificaContaPeloNum(self, numConta, agencia):
        consulta = 'SELECT * FROM contasBancarias WHERE numeroConta = ? AND agencia = ?'
        self.cursor.execute(consulta, (numConta, agencia))
        return self.cursor.fetchone()
    
    def entradaDeDinheiro(self, valor, conta, agencia):
        consulta = 'UPDATE contasBancarias SET saldo = saldo + ? WHERE numeroConta = ? AND agencia = ?'
        self.cursor.execute(consulta, (valor, conta, agencia))
        self.conexao.commit()
    
    def verificaSenha(self, numConta, agencia, senha):
        consulta = 'SELECT * FROM contasBancarias WHERE numeroConta = ? AND agencia = ? AND senha = ?'
        self.cursor.execute(consulta, (numConta, agencia, senha))
        return self.cursor.fetchone()

    def exibirSaldo(self, numConta, agencia):
        consulta = 'SELECT saldo FROM contasBancarias WHERE numeroConta = ? AND agencia = ?'
        self.cursor.execute(consulta, (numConta, agencia))
        return self.cursor.fetchone()