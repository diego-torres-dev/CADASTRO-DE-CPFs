# Solicita que o usuário digite seu CPF
cpf = input("Digite seu CPF:\n")

# Limpeza do CPF
cpf = cpf.strip().replace(".", "").replace("-", "")

# Verifica se o usuário digitou um CPF válido
if cpf.isnumeric() and len(cpf) == 11:
    print("O CPF digitado é válido.")
elif cpf.isnumeric() and not(len(cpf) == 11):
    print("CPF inválido. O CPF deve possuir 11 dígitos.")
elif not cpf.isnumeric() and len(cpf) == 11:
    print("CPF inválido. O CPF deve possuir apenas números.")
else:
    print("CPF inválido. O CPF deve possuir 11 caracteres numéricos.")
    