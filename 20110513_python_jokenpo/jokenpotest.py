import unittest

from jokenpo import jokenpo

class TestJokenpo(unittest.TestCase):
    def test_pedra_contra_papel_deve_retornar_papel_vencedor(self):
      self.assertEqual('papel', jokenpo('pedra','papel'))      

    def test_papel_contra_pedra_deve_retornar_papel_vencedor(self):
      self.assertEqual('papel', jokenpo('papel','pedra'))      

    def test_tesoura_contra_papel_deve_retornar_tesoura_vencedor(self):
      self.assertEqual('tesoura', jokenpo('papel','tesoura'))      
      
    def test_tesoura_contra_pedra_deve_retornar_pedra_vencedor(self):
      self.assertEqual('pedra', jokenpo('pedra','tesoura')) 
      
    def test_pedra_contra_pedra_deve_retornar_pedra_vencedor(self):
       self.assertEqual('pedra', jokenpo('pedra','pedra'))
       
    def test_papel_contra_papel_deve_retornar_papel_vencedor(self):
       self.assertEqual('papel', jokenpo('papel','papel'))  
    
    def test_tesoura_contra_tesoura_deve_retornar_tesoura_vencedor(self):
       self.assertEqual('tesoura', jokenpo('tesoura','tesoura'))


unittest.main()
