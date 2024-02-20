# kwatgs = parâmetro que irá acoplar todos os argumentos em um dictionary, útil para quando uma função aceita vários argumentos keyword

# args, pegam vários argumetnos posicionais, e guardam eles em um tuple
# kwargs pegam vários keywords e colocam eles em um dictionary

# também não é necessário que o nome seja kwargs, mas é convenção de nomeclarua, já que kwargs significa, keyword arguments
def hello(**kwargs):
    #print(kwargs['first'] + kwargs['last'])
    print("Hello",end=" ")
    for key,value in kwargs.items():
        print(value, end=" ")

hello(title= "Mr.", first="Bro", middle="Dude", last="Code")

