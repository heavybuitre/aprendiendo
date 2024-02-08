#Variables
my_variable = "My String Variable"
print(my_variable)
cliente = "Dell"
print(cliente)
kilometros = 5
print(kilometros)
bool_variable = False
print(bool_variable)
#Concatenación de variables en print
print(cliente, kilometros, bool_variable)
my_int_to_str_variable = str(my_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

#Funciones del sistema
print(len(my_int_to_str_variable))  #Contar caracteres
print("Kilometros recorridos:",kilometros)
#Variables en una sola linea
name, apellido, alias, edad = "Yeicob","Herrera", 'heavybuitre', 35.5
print("Me llamo:", name, apellido, "Mi edad es:",edad,'años Y mi alias es:', alias)
print(type(edad))
#Solicitar datos
name = input('¿Cual es tu nombre?')
edad = input('¿Cuantos años tienes?')
print(name )
print(edad)

#No tiene type fuerte o constante, cambia entre numeros y texto sin problema
name = 38
age= 'Yeicob'
print(name)
print(age)

#¿Forzamos el tipo? INT(Entero) STR (texto)
address: str = 'Mi direccion'
address = True
address = 5
adrress = 1.2


 