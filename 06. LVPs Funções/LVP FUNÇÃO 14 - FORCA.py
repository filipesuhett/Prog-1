def f_vefle(le,seg,forc):
  seg2 = ""
  for x in range(len(seg)):
    if (seg[x] == le):
      seg2 += le
    else:
      seg2 += forc[x]
  return seg2

def f_forc(se):
  sef = ""
  for x in range(len(se)):
    sef += "_"
  return sef

def f_comp(a,b):
  if (a == b):
    return True
  else:
    return False

def f_prin(d):
  for x in range(len(d)):
    print(d[x],end=" ")
  print()

def f_rep(let,letj):
  for x in range(len(letj)):
    if(let == letj[x]):
      return True
  return False  

def main():
  erra = ""
  letj = ""
  cont = 0
  jog = 0
  gan = False
  
  seg = input("Digite a Palavra: ").upper()
  
  print(seg)
  
  forc = f_forc(seg)

  f_prin(forc)

  while(cont < 6 and not gan):
    let = input("").upper()
    while (f_rep(let,letj)):
      let = input("Tente outra letra: ").upper()
    letj += let
    jog += 1
    if (let in seg):
      forc = f_vefle(let,seg,forc)
    else:
      erra += let
      cont += 1
    f_prin(forc)
    print(erra)
    gan = f_comp(forc,seg)
  
  if (gan):
    print(f'Parabéns, você ganhou com {jog} jogadas')
  else:
    print(f'Que pena, você não acertou a palavra {seg}')
      
  return 0

if __name__ == "__main__":
  main()