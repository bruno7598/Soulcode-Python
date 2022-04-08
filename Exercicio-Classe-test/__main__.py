from modules.test import Test


if __name__ == "__main__":
    
    lista = ['Alberto', 'Fernando', 'Robson', 'Juliana']
    
    const = Test(pessoas=None, lugares=None, casas=None)
    const.add_pessoas('Alberto')
    
    print(const.get_pessoas())