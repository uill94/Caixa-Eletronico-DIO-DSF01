saldo = 0
valor = 0
cont_saques = 0
extrato = []




def depositar(valor):
    global saldo
    if valor > 0:
        saldo += valor
        print("Você depositou R${} Reais! Seu saldo atualizado é de R${} Reais".format(valor, saldo))
        op1="DEPÓSITO"
        sa1="SALDO"
        extrato.append((op1, valor, sa1, saldo))
    
    else:
        print("Valor inválido! Tente novamente.")

def sacar (valor):
    global saldo
    global cont_saques
  

    if valor <= saldo and valor <= 500:
        saldo -= valor
        print("Voçê sacou R${} Reais! Seu saldo atualizado é de R${} Reais".format(valor, saldo))
        cont_saques += 1
        op2="SAQUE"
        sa2="SALDO"
        extrato.append((op2, valor, sa2, saldo))
    
    elif valor > saldo:
        print("Saldo insuficiente para saque")

while True:
    print("""======MENU_DO_CAIXA_ELETRONICO======
      DIGITE [1] DEPOSITAR
             [2] SACAR 
             [3] EXTRATO """)
    escolha = input("Digite sua operação: ")




    if escolha == "1":
        valor=float(input("Digite o valor a ser depositado: "))
        depositar(valor)



    elif escolha == "2":
        if cont_saques <3:
        
            valor=float(input("Digite o valor a ser sacado: "))
            sacar(valor)

        else: 
            print("Limite de saques diários atingido! Volte amanhã.")


    elif escolha == "3":
        for extrat in extrato:
            print(extrat)

    elif escolha == "4":
        break
    
    
    else: 
        print("Opção Invalida. Tente novamente")