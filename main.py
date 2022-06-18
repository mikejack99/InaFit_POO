from datetime import date
class Pai:
  def __init__(self,**D):
    self.nome = D.pop('n','--')
    self.anoNasc = D.pop('a',0)
    self.sexo = D.pop('s','-')
  def calcIdade(self):
    agora = date.today()
    return agora.year - self.anoNasc
class Mae:
  def __init__(self,*L):
    self.peso = L[0]
    self.altura = L[1]
  def calcIMC(self):
    imc = round(self.peso / (self.altura**2),2)
    if imc >= 25:
      return "IMC: "+str(imc)+str("\nClassificação: Sobrepeso")
    else:
      if imc >= 18.5:
        return "IMC: "+str(imc)+str("\nClassificação: Peso Saudável")
      else:
        return "IMC: "+str(imc)+str("\nClassificação: Abaixo do Peso")
class Filha(Pai,Mae):
   def __init__(self,cor,compr,*L,**D):
    super().__init__(**D)
    Mae.__init__(self,*L)
    self.cabeloCor = cor
    self.cabeloCompr = compr
peso = float(input("Peso: "))
altura = float(input("Altura: "))
while peso<= 0 or altura<=0:
  print("Erro!! Peso ou altura menores ou iguais a 0")
  peso = float(input("Peso: "))
  altura = float(input("Altura: "))
filha1 = Filha ('castanho','longo',peso,altura,n='Angelica',a=1970,s='F')
print('Nome: '+str(filha1.nome)+'\nCor do cabelo: '+str(filha1.cabeloCor)+'\nTamanho do cabelo: '+str(filha1.cabeloCompr)+'\nPeso: '+str(filha1.peso),\
      '\nAltura: '+str(filha1.altura)+'\nIdade: '+str(filha1.calcIdade())+' anos'+'\n'+filha1.calcIMC())
