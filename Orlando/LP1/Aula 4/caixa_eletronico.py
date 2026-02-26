while True:
    while True:
        valor = int(input('Digite um valor em R$ para saque (múltiplo de 5): '))

        if valor % 5 == 0:
            break
        
        print('Erro: Só trabalhamos com notas múltiplas de 5. Tente novamente.')

    restante = valor
    notas = [200, 100, 50, 20, 10, 5]

    for nota in notas:
        quantidade = restante // nota
        
        if quantidade > 0:
            print(f'{quantidade} nota(s) de R$ {nota}')

        restante = restante % nota

    print("-" * 30)
    while True: 
        opcao = int(input('\nDeseja realizar outro saque? \n1 - Sim \n2 - Não\nEscolha: '))
        
        if opcao == 1 or opcao == 2:
            break 
        print('Opção inválida! Digite apenas 1 para continuar ou 2 para sair.')

    if opcao == 2:
        print('Sistema encerrado')
        break