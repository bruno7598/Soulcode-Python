from modules.aluno import Aluno
from modules.pessoa import Pessoa
from modules.aluno_matematica import Aluno_matematica
from modules.aluno_portugues import Aluno_portugues
from modules.funcionario import Funcionario


if __name__ == "__main__":
    
    
    
    while True:
        
        selecao = input("1 - CONSULTAR DADOS ALUNO PORTUGUES \n"
                        "2 - CONSULTAR DADOS ALUNO MATEMATICA \n"
                        "3 - CONSULTAR DADOS FUNCIONARIO \n"
                        "4 - CONSULTAR DADOS DOS ALUNOS \n"
                        "5 - CONSULTAR DADOS DE PESSOAS \n"
                        "6 - ENCERRAR \n"
                        " Faça sua escolha: ")    
        
        
            
        if selecao == '1':
            
            
            
            aluno =  Aluno_portugues()
            aluno.nome = ['Bruno', 'Alberto', 'Cecilia', 'Fernanda', 'Alexandra']
            aluno.rg = [545456567, 2342445435, 324536435, 2344545, 325346456]
            aluno.endereco = ['Rua A', 'Rua B', 'Rua C', 'Rua D', 'Rua E']
            aluno.contato = [98850349, 958934034, 893595496, 394955490, 349054956]
            
            
            
            print("=-"*30)
            aluno.print_matricula()
            aluno.print_nota_portugues()
            aluno.print_indentidade()
            print("=-"*30)
         
        
            
        if selecao == '2':
                
            
            aluno =  Aluno_matematica()
            aluno.nome = ['Bruno', 'Alberto', 'Cecilia', 'Fernanda', 'Alexandra']
            aluno.rg = [545456567, 2342445435, 324536435, 2344545, 325346456]
            aluno.endereco = ['Rua A', 'Rua B', 'Rua C', 'Rua D', 'Rua E']
            aluno.contato = [98850349, 958934034, 893595496, 394955490, 349054956]
            
    
            print("=-"*30)
            aluno.print_matricula()
            aluno.print_nota_matematica()
            aluno.print_indentidade()
            print("=-"*30)
        
        
            
        if selecao == '3':
            
            
            funcionario = Funcionario()
            funcionario.nome = ['Felipe', 'Gerson', 'Enzo', 'Azagal', 'Juliano']
            funcionario.rg = [324542354,123424235,123423565,6457567,6857868]
            funcionario.endereco = ['Rua z', 'Rua x', 'Rua y', 'Rua h', 'Rua j']
            funcionario.contato = [9034903, 95405950, 59345958, 54305949,6485498]

            print("=-"*30)
            funcionario.print_id_funcionario()
            funcionario.print_indentidade()
            print("=-"*30)
            
        if selecao == '4':
            
            
            pessoa = Pessoa()
            pessoa.nome = ['Felipe', 'Gerson', 'Enzo', 'Azagal', 'Juliano']
            pessoa.rg = [324542354,123424235,123423565,6457567,6857868]
            pessoa.endereco = ['Rua z', 'Rua x', 'Rua y', 'Rua h', 'Rua j']
            pessoa.contato = [9034903, 95405950, 59345958, 54305949,6485498]
            
            print("=-"*30)
            pessoa.print_indentidade()
            print("=-"*30)
            
        if selecao == '5':
            
            alunos = Aluno()
            alunos.nome = ['Bruno', 'Alberto', 'Cecilia', 'Fernanda', 'Alexandra']
            alunos.rg = [545456567, 2342445435, 324536435, 2344545, 325346456]
            alunos.endereco = ['Rua A', 'Rua B', 'Rua C', 'Rua D', 'Rua E']
            alunos.contato = [98850349, 958934034, 893595496, 394955490, 349054956]
            
            print("=-"*30)
            alunos.print_matricula()
            alunos.print_indentidade()
            print("=-"*30)
            
        if selecao == '6':
            
            break