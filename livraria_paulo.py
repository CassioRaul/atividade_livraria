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
    def __init__(self, nome, numero_de_paginas, idioma, tipo):
        self.__nome = nome
        self.__num_de_pag = numero_de_paginas
        self.__idioma = idioma
        self.__tipo = tipo
        self.__estoque_revista = 0
        self.__estoque_livro = 0
        self.limite_de_estoque = 1000
    
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
            print('Digite corretamente')

    @property
    def tipo(self):
        return self.__idioma

    @tipo.setter
    def tipo(self, novo_tipo):
        if type(novo_tipo) == str():
            self.__tipo = novo_tipo
        else:
            print('Digite corretamente')
    
    def adicionar_livros(self, livros):
        if self.limite_de_estoque < 1000:
            if type(livros) == int():
                self.__estoque_livro += livros
            else:
                print('DIGITE NOVAMENTE!')
        else:
            print('VOCÊ NÃO PODE ADICIONAR MAIS LIVROS!')

    def adicionar_revista(self, resvista):
        if self.limite_de_estoque < 1000:
            if type(resvista) == int():
                self.__estoque_revista += resvista
            else:
                print('DIGITE NOVAMENTE!')
        else:
            print('VOCÊ NÃO PODE ADICIONAR MAIS LIVROS!')

livro = Livraria('Harry Potter', 300)
