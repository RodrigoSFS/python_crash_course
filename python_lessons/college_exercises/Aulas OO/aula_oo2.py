class ClasseTeste():
    def __init__(self, a,b):
        self.a = a
        self.b = b
        self.__r = 0 

    def soma(self):
        self.r = self.a + self.b
        
    
    def imprime(self):
        print('resposta:', self.r)

    def __str__(self): # that would be like rewrite the 'toString' method in Java.
        saida = 'a:' + str(self.a) + ' b:' + str(self.b) + ' resposta:' + str(self.r)
        return saida

meu_obj = ClasseTeste(10,20)
meu_obj.soma()
meu_obj.imprime()

print(meu_obj) # that on itself print the memory path to the object, so we gotta write meu_obj.__str__, witch is like the 'toString' on Java.