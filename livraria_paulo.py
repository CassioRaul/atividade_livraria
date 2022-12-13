#Lembrando que:
# snake_case para variáveis, funções e métodos;
# PascalCase para classes;
#============================================================
# Crie um ambiente O.O. completo utilizando classes e métodos:
# Na classe Livraria sub-classes Revista e Livro sabemos que:
# atributos: nome, Número de páginas, Idioma, Editora, tipo e status
# todos atributos encapsulados fortemente
# métodos para:
# controlar o aluguel dos livros, calculo do aluguel em (07)dias
# controlar a venda dos livros
# OBS: Lembre-se de fazer os GETs e SETs
# OBS: Não esqueça das validações
# OBS: Sempre que acontecer um aluguel ou venda diminuir do estoque.
# OBS: Faça a impressão dos elementos

class Livraria:
    def __init__(self, nome, numero_de_paginas, idioma, editora, tipo):
        self.__nome = nome
        self.__num_de_pag = numero_de_paginas
        self.__idioma = idioma
        self.__editora = editora
        self.__tipo = tipo
        self.__estoque = 0
        self.__estoque_livro = 0
        self.__estoque_revista = 0
        self.__limite_de_estoque = 1000
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        if type(novo_nome) == str():
            self.__nome = novo_nome
        else:
            print('Digite corretamente')
    
    @property
    def num_de_pag(self):
        return self.num_de_pag

    @num_de_pag.setter
    def num_de_pag(self, novo_pag):
        if type(novo_pag) == int():
            self.__num_de_pag = novo_pag
        else:
            print('Digite corretamente')

    @property
    def idioma(self):
        return self.__idioma

    @idioma.setter
    def idioma(self, novo_idioma):
        if type(novo_idioma) == str():
            self.__idioma = novo_idioma
        else:
            print('DIGITE NOVAMENTE!')

    @property
    def editora(self):
        return self.__editora

    @editora.setter
    def editora(self, nova__editora):
        if type(nova__editora) == str():
            self.__editora = nova__editora
        else:
            print('DIGITE NOVAMENTE!')

    @property
    def tipo(self):
        return self.__idioma

    @tipo.setter
    def tipo(self, novo_tipo):
        if type(novo_tipo) == str():
            self.__tipo = novo_tipo
        else:
            print('DIGITE NOVAMENTE!')

    def adicionar_livro(self, quant_livros):
        if type(quant_livros) == type(int()):
            if quant_livros < self.__limite_de_estoque and self.__estoque < self.__limite_de_estoque:
                self.__estoque += quant_livros
                print(f'VOCÊ ADICIONOU {quant_livros} LIVROS EM SEU ESTOQUE.')
            else:
                print('VOCÊ NÃO PODE ADICIONAR MAIS EXAMPLARES!')
        else:
            print('DIGITE NOVAMENTE!')

    def adicionar_revista(self, quant_revista):
        if type(quant_revista) == type(int()):
            if quant_revista < self.__limite_de_estoque and self.__estoque < self.__limite_de_estoque:
                self.__estoque += quant_revista
                print(f'VOCÊ ADICIONOU {quant_revista} REVISTAS EM SEU ESTOQUE.')
            else:
                print('VOCÊ NÃO PODE ADICIONAR MAIS EXAMPLARES!')
        else:
            print('DIGITE NOVAMENTE!')

    def verificar_estoque_livros(self):
        return f'VOCÊ TEM {self.__estoque_livro} LIVROS EM SEU ESTOQUE.'
    
    def verificar_estoque_revistas(self):
        return f'VOCÊ TEM {self.__estoque_revista} REVISTAS EM SEU ESTOQUE.'
    
    def verificar_estoque(self):
        print (f'VOCÊ TEM EM ESTOQUE ENTRE LIVROS E REVISTAS {self.__estoque} EXEMPLARES.')
    
    def aluguel(self):
        if self.__tipo == 'Alugado' or self.__tipo == 'Vendido':
            aluguel = self.__estoque - 1
            print(f'FOI RETIRADO {aluguel} EXEMPLAR DO ESTOQUE.')
        else:
            print('DIGITE NOVAMENTE!')

    def __str__(self):
        return f'Seu livro é {self.__nome} tem {self.__num_de_pag} páginas está em {self.__idioma} e é {self.__tipo}'

class Livro(Livraria):
    def __init__(self, nome, numero_de_paginas, idioma, editora, tipo):
        super().__init__(nome, numero_de_paginas, idioma, editora, tipo)

class Revista(Livraria):
    def __init__(self, nome, numero_de_paginas, idioma, editora, tipo):
        super().__init__(nome, numero_de_paginas, idioma, editora, tipo)

revista = Revista('PLAYBOY', 40, 'Português', 'PAPILO', 'Vendido')
livro = Livro('Harry Potter', 300, 'Português', 'INTRÍSECA', 'Alugado')
print('*'*20)
print(livro)
print('*'*20)
livro.adicionar_livro(100)
print('*'*20)
revista.adicionar_revista(7)
print('*'*20)
livro.adicionar_livro(3)
print('*'*20)
print(livro.verificar_estoque_livros())
revista.aluguel()
livro.aluguel()
livro.verificar_estoque()
print(livro)