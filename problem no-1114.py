password = 2002
while True:
    A = int(input())
    if A != password:
        print("Senha Invalida")
    elif A== password:
        print("Acesso Permitido")
        break