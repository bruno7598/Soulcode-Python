from modules.netflix import netflix

if __name__ == "__main__":
    try:
    
        test = netflix("Bruno", "brunomirandamagalhaes@gmail.com", "R$50.00", "118.302.405-98", "06/11/1994")
        print("-="*30)
        a = str(input("Digite o seu nome: "))
        b = str(input("Digite o seu email: "))
        c = input("Digite o seu valor a pagar: ")
        d = input("Digite o seu CPF: ")
        e = input("Digite sua data de nasciment: ")
        test.__init__(a, b, c ,d , e)
        print("-="*30)
    
        print("Seu nome: {} \n"
          "Seu EMAIL: {} \n"
          "O valor a pagar: {} \n"
          "O seu CPF:{} \n"
          "Sua data de nascimento: {} \n".format(test.nome, test.email, test.valor, test.cpf, test.data_nascimento))
    
        
    except Exception as e:
        print(str(e))