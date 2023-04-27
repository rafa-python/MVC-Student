from controller import ControllerStudent


class ViewStudent:
    """
    classe responsavel pela exibição e iteração com o usuario
    """
    @classmethod
    def func_view_return_menu(cls):
        """
        Exibe o menu e também captura a opção desejada do usuario.
        """
        print("====================================================")
        response = input("1 para voltar ao menu e 2 para sair: ")
        if response == "1":
            ViewStudent.func_view_menu_option(ViewStudent.func_view_menu())
        elif response == "2":
            print("====================================================")
            print("Encerrando programa.")
            print("====================================================")
            exit()
        else:
            print("====================================================")
            print("Opção invalida, retornando ao menu...")
            print("====================================================")
            ViewStudent.func_view_menu_option(ViewStudent.func_view_menu())

    @classmethod
    def func_view_menu(cls):
        # menu
        print("====================================================")
        print("Bem-vindo ao sistema de gerenciamento de alunos!")
        print("====================================================")
        print("1 - Cadastrar novo aluno.")
        print("2 - Exibir lista de alunos ja cadastrados.")
        print("3 - Editar aluno ja cadastrado.")
        print("4 - Remover aluno do sistema.")
        print("5 - Encerrar programa")
        print("====================================================")
        return int(input("Selecione a opção desejada: "))

    @classmethod
    def func_view_menu_option(cls, option):
        # classe responsavel por direcionar as requisições do usuario  
        if option == 1:
            ControllerStudent.func_controll_create()
            print("====================================================")
            print("Aluno regristrado com sucesso.")
            print("====================================================")
            ViewStudent.func_view_return_menu()

        elif option == 2:
            table = ControllerStudent.func_controll_display_table()
            print(table)
            ViewStudent.func_view_return_menu()

        elif option == 3:
            table = ControllerStudent.func_controll_display_table()
            print(table)
            false_or_id = ControllerStudent.func_check_if_id_exists()
            response = ControllerStudent.func_controll_update(false_or_id)
            print(response)
            ViewStudent.func_view_return_menu()

        elif option == 4:
            table = ControllerStudent.func_controll_display_table()
            print(table)
            false_or_id = ControllerStudent.func_check_if_id_exists()
            response = ControllerStudent.func_controll_delete(false_or_id)
            print(response)
            ViewStudent.func_view_return_menu()

        elif option == 5:
            print("====================================================")
            print("Encerrando programa!")
            print("====================================================")
            exit()

        else:
            print("====================================================")
            print("Opção invalida, retornando ao menu")
            print("====================================================")
            ViewStudent.func_view_return_menu()


if __name__ == "__main__":
    ViewStudent.func_view_menu_option(ViewStudent.func_view_menu())
