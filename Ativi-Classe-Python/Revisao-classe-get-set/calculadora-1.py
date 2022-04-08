def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y
def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    return x // y
def raiz(x):
    return (x**1/2)
def expoente(x,y):
    return (x**y)
    

print("**Python Calculator**")

print("\nSelecione o número da opção desejada: \n")
    
option = int(input("\nDigite sua opção (1/2/3/4/5/6): "))
    
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Raiz")
print("6 - Potência")
print("-"*20)
    
if option <= 0 or option > 6:
        
    print("\nOpção inválida!\n")
    exit(0)      

if __name__ == "__main__":
    try:
    
    
        x = float(input("\nDigite o primeiro número: "))    
        y = float(input("\nDigite o segundo número: "))   
        if option == 1:
            print(x, "+", y, "=", soma(x, y))

        elif option == 2:
            print(x, "-", y, "=", subtracao(x, y))

        elif option == 3:
            print(x, "*", y, "=", multiplicacao(x, y))

        elif option == 4:
            print(x, "/", y, "=", divisao(x, y))          
        elif option == 5:
            print(x, "=" , raiz(x))
        elif option == 6:
            print(x, "**", y, "=", expoente(x, y))
        
    except Exception as e:
        print(str(e))
