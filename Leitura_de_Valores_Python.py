#Par e Ímpar
positivo = 0
negativo = 0
par = 0
impar = 0

for elemento in range(0,5):
  valor = float(input()) #-5
  if valor<0:
    newvalor = -(valor)
  else: 
    newvalor = valor
  
  if valor<0:
    negativo += 1
  elif valor>0:
    positivo += 1
    
  if newvalor%2==0:
    par += 1
  else:
    impar += 1

print(f"{par} valor(es) Par(es) \n{impar} valor(es) Impar(es) \n{positivo} valor(es) Positivo(s) \n{negativo} Valor(es) Negativo(s)")
