#SMART-BANK

import random
import sqlite3
import dataBase

arquivoBanco = '/home/nicolas/DEV/curso_python/DesafioCaixaEletronico/caixaEletronico.db'
acessaOBanco = dataBase.ContasBancariasDB(arquivoBanco)


class ContaPessoaFisica:

    logou = False
    numContaEntrada = ''
    agenciaContaEntrada = ''

    def __init__(self):
        self.logou = False       
        self.agencia = "3966"

    def CriarConta(self):
        self.numeroConta = random.randint(1,599)
        self.nomeCompleto = input("Digite o nome do titular: ")
        self.cpf = input("Digite o cpf do titular: ")
        self.senha = input("Digite a senha de 6 digitos (apenas números): ")
        condicaoSenhaCorreta = (len(self.senha) < 7 and len(self.senha) > 5 and self.senha.isdigit)
        while(condicaoSenhaCorreta is False):
            self.senha = input("Tente novamente lembrando (6 digitos apenas números): ")
            condicaoSenhaCorreta = (len(self.senha) < 7 and len(self.senha) > 5 and self.senha.isdigit)
        self.saldo = 0
        acessaOBanco.salvarContaAoBanco(self)

    def ExibirContaComSaldo(self):
        print(f"Parabêns Sr(a) {self.nomeCompleto}, sua conta foi criada com os seguintes dados:")
        print("Nome: [" + self.nomeCompleto + "]")
        print("CPF: [" + self.cpf + "]")
        print("Agência: ["+ self.agencia + "]")
        print("Número da conta [" + str(self.numeroConta) + "]")
        print("Saldo da conta [" + str(self.saldo) + "]")

    def ExibirContaSemSaldo(self):
        print(f"Parabêns Sr(a) {self.nomeCompleto}, sua conta foi criada com os seguintes dados:")
        print("Nome: [" + self.nomeCompleto + "]")
        print("CPF: [" + self.cpf + "]")
        print("Agência: ["+ self.agencia + "]")
        print("Número da conta [" + str(self.numeroConta) + "]")
    
    def BuscarContaNoBD(self, numContaEntrada, agencia):
        retorno = False
        if acessaOBanco.verificaContaPeloNum(numContaEntrada, agencia) == None:
            tentarNovamente = input("Conta não encontrada...\nTentar novamente? [S]im [N]ão: ")
            if tentarNovamente == 's' or tentarNovamente == 'S':
                self.FazerDeposito()
            elif tentarNovamente == 'n' or tentarNovamente == 'N':
                retorno = False
            else:
                print("Opção inválida...")
                retorno = False
        else: 
            retorno =  True
        return retorno

    def FazerDeposito(self):
        contaDep = input("Informe a conta para depósito: ")
        agenciaDep = input("Informe a agência para depósito: ")
        self.BuscarContaNoBD(contaDep, agenciaDep)
        valor = float(input("Digite o valor que está no envelope: "))
        acessaOBanco.entradaDeDinheiro(valor, contaDep, agenciaDep)
        print("Depósito realizado...")

    def ValidarSenha(self, numContaEntrada, agenciaContaEntrada, senhaEntrada):
        retorno = False
        if acessaOBanco.verificaSenha(numContaEntrada, agenciaContaEntrada, senhaEntrada) != None:
            retorno = True
        else:
            retorno = False
        return retorno

    def ExibirSaldo(self, numContaEntrada, agenciaContaEntrada):
        print(acessaOBanco.exibirSaldo(numContaEntrada, agenciaContaEntrada))
    

    def AcessarConta(self):
        self.numContaEntrada = input("Informe o NÚMERO da conta: ")
        self.agenciaContaEntrada = input("Informe a AGÊNCIA da conta: ")
        if self.BuscarContaNoBD(self.numContaEntrada, self.agenciaContaEntrada) == True:
            senhaEntrada = input("Digite a senha: ")
            if self.ValidarSenha(self.numContaEntrada, self.agenciaContaEntrada, senhaEntrada) == True:
                self.logou = True
            else:
                tentarNovamente = input("Dados inválidos, tentar novamente?'\n [S]im [N]ão: ")
                if tentarNovamente == 'S' or tentarNovamente == 's':
                    self.AcessarConta()
                elif tentarNovamente == 'N' or tentarNovamente == 'n':
                    print("Voltando ao menu...")
                    self.logou = False
                else:
                    self.logou = False
                    print("Opção inválida!")
                    print("Voltando ao menu...")
        else:
            print("AGENCIA E CONTA NÃO ENCONTRADOS...")

    def FazerSaque(self):
        self.ExibirSaldo(self.numContaEntrada, self.agenciaContaEntrada)
        if self.logou == True:
            self.ExibirSaldo(self.numContaEntrada, self.agenciaContaEntrada)
            valorSaque = input("Qual o valor do saque: ")

    
    def __repr__(self):
        return str(self.__dict__)
