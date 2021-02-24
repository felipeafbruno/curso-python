pessoa = {'nome': 'Felipe', 'idade': 26, 'cursos': ['Python', 'React', 'Java', 'PHP', 'JavaScript']}
print(len(pessoa))
print(pessoa)
print(pessoa['nome'])
print(pessoa['cursos'][1])
print(pessoa.keys()) # retorna as chaves contidas no dicionário
print(pessoa.values()) # restorna os valores representados pelas chaves
print(pessoa.items()) # retorna cada item chave/valor do dicionário 
print(pessoa.get('nome')) # outra maneira de obter um valor da do dicionário utilizando o método get() print(pessoa.get('nome'))
print(pessoa.get('tags', [])) # obter 'tag' da lista caso não existe retornar um valor padrão

pessoa['idade'] = 27
pessoa['cursos'].append('Angular')
print(pessoa)
print(pessoa.pop('idade')) # remove o valor e retorna o valor removido
print(pessoa)
pessoa.update({'idade': 27, 'sexo': 'M'})
print(pessoa)