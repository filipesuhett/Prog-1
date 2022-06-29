def f_armstrong(n):
#n = numero
#s = soma
#i = tamanho do numero
  
  s = 0
  for i in str(n):
    s += int(i)**(len(str(n)))
  return s
	
def f_verificaArmstrong(n):
#n = numero
  
  return n == f_armstrong(n)

def f_tam(n):
#n = numero
#t = tamanho do numero

  t = 0
  while(n > 0):
    n = n // 10
    t += 1
  return t
  
def f_inverte(n):
#n = numero
#a = numero invertido
#r = resto
#t = tamanho
  
  t = f_tam(n)-1
  a = 0
  while (n > 0):
    r = n % 10
    a += r * 10 ** t
    n = n // 10
    t = t -1
  return a

def f_capicua(n):
#n = numero
  
  return n == f_inverte(n)

def f_primo(n):
#p = primo
#n = numero

  p = 0

  for i in range(1, (n + 1)):
    if (n % i == 0):
      p += 1

  if (p == 2):
    return True
  else:
    return False
  

def f_perfeito(n):
#n = numero
#s = soma
#i = valor

  s = 0
  for i in range(1, n):
    if (n % i == 0):
      s += i
  if (s == n):
    return True
  else:
    return False

def f_decToBin(n):
#n = numero
#bin = numero em forma binaria
#r = resto  
  
  bin = ""
  
  while (n > 0):
    r = n % 2
    bin += str(r)
    n = n // 2
  bin = str(bin)
  bin = bin[::-1]
  return bin

def f_decToHex(n):
#n = numero
#hex = numero em forma hexadecimal
#r = resto
#he = resto acima de 10

  hex = ""
  he = "ABCDEF"

  while (n > 0):
    r = n % 16
    if (r < 10):
      hex += str(r)
    else:
      hex += he[r - 10]
    n = n // 16
  hex = str(hex)
  hex = hex[::-1]
  return hex

def f_mdc(n,b):
#n = numero
#b = inverso
#r = resto

  while (b!= 0):
    r = n % b
    n = b
    b = r

  return n
    
def f_contPrimo(a,b):  
  
  c = 0
  if (a > b):
    x = b
    b = a
    a = x
  for i in range(a,b+1):
    if (f_primo(i)):
      c += 1
  return c

def f_verificaOpcao(m):
#m = operação  
  return m > 0 and m < 12
