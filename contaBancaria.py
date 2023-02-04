#SMART-BANK

import random
import sqlite3
import dataBase

arquivoBanco = '/home/nicolas/DEV/curso_python/DesafioCaixaEletronico/caixaEletronico.db'
acessaOBanco = dataBase.ContasBancariasDB(arquivoBanco)


class ContaPessoaFisica:

    logou = False
    numContaDigitada = ''
    agenciaContaDigitada = ''

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
        acessaOBanco.SalvarContaAoBanco(self)

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
    
    def BuscarContaNoBD(self, numContaDigitada, agenciaContaDigitada):
        if acessaOBanco.VerificaContaPeloNum(numContaDigitada, agenciaContaDigitada) == None:
            return False
        else:
            return True


    def FazerDeposito(self):
        self.numContaDigitada = input("Informe a conta para depósito: ")
        self.agenciaContaDigitada = input("Informe a agência para depósito: ")
        if self.BuscarContaNoBD(self.numContaDigitada, self.agenciaContaDigitada) == True:
            valor = float(input("Digite o valor que está no envelope: "))
            if valor <= 0:
                print("Valor inválido...")
            else:
                acessaOBanco.EntradaDeDinheiro(valor, self.numContaDigitada, self.agenciaContaDigitada)
                print("Depósito realizado...")
        else:
            print("Contra não encontrada na base de dados...")

    def ValidarSenha(self, numContaEntrada, agenciaContaEntrada, senhaEntrada):
        retorno = False
        if acessaOBanco.VerificaSenha(numContaEntrada, agenciaContaEntrada, senhaEntrada) != None:
            retorno = True
        else:
            retorno = False
        return retorno

    def RetornaSaldo(self, numContaEntrada, agenciaContaEntrada):
        saldo = acessaOBanco.ExibirSaldo(numContaEntrada, agenciaContaEntrada)
        return saldo[0]

    def AcessarConta(self):
        self.numContaDigitada = input("Informe o NÚMERO da SUA conta: ")
        self.agenciaContaDigitada = input("Informe a AGÊNCIA da SUA conta: ")
        if self.BuscarContaNoBD(self.numContaDigitada, self.agenciaContaDigitada) == True:
            senhaEntrada = input("Digite a senha: ")
            if self.ValidarSenha(self.numContaDigitada, self.agenciaContaDigitada, senhaEntrada) == True:
                self.logou = True
            else:
                tentarNovamente = input("Dados inválidos, tentar novamente?'\n [S]im [N]ão: ")
                if tentarNovamente == 'S' or tentarNovamente == 's':
                    self.logou = False
                    self.AcessarConta()
                elif tentarNovamente == 'N' or tentarNovamente == 'n':
                    self.logou = False
                    print("Voltando ao menu...")
                else:
                    print("Opção inválida!")
                    print("Voltando ao menu...")
        else:
            print("AGENCIA E CONTA NÃO ENCONTRADO...")

    def FazerSaque(self):
        if self.logou == True:
            saldoEmConta = self.RetornaSaldo(self.numContaDigitada, self.agenciaContaDigitada)
            print("Seu saldo atual é: ", saldoEmConta)
            valorSaque = float(input("Qual o valor do saque?: "))
            if valorSaque <= 0:
                print("valor inválido...")
            else:
                if (valorSaque + 100) > saldoEmConta:
                    entradaChEspecial = input("Caso realize esse saque você entrará em cheque especial, fazer mesmo assim?\n[S]im, [N]ão: ")
                    if entradaChEspecial == 's' or entradaChEspecial == 'S':
                        print("Aguarde as cédulas sairem na banjeta...")
                        acessaOBanco.RetiradaDeDinheiro(self.numContaDigitada, self.agenciaContaDigitada, valorSaque)
                        print("Saque realizado, seu saque agora é: ", self.RetornaSaldo(self.numContaDigitada, self.agenciaContaDigitada))

                    elif entradaChEspecial == 'n' or entradaChEspecial == 'N':
                        print("Voltando ao menu...")
                    else: 
                        print("Opção inválida\nVoltando ao menu...")
                else:
                    print("Aguarde as cédulas sairem na banjeta...")
                    acessaOBanco.RetiradaDeDinheiro(self.numContaDigitada, self.agenciaContaDigitada, valorSaque)
                    print("Saque realizado, seu saque agora é: ", self.RetornaSaldo(self.numContaDigitada, self.agenciaContaDigitada))
        else:
            self.AcessarConta()
            self.FazerSaque()

    def DeletarConta(self):
        if self.logou == True:
            senha = input("Entre com a senha novamente: ")
            acessaOBanco.DeletarConta(self.numContaDigitada, self.agenciaContaDigitada, senha)
            print("Conta Deletada...")
        else:
            self.AcessarConta()
            senha = input("Entre com a senha novamente: ")
            acessaOBanco.DeletarConta(self.numContaDigitada, self.agenciaContaDigitada, senha)
            print("Conta Deletada.")
    
    def FazerTransferencia(self):
        if self.logou == True:
            numContaTransf = input("Informe o NÚMERO da conta que deseja transferir: ")
            agenciaContaTransf = input("Informe a AGENCIA da conta que deseja transferir: ")
            if self.BuscarContaNoBD(numContaTransf, agenciaContaTransf) == True:
                valorTransf = int(input("Informe o VALOR que deseja transferir: "))
                senhaDigitada = input("Entre com a senha da sua conta: ")
                acessaOBanco.TransferenciaEntreContas(valorTransf, self.numContaDigitada, self.agenciaContaDigitada, senhaDigitada, numContaTransf, agenciaContaTransf)
                print("Transferência realizada com sucesso!")
                if valorTransf <= 0:
                    print("Valor inválido...")
                elif valorTransf > int(self.RetornaSaldo(self.numContaDigitada, self.agenciaContaDigitada)):
                    entradaChEspecial = input("Caso realize essa tranferência você entrará no cheque especial, continuar?\n[S]im [N]ão")
                    if(entradaChEspecial == 's' or entradaChEspecial == 'S'):
                        senhaDigitada = input("Entre com a senha da sua conta: ")
                        acessaOBanco.TransferenciaEntreContas(valorTransf, self.numContaDigitada, self.agenciaContaDigitada, senhaDigitada, numContaTransf, agenciaContaTransf)
                        print("Transferência realizada com sucesso!")

                    elif(entradaChEspecial == 'n' or entradaChEspecial == 'N'):
                        print("Voltando ao menu...")
                    else:
                        print("Opção inválida...")
            else:
                print("Conjunto de número da conta e agência não encontrado\nVoltando ao menu...")
        else:
            self.AcessarConta()
            self.FazerTransferencia()

    def __repr__(self):
        return str(self.__dict__)
