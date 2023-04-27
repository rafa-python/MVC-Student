from model import Student
from dao import DaoJson


class ControllerStudent:
    """
    Essa classe é onde fica a logica e onde tem os metodos do CRUD,
    CREATE, READ, UPDATE, DELETE, essas são as 4 operações que todo programador deve dominar.
    """
    @classmethod
    def func_controll_create(cls):
        """
        metodo responsavel por criar novo aluno.
        """
        print("====================================================")
        name = input("Informe o nome do aluno: ")
        age = int(input("Informe a idade do aluno: "))
        students = DaoJson.func_get_all()
        student_id = (
            max([student["student_id"] for student in students]) + 1 if students else 1
        ) # função max retorna o maior id e soma + 1  
        student = Student(name, age, student_id)
        students.append(
            {"name": student.name, "age": student.age, "student_id": student.student_id}
        )
        DaoJson.func_write(students)

    @classmethod
    def func_controll_display_table(cls):
        """
        Metodo responsavel por retornar uma tabela elegante,
        eu poderia simplesmente chamar de dao diretamente em view, mas segundo o MVC é uma boa praticar usar a camada
        controller para servir de intermedium entre model, dao e view.
        """
        return DaoJson.func_read_students()

    @classmethod
    def func_check_if_id_exists(cls):
        """
        Verifica se o id existe e retorna.
        """        
        id = input("Informe o ID do aluno: ")
        students = DaoJson.func_get_all()
        for i in students:
            if i["student_id"] == int(id):
                return id

    @classmethod
    def func_controll_update(cls, student_id):
        """
        Atualiza os dados no json com base no ID escolhido
        """
        if student_id:
            name = input("Informe o nome: ")
            age = input("Informe a idade: ")
            DaoJson.func_dao_update(student_id, name, age)
            return "Aluno atualizado com sucesso"
        else:
            return "Aluno nao encontrado"

    @classmethod
    def func_controll_delete(cls, student_id):
        '''
        Delete um registro do json com base no id selecionado.
        '''
        if student_id != None:
            students = DaoJson.func_get_all()
            for position, student in enumerate(students): # a função enumerate é uma delicia.
                if str(student["student_id"]) == str(student_id):
                    del students[position]
                    DaoJson.func_write(students)
                    return "Aluno apagado com sucesso"

        else:
            print("====================================================")
            return "ID não existe\n===================================================="


if __name__ == "__main__":
    pass
