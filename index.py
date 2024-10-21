class Pessoa:
    def __init__(self, nome, equipe, area):
       self.nome = nome
       self.equipe = equipe
       self.area = area

pessoas = [
    Pessoa(nome='Alice', equipe='Desenvolvimento', area='Tecnologia'),
    Pessoa(nome='Bob', equipe='Desenvolvimento', area='Tecnologia'),
    Pessoa(nome='Carol', equipe='Marketing', area='Comunicação'),
    Pessoa(nome='David', equipe='Marketing', area='Comunicação'),
    Pessoa(nome='Eve', equipe='Desing', area='Tecnologia')
]

#regras
def regraGeral():
   for pessoa in pessoas:
      if pessoa.nome and (pessoa.equipe == 'Desenvolvimento' or pessoa.equipe == 'Desing'):
         print(f'\t{pessoa.nome} area de {pessoa.area}')
      else:
         print(f'\t{pessoa.nome} area da {pessoa.area}')

def areaTecnologia():
   for pessoa in pessoas: 
      if pessoa.nome and pessoa.area == 'Tecnologia':
         print(f'\t{pessoa.nome} é {pessoa.area}')

def areaEspecifica():
   for pessoa in pessoas:
      if pessoa.nome == 'Carol':
         print(f'\t{pessoa.nome} trabalha com {pessoa.area}')

print('\n\t1.Lista a area de tecnologia\n')
areaTecnologia()
print('=====================================')

print('\t2.Carol e da área de comunicação?\n')
areaEspecifica()
print('=====================================')

print('\t3.Lista das Pessoas\n')
regraGeral()
print('\n')