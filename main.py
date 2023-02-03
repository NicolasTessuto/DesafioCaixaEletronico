import contaBancaria

opcUser = 0
print("Bem-vindo ao Banco!")

while opcUser != 6:

    conta = contaBancaria.ContaPessoaFisica()

    opcUser = input("\nEntre com o que deseja:\n[1] - Criar conta\n[2] - Fazer um depósito" +
    "\n[3] - Fazer saque\n[4] - Fazer transferência \n[5] - Excluir conta \n[6] - Sair do sistema\n\n")
    
    opcUser = int(opcUser)

    match opcUser:
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
            