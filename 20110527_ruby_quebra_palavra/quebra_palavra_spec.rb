require 'rspec'
require './quebra_palavra'

describe 'Testando Word Wrapper' do
  let(:quebra_palavra) { quebra_palavra = QuebraPalavra.new }

  describe "teste com palavras menores que 5 caracteres" do
    it "palavra menor que 5 caracteres nao sera quebrada" do
      quebra_palavra.frase("oi").should be_eql('oi')
    end

    it "a palavra cinco nao deve ser quebrada" do
      quebra_palavra.frase("cinco").should be_eql('cinco')
    end 
  end
  describe "testa frase com 18 caracteres" do
    it "retornar feitos na proxima linha"do
      quebra_palavra.frase("sao palitinhos feitos").should be_eql("sao palitinhos \nfeitos")
    end 
    it "retornar feitos na proxima linha"do
      quebra_palavra.frase("sao palitinhos quebrados").should be_eql("sao palitinhos \nquebrados")
    end 
  end
end
