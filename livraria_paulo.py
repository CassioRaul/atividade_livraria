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
        self.__estoque = 0
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
    def tipo(self):
        return self.__idioma

    @tipo.setter
    def tipo(self, novo_tipo):
        if type(novo_tipo) == str():
            self.__tipo = novo_tipo
        else:
            print('DIGITE NOVAMENTE!')
    
    def verificar_estoque(self):
        return f'VOCÊ TEM EM ESTOQUE ENTRE LIVROS E REVISTAS {self.__estoque} EXEMPLARES.'

    def adicionar_livro(self, quant_livros):
        if type(quant_livros) == type(int()):
            if quant_livros < self.__limite_de_estoque:
                self.__estoque += quant_livros
                print(f'VOCÊ ADICIONOU {quant_livros} EM SEU ESTOQUE.')
            else:
                print('VOCÊ NÃO PODE ADICIONAR MAIS LIVROS!')
        else:
            print('DIGITE NOVAMENTE!')

    def __str__(self):
        return f'Seu livro é {self.__nome} tem {self.__num_de_pag} páginas está em {self.__idioma} e é {self.__tipo}'

livro = Livraria('Harry Potter', 300, 'Português', 'Alugado')
print(livro)
print(livro.verificar_estoque())
livro.adicionar_livro(100)
livro.adicionar_livro(3000)
print(livro.verificar_estoque())