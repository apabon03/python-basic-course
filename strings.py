myStr = "Hello World"

print(f"Mi saludo en ingles es: { myStr }")
print("Mi saludo en ingles es: {0}".format(myStr))

#print(dir(myStr))

print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.capitalize())
print(myStr.replace('Hello', 'bye').upper()) #metodos encadenados
print(myStr.count('l'))
print(myStr.startswith('hola'))
print(myStr.endswith('ld'))
print(myStr.split())
print(myStr.find('o'))  #devuelve la posicion
print(len(myStr))
print(myStr.index('e'))
print(myStr.isnumeric())
print(myStr.isalpha())
print(myStr[4])
print(myStr[-4])
