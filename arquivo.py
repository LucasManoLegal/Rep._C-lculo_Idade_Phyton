nascimento = 2007
nascimento_do_Joselito = 1980
anoAtual = 2023

def calculoIdade(nascimento, anoAtual):
    idade = anoAtual - nascimento
    return idade
idade = calculoIdade(nascimento, anoAtual)
idade_do_Joselito = calculoIdade(nascimento_do_Joselito, anoAtual)

print(' A idade é ' +str(idade))
print(' A idade do Joselito é ' +str(idade_do_Joselito))