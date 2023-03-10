from os import system
from getpass import getpass
from time import sleep

class tela_de_login:
    def Menu_login(self):

        print('''         Sistema Conectado!
        [1] Lista de usuarios
        [2] Deletar um usuario
        [3] Voltar ao menu principal''')
        data = input('O que deseja fazer? ')
        if data == '1':
            i = 1

            consulta = self.mostrar_lista()

            for x in range(len(consulta)):
                print(f'[{i}] {consulta[x]}')
                i = i+1
            else:
                input('Digite qualquer coisa.')
                self.Menu_login()
        if data == '2':
            i = input('Qual usuário deseja deletar? ')
            self.excluir_user(i)
   
    def Menu_principal(self):
        system('cls')
        print('''       Menu principal
        [1] Fazer Login
        [2] Fazer Cadastro
        [3] Sair''')
        acao = input('O que deseja fazer? ')
        return(acao)
    
    def Login_de_usuario(self):
        system('cls')
        login_user=input('Nome: ')
        senha_user=input('Senha: ')
        return(login_user,senha_user)
    
    def busca_de_usuario(self, login_user, senha_user):
        users = []
        try:
            with open('logins.txt', 'r+', encoding='latin-1', newline='') as arquivo:
                for linha in arquivo:
                    linha=linha.strip(',')
                    users.append(linha.split())
                for user in users:
                    nome = user [0]
                    senha = user [1]
                    if login_user == nome and senha_user == senha:
                        return True
        except Exception as error:
            return False

    def teste_letras(self, senha_user):
        if any(i.isupper() for i in senha_user):
            if any(p.islower() for p in senha_user):
                return True
            return False
        return False
    
    def teste_senha(self, login_user, senha_user):
        test1 = self.teste_letras(senha_user)
        test2 = (senha_user.isalpha())
        print(test1)
        print(test2)
        
        if login_user == senha_user:
            return False
        elif test1 == True:
            print(test1)
            if test2 == False:
                print(test2)
                if 8 <= len(senha_user):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def mostrar_lista(self):
        usuarios = []
        try:
            with open('logins.txt', 'r', encoding='latin-1', newline='') as arquivo:
                for linha in arquivo:
                    usuarios.append(linha.split(' ')[0])
                return usuarios
        except Exception as error:
            return ''

    def excluir_user(self, i):
        try:
            with open('logins.txt', 'r', ) as arquivo:
                lines = arquivo.readlines()
                ptr = 1
                with open('logins.txt', 'w', ) as arch:
                    for line in lines:
                        if ptr != int(i):
                            arch.write(line)
                        ptr += 1
            print('Usuário ',i,' deletado')
            input('Digite qualquer coisa.')
            self.Menu_login()
        except Exception as error:
            self.Menu_login()
   
    def run(self):
        acao = self.Menu_principal()
        #Login
        if acao == '1':
            login_user, senha_user = self.Login_de_usuario()
            valid = self.busca_de_usuario(login_user, senha_user)
            if valid == True:
                consulta = []
                system('cls')
                print('Login realizado com sucesso!')
                print('Carregando.')
                sleep(0.5)
                system('cls')
                self.Menu_login()
            else:
                print('Você deve ter digitado um login ou senha incorreto.')
                sleep(10)
           
        #Cadastro
        elif acao == '2':
            login_user, senha_user = self.Login_de_usuario()
            test_final = self.teste_senha(login_user, senha_user)
            valid = self.busca_de_usuario(login_user, senha_user)
            #Verifica se ja existe usuario
            if valid == True:
                print('Usuário ja existe!')
           
            #Verifica se a senha é valida
            elif  test_final == False:
                print('''Sua senha deve ser diferente do login, conter mais de 8 caracteres, letras maiusculas, minusculas e numeros.''')
                menu = input('Digite qualquer coisa para voltar ao menu.')
                self.Menu_principal()
            #Salva o login
            else:
                with open('logins.txt', 'a+', encoding=('latin-1'), newline='') as arquivo:
                    arquivo.writelines(f'{login_user} {senha_user}\n')
                    print('Cadastro Aprovado')
           
        #Sair
        else:
            print('Bye')
            exit()

while True:
    tela_de_login().run()
