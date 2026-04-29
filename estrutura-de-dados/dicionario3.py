tupla = (1,2,3,4,5)
print(tupla)

# desempacotamento de tupla
a,b,c,d,e = tupla 
print(a)
print(b)
print(c)
print(d)
print(e)

x,y,z = (10,20,30)
print(x)
print(y)
print(z)

a= (1,2,3)
print(a)
print("Id da primeira tupla", id(a)) #o id é o mesmo, ou seja, a tupla é imutável, ou seja, não pode ser alterada, ou seja, quando tentamos alterar a tupla, na verdade estamos criando uma nova tupla e atribuindo a variável a para essa nova tupla, ou seja, a variável a passa a apontar para a nova tupla e o id da nova tupla é diferente do id da tupla original

a= (0,1,2)
print(a)
print("Id da segunda tupla", id(a)) #o id é diferente, ou seja, a tupla foi alterada, ou seja, a variável a passou a apontar para a nova tupla e o id da nova tupla é diferente do id da tupla original

c= (1,2,3)
d= c
print("Id do c: ", id(c))
print("Id do d: ", id(d))