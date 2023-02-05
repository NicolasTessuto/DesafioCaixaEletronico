import sqlite3
import contaBancaria

banco = '/home/nicolas/DEV/curso_python/DesafioCaixaEletronico/caixaEletronico.db'

class ContasBancariasDB:
    
    def __init__(self, arquivo):
        self.conexao = sqlite3.connect(arquivo)
        self.cursor = self.conexao.cursor()
    
    def SalvarContaAoBanco(self, conta):
        consulta = 'INSERT INTO contasBancarias (nomeCompleto, cpf, numeroConta, agencia, saldo, senha) VALUES (?, ?, ?, ?, ?, ?)'
        self.cursor.execute(consulta, (conta.nomeCompleto, conta.cpf, conta.numeroConta, conta.agencia, conta.saldo, conta.senha))
        self.conexao.commit()
    
    def VerificaContaPeloNum(self, numContaDigitada, agenciaContaDigitada):
        consulta = 'SELECT * FROM contasBancarias WHERE numeroConta = ? AND agencia = ?'
        self.cursor.execute(consulta, (numContaDigitada, agenciaContaDigitada))
        return self.cursor.fetchone()
    
    def EntradaDeDinheiro(self, valor, numContaDigitada, agenciaContaDigitada):
        consulta = 'UPDATE contasBancarias SET saldo = saldo + ? WHERE numeroConta = ? AND agencia = ?'
        self.cursor.execute(consulta, (valor, numContaDigitada, agenciaContaDigitada))
        self.conexao.commit()
    
    def VerificaSenha(self, numContaDigitada, agenciaContaDigitada, senha):
        consulta = 'SELECT * FROM contasBancarias WHERE numeroConta = ? AND agencia = ? AND senha = ?'
        self.cursor.execute(consulta, (numContaDigitada, agenciaContaDigitada, senha))
        return self.cursor.fetchone()
        
    def ExibirSaldo(self, numContaDigitada, agenciaContaDigitada):
        consulta = 'SELECT saldo FROM contasBancarias WHERE numeroConta = ? AND agencia = ?'
        self.cursor.execute(consulta, (numContaDigitada, agenciaContaDigitada))
        return self.cursor.fetchone()

    def RetiradaDeDinheiro(self, numContaDigitada, agenciaContaDigitada, valorDigitado):
        consulta = 'UPDATE contasBancarias SET saldo = saldo - ? WHERE numeroConta = ? AND agencia = ?'
        self.cursor.execute(consulta,(valorDigitado, numContaDigitada, agenciaContaDigitada))
        self.conexao.commit()

    def DeletarConta(self, numContaDigitada, agenciaContaDigitada, senha):
        consulta = 'DELETE FROM contasBancarias WHERE numeroConta = ? AND agencia = ? AND senha = ?'
        self.cursor.execute(consulta, (numContaDigitada, agenciaContaDigitada, senha))
        self.conexao.commit()

    def TransferenciaEntreContas(self, valorTransf, numContaLogada, agenciaContaLogada, senha, numContaTransf, agenciaContaTransf):
        consulta = 'UPDATE contasBancarias SET saldo = saldo - ? WHERE numeroConta = ? AND agencia = ? AND senha = ?'
        consulta2 = 'UPDATE contasBancarias SET saldo = saldo + ? WHERE numeroConta = ? AND agencia = ?'
        self.cursor.execute(consulta, (valorTransf, numContaLogada, agenciaContaLogada, senha))
        self.conexao.commit()
        self.cursor.execute(consulta2, (valorTransf, numContaTransf, agenciaContaTransf))
        self.conexao.commit()