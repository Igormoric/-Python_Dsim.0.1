

from matgeo import dist2p
import random

class pessoa:	#clase q cria pessoa
	def __init__(self,x,y,numero,d=0):
		self.x=x	#posicao horizontal da pessoa
		self.y=y	#posicao vertical da pessoa
		self.d=d	#se a pessoa esta doente(ou nivel de contaminacao)
		#self.c=False
		#self.a=True
		self.id=numero	#identifica a pessoa

class simu:
	def __init__(self,tempo,contamidados,populacao,perigod=5,perigoc=5,mapa=100):
		self.populacao=[]	#todas as pessoas
		self.populacaoc=[]	#todas as pessoas doentes
		self.tempolimite=tempo	#quanto tempo vai durar a simulacao
		self.npd=perigod	#chance de se contaminar
		self.npc=perigoc	#distancia para se contaminar
		self.limitemap=mapa	#tamanho maximo do mapa
		for i in range(populacao):
			self.populacao.append(pessoa(random.randint(1,self.limitemap),random.randint(1,self.limitemap),i))
		for i in range(contamidados):
			x=random.randint(1,populacao-1)
			self.populacao[x].d=self.npc
			self.populacaoc.append(self.populacao[x])
			#self.listamedia()

	def contadoente(self):
		x=0
		for i in self.populacao:
			if(i.d==5):
				x+=1
		return x
	
	def listapessoas(self):
		for i in self.populacao:
			print("cidadao {} em {},{} estado={}".format(i.id+1,i.x,i.y,i.d))
	
	def listamedia(self):
		x=self.contadoente()
		print("{} pessoas doentes de {}".format(x,len(self.populacao)))
      
	def getvar(self):
		print("tempo:{}\npessoas:{}\nnivel de perigo:{}\ninfectados:{}".format(self.tempolimite,len(self.populacao),self.npd,self.contadoente()))

	def pessoamov(self,pessoa):
		dire=random.randint(1,9)
		if((dire==7)or(dire==8)or(dire==9)):
			if(pessoa.x<self.limitemap):
				pessoa.x+=1
		if((dire==3)or(dire==6)or(dire==9)):
			if(pessoa.y<self.limitemap):
				pessoa.y+=1
		if((dire==7)or(dire==4)or(dire==1)):
			if(pessoa.y>1):
				pessoa.y-=1
		if((dire==1)or(dire==2)or(dire==3)):
			if(pessoa.x>1):
				pessoa.x-=1
        
	def pessoacontamina(self):
		for pessoa in self.populacaoc:
			for i in self.populacao:
				if((dist2p(pessoa.x,pessoa.y,i.x,i.y)<self.npd)):
					i.d+=2
		for i in self.populacao:
                        if(i.d>self.npc-1):
                                i.d=self.npc
                                self.populacaoc.append(i)
                        else:
                                if(i.d>1):
                                        i.d-=1
				
	def start(self):
#		self.listapessoas()
		self.getvar()
		self.listamedia()
		print("\n")
		for d in range(0,self.tempolimite):
			for i in self.populacao:
				self.pessoamov(i)
			self.pessoacontamina()
			print("dia:{} ".format(d+1))
			self.listamedia()
			if(self.populacao==self.populacaoc):
                                break

	def smalltest(self):
		test=simu(20,5,40,mapa=10)
		self.getvar()
		self.listamedia()
		print("\n")
		for d in range(0,self.tempolimite):
			for i in self.populacao:
				self.pessoamov(i)
			self.pessoacontamina()
			print("dia:{} ".format(d+1))
			self.listapessoas()
			if(self.populacao==self.populacaoc):
                                break
        
        

test=simu(10,5,200,mapa=100)
test.start()
