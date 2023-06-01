from numpy import array
print('-' * 50)
print('Jogo da Velha')
print('-' * 50)

mapeamento = {0: ' ', 1: 'X', 2: 'O'}

tabela = array([[0, 0 , 0],
                [0, 0 , 0],
                [0, 0 , 0]])
while True:
    #Vez do X
    #Tabela do jogo
    print('  0  1  2')
    for i, row in enumerate(tabela):
        print(f'{i} {mapeamento[row[0]]}  {mapeamento[row[1]]}  {mapeamento[row[2]]}')
    print('\n')
    #Entrada de dados do Jogador 
    l = int(input('Escolha uma linha 0, 1 ou 2: '))
    while l not in [0, 1, 2]:
        l = int(input('Informação incorreta, tente novamente: '))
    c = int(input('Escolha uma coluna 0, 1 ou 2: '))
    while c not in [0, 1, 2]:
        c = int(input('Informação incorreta, tente novamente: '))
    print('\n')
    tabela[l][c] = 1
    #Vitoria fazando uma linha horizontal
    if tabela[0][0] * tabela[0][1] * tabela[0][2] == 1 or tabela[1][0] * tabela[1][1] * tabela[1][2] == 1 or tabela[2][0] * tabela[2][1] * tabela[2][2] == 1:
        mapeamento = {0: ' ', 1: '\033[32mX\033[0m', 2: 'O'}
        print('O X GANHOU')
        print('  0  1  2')
        for i, row in enumerate(tabela):
            print(f'{i} {mapeamento[row[0]]}  {mapeamento[row[1]]}  {mapeamento[row[2]]}')
        print('\n')
        break
    #Vitoria fazando uma linha vertical
    elif tabela[0][0] * tabela[1][0] * tabela[2][0] == 1 or tabela[0][1] * tabela[1][1] * tabela[2][1] == 1 or tabela[0][2] * tabela[1][2] * tabela[2][2] == 1:
        mapeamento = {0: ' ', 1: '\033[32mX\033[0m', 2: 'O'}
        print('O X GANHOU') 
        print('  0  1  2')
        for i, row in enumerate(tabela):
            print(f'{i} {mapeamento[row[0]]}  {mapeamento[row[1]]}  {mapeamento[row[2]]}')
        print('\n')
        break
    #Vitoria fazando cruzado
    elif tabela[0][0] * tabela[1][1] * tabela[2][2] == 1 or tabela[0][2] * tabela[1][1] * tabela[2][0] == 1:
        mapeamento = {0: ' ', 1: '\033[32mX\033[0m', 2: 'O'}
        print('O X GANHOU')
        print('  0  1  2')
        for i, row in enumerate(tabela):
            print(f'{i} {mapeamento[row[0]]}  {mapeamento[row[1]]}  {mapeamento[row[2]]}')
        print('\n')
        break
    #Para caso aconteca um empate
    if 0 not in tabela:
        print('Empate')
        print('\n')
        print('  0  1  2')
        for i, row in enumerate(tabela):
            print(f'{i} {mapeamento[row[0]]}  {mapeamento[row[1]]}  {mapeamento[row[2]]}')
        print('\n')
        break
    #Vez do O
    #Tabela do jogo
    print('  0  1  2')
    for i, row in enumerate(tabela):
        print(f'{i} {mapeamento[row[0]]}  {mapeamento[row[1]]}  {mapeamento[row[2]]}')
    print('\n') 
    #Entrada de dados do Jogador 
    l = int(input('Escolha uma linha 0, 1 ou 2: '))
    while l not in [0, 1, 2]:
        l = int(input('Informação incorreta, tente novamente: '))
    c = int(input('Escolha uma coluna 0, 1 ou 2: '))
    while c not in [0, 1, 2]:
        c = int(input('Informação incorreta, tente novamente: '))
    print('\n')
    tabela[l][c] = 2
    #Vitoria fazando uma linha horizontal
    if tabela[0][0] * tabela[0][1] * tabela[0][2] == 8 or tabela[1][0] * tabela[1][1] * tabela[1][2] == 8 or tabela[2][0] * tabela[2][1] * tabela[2][2] == 8:
        mapeamento = {0: ' ', 1: 'X', 2: '\033[32mO\033[0m'}
        print('O O GANHOU')
        print('  0  1  2')
        for i, row in enumerate(tabela):
            print(f'{i} {mapeamento[row[0]]}  {mapeamento[row[1]]}  {mapeamento[row[2]]}')
        print('\n')
        break
    #Vitoria fazando uma linha vertical
    elif tabela[0][0] * tabela[1][0] * tabela[2][0] == 8 or tabela[0][1] * tabela[1][1] * tabela[2][1] == 8 or tabela[0][2] * tabela[1][2] * tabela[2][2] == 8:
        mapeamento = {0: ' ', 1: 'X', 2: '\033[32mO\033[0m'}
        print('O O GANHOU') 
        print('  0  1  2')
        for i, row in enumerate(tabela):
            print(f'{i} {mapeamento[row[0]]}  {mapeamento[row[1]]}  {mapeamento[row[2]]}')
        print('\n')
        break
    #Vitoria fazando cruzado
    elif tabela[0][0] * tabela[1][1] * tabela[2][2] == 8 or tabela[0][2] * tabela[1][1] * tabela[2][0] == 8:
        mapeamento = {0: ' ', 1: 'X', 2: '\033[32mO\033[0m'}
        print('O O GANHOU')
        print('  0  1  2')
        for i, row in enumerate(tabela):
            print(f'{i} {mapeamento[row[0]]}  {mapeamento[row[1]]}  {mapeamento[row[2]]}')
        print('\n')
        break
    #Para caso aconteca um empate
    if 0 not in tabela:
        print('EMPATE')
        print('\n')
        print('  0  1  2')
        for i, row in enumerate(tabela):
            print(f'{i} {mapeamento[row[0]]}  {mapeamento[row[1]]}  {mapeamento[row[2]]}')
        print('\n')
        print('\n')
        break
