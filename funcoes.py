def hotel_custo(noites):
  #O hotel custa 140 por noite...
  return 140 * noites

def viajem_aviao_custo(cidade):
  if cidade == 'Madrid':
    return 183
  elif cidade == 'Paris':
    return 220
  elif cidade == 'Londres':
    return 222
  elif cidade == 'Berlim':
    return 475

def alugo_carro_custo(dias):
  custo = 40 * dias
  if dias >= 7:
    return custo - 50
  elif dias >= 3:
    return custo - 20
  else:
    return custo
  
def viajem_custo(cidade, dias, dinheiro_gasto):
  return alugo_carro_custo(dias) + hotel_custo(dias-1) + viajem_aviao_custo(cidade) + dinheiro_gasto

print(viajem_custo('Berlim', 5, 600))