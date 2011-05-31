class QuebraPalavra
 def frase (palavra)
   if palavra.size > 18
     primeira_parte = palavra[0..14]
     segunda_parte = palavra[15..-1]
     primeira_parte + "\n" + segunda_parte
   else
     palavra
   end
 end
end