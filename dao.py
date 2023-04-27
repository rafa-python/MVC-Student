import json
from prettytable import PrettyTable


class DaoJson:
    """
    Classe responsavel por manipular o arquivo json que nessa aplicação faz o papel do banco de dados.
    """

    # métodos de classe são bastante uteis.
    @classmethod
    def func_get_all(cls):
        """
        Esse método tem por objetivo acessar o arquivo json e retornar todos os dados.
        """
        """
        O try/except é muito usado quando algum erro inesperado pode ocorrer em seu codido.
        Uma tradução seria tente/try, se houver uma exceção/except(erro) faça isso.
        Ele tenta(try) abrir o arquivo 'students.json' no modo de leitura('r')
        Se ele conseguir abrir o arquivo sem nenhum erro ele não executa o codigo abaixo de except, ou seja, 
        ele nao retorna uma lista vazia.
        """
        try:
            with open("students.json", "r") as arq:
                students = json.load(arq)
            
            
            arq.close() # é muito importante fechar o arquivo com a instrução .close()
            return students
        except:
            return []

    @classmethod # isso se chama decorador/decorator, existem varios na linguagem python
    def func_write(cls, students):
        """
        Essa função escreve no nosso arquivo json, note que o modo de abertura do arquivo é o 'w' 
        que é para escrever em arquivos.
        """
        with open("students.json", "w") as arq:
            # json.dump() altera o arquivo json e também fecha ele dispensando o uso do .close()
            # note o indent=4, serve para identar oque for escrito no json.
            json.dump(students, arq, indent=4)

    @classmethod
    def func_read_students(cls):
        """
        Essa função retorna uma tabela elegante dos alunos cadastrados.
        essa lib 'PrettyTable é uma delicia e também é muito facil de usar.
        """
        students = DaoJson.func_get_all()
        table = PrettyTable() # cria a tabela 
        table.field_names = ["ID", "NOME", "IDADE"] # define o nome dos campos/cabeçalhos
        # aqui com esse for eu monto minha tabela.
        for i in students:
            table.add_row([i["student_id"], i["name"], i["age"]]) 

        return table # retorno a tabela pronta para exibição.

    @classmethod
    def func_dao_update(cls, student_id, name, age):
        """
        Esse método atualiza um determinado aluno pelo seu id.
        """
        students = DaoJson.func_get_all()
        update = False
        for student in students:
            if str(student["student_id"]) == student_id:
                student["name"] = name
                student["age"] = age
                update = True
                break

        if update:
            DaoJson.func_write(students)
            return True
        else:
            return False


if __name__ == "__main__":
    print(DaoJson.func_read_students())
