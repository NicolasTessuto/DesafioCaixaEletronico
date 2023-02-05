import contaBancaria

class MenuPrincipal:
    def __init__(self):
        self.opcUser = 0
    
    def Menu(self, opcUser):
        while opcUser != 6:
            try:
                opcUser = input("\nEntre com o que deseja:\n[1] - Criar conta\n[2] - Fazer um depósito" +
                "\n[3] - Fazer saque\n[4] - Fazer transferência \n[5] - Excluir conta \n[6] - Sair do sistema\n\n")
                opcUser = int(opcUser)
                match opcUser:
                    case 0:
                        conta.Dados()
                    case 1:
                        conta.CriarConta()
                        conta.ExibirContaComSaldo()
                    case 2:
                        conta.FazerDeposito()
                    case 3:
                        conta.FazerSaque()
                    case 4:
                        conta.FazerTransferencia()
                    case 5:
                        conta.DeletarConta()
                    case 6:
                        print("Saindo....")

            except ValueError:
                print("Opção inválida, por favor digite apenas números")

if __name__ == '__main__':
    conta = contaBancaria.ContaPessoaFisica()
    opcUser = 0
    print("🆂 🅼 🅰 🆁 🆃 - 🅱 🅰 🅽 🅺")
    menu = MenuPrincipal()
    menu.Menu(opcUser)
