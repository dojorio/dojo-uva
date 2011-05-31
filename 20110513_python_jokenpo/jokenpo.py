def jokenpo(jogada1,jogada2):
  dic = {
     'tesoura pedra':'pedra'
     'tesoura '}
  return dic[jogada1+' '+jogada2]
  
  if jogada1 == 'tesoura':
    if jogada2 == 'pedra':
      return 'pedra'
  elif jogada1 == 'papel' and jogada2 == 'tesoura':
    return 'tesoura'
    
  elif jogada1 == 'pedra' and jogada2 == 'tesoura':
      return 'pedra'
      
  elif jogada1 ==  jogada2:
    return jogada1
    
  return 'papel'
    
