
class Student:
    """
    classe estudante, é o molde pelo qual conseguiremos instanciar novos alunos.
    """
    def __init__(self, name: str, age: int, student_id: int):
        # coloquei tudo em uma linha, não perde a elegancia e funciona.
        self.name, self.age, self.student_id = name, age, student_id       
    
    def __str__(self):
        """
        metodo magico str, ele faz a magica de imprimir na tela do usuario o nome e a idade do aluno.
        Exemplo: print(s1)
        Saida: 'Name: Ruan Sales Age: 19'
        Sem esse método o print() exibiria : <__main__.Student object at 0x000001DE0A97FE10> que é o tipo de s1 e 
        também o endereço de memoria que esse dado esta alocado.
        """
        return f'Name: {self.name}\nAge: {self.age}\n'

# essa instrução faz com que o codigo abaixo so rode SE o arquivo executado for esse(model.py)
if __name__ == "__main__":
    s1 = Student("Ruan Sales", 19, 10)

    print(s1)


