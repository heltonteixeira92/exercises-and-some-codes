*PRINCIPIOS SOLID*

SOLID é um acronico


Resposábilidade única

Antes:

```
class SistemaCadastral:

    def cadastrar(self, nome: str, idade: int) -> None:
        if isinstance(nome, str) and isinstance(idade, int):
            print('acessando o banco de dados...')
            print('Cadastrando o Usuário {}, Idade {}'.format(nome, idade))
        else:
            print('dados inválidos!') 
```

Depois:


```
class SistemaCadastral:

    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__verficar_dados(nome, idade):
            self.__armazenar_usuario(nome, idade)
        else:
            self.__indicar_erro()

    def __verficar_dados(self, nome: str, idade: int) -> bool:
        if isinstance(nome, str) and isinstance(idade, int):
            return True
        else:
            return False

    def __armazenar_usuario(self, nome: str, idade: int) -> None:
        print('acessando o banco de dados...')
        print('Cadastrando o Usuário {}, Idade {}'.format(nome, idade))

    def __indicar_erro(self) -> None:
        print('dados inválidos!')


sistema = SistemaCadastral()
sistema.cadastrar('Helton', 30)
```


Os métodos privados não sairam do contexto da classe, 
o objeto só terá acesso ao método cadastrar

O - Princípio Aberto / Fechado

Motivação: Entradas diferentes geram ações diferentes!

Antes:

```
class Circo:

    def apresentar(self, tipo):
        if tipo == 1:
            self.apresentar_malabarista()
        if tipo == 2:
            self.apresentar_palhaco()

    def apresentar_malabarista(self):
        print('Malabarista apresentando seu show')

    def apresentar_palhaco(self):
        print('Palhaço apresentando seu show')


circo = Circo()
```

Depois:

```
class Circo:

    def apresentar(self, apresentador: any):
        apresentador.apresentar_show()


class Malabarista:

    def apresentar_show(self):
        print('Malabarista apresentando seu show')


class Palhaco:
    def apresentar_show(self):
        print('Palhaço apresentando seu show')
        
class Domador:
    
    def apresentar_show(self):
        print('Domador apresentando seu show')
       
 
circo = Circo()
malabarista = Malabarista()
palhaco = Palhaco()
domador = Domador()

circo.apresentar(malabarista)  # isso é uma associação de classes
circo.apresentar(domador)

```
As classes acabem tendo o método apresentar_show() em comum

Ele fica fechado para alteração, mas aberto para extensão
