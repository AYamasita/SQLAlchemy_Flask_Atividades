from models import Pessoas

def insere_pessoa(param_nome,param_idade):
    pessoa = Pessoas(nome=param_nome, idade=param_idade)
    pessoa.db_save()
    print(pessoa)

def excluir_pessoa(param_nome):
    pessoa = Pessoas.query.filter_by(nome = param_nome).fist()
    pessoa.db_delete()

def consulta_pessoa(param_nome):
    pessoa = Pessoas.query.all()
    pessoa = Pessoas.query.filter_by(nome=param_nome).first()
    print('A pessoa : {} tem {} anos.' .format(pessoa.nome, pessoa.idade))

def lista_pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)

if __name__ == '__main__':
   # insere_pessoa('Alexandre',46)
   # insere_pessoa('Lidiane', 37)
    lista_pessoas()
    consulta_pessoa('Lidiane')