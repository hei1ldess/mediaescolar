nome = input('Qual é a materia que você deseja calcular a media de nota? ')
media = float(input('Qual a média  que sua escola adota? '))
option = input ('A sua escola é Bimestral,Trismestral ou Semestral? ')
option = option.lower()
if option == 'bimestral': 
    nota1 = float(input('Nota do seu primeiro bimestre: '))
    nota2 = float(input('Nota do seu segundo bimestre: '))
    nota3 = float(input('Nota do seu terceiro bimestre: '))
    nota4 = float(input('Nota do seu quarto bimestre: '))
    mdia1 = (nota1 + nota2 + nota3 + nota4) / 4
    if mdia1 < media:
     print(f"Sua média em {nome} é {mdia1}, portanto você não está na média.")
    if mdia1 >= media:
     print(f"Sua média em {nome} é {mdia1}, portanto você está na média.")
if option == "trimestral":
    nota5 = float(input('Nota do seu primeiro trimestre: '))
    nota6 = float(input('Nota do seu segundo trimestre: '))
    nota7 = float(input('Nota do seu terceiro trimestre: '))
    mdia2 = (nota5+nota6+nota7)/3
    if mdia2 < media:
     print(f"Sua media em {nome} é {mdia2}, portanto você não está na média.")
    elif mdia2 >= media:
     print(f"Sua media em {nome} é {mdia2}, portanto você está na média.")
if option == "semestral":
    nota8 = float(input('Nota do seu primeiro semestre: '))
    nota9 = float(input('Nota do seu segundo semestre: '))
    mdia3 = (nota8+nota9)/2
    if mdia3 < media:
     print(f"Sua media em {nome} é {mdia3}, portanto você não está na média.")
    elif mdia3 >= media:
     print(f"Sua media em {nome} é {mdia3}, portanto você está na média.")







