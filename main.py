import contaBancaria

opcUser = 0
print("Bem-vindo ao Banco!")

while opcUser != 6:

    conta = contaBancaria.ContaPessoaFisica()

    opcUser = input("\nEntre com o que deseja:\n[1] - Criar conta\n[2] - Fazer um depósito" +
    "\n[3] - Fazer uma saque\n[4] - Fazer transferência \n[5] - Excluir conta \n[6] - Sair do sistema\n\n")
    
    opcUser = int(opcUser)

    match opcUser:
        case 1:
            conta.CriarConta()
            conta.ExibirContaComSaldo()
        case 2:
            conta.FazerDeposito()
        case 3:
            if conta.logou != True:
                conta.AcessarConta()
                conta.FazerSaque()
            