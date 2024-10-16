print(" ")
print("Alvaro Campechano 3W")
print(" ")
# Creamos un diccionario para almacenar la información del usuario.
usuario = {}

# Solicitamos al usuario que ingrese su nombre, edad, dirección y teléfono.
usuario['nombre'] = input("Introduce tu nombre: ")
usuario['edad'] = input("Introduce tu edad: ")
usuario['direccion'] = input("Introduce tu dirección: ")
usuario['telefono'] = input("Introduce tu número de teléfono: ")

# Mostramos el mensaje con la información del usuario.
print(f"{usuario['nombre']} tiene {usuario['edad']} años,")
print(f"vive en {usuario['direccion']} y su número de teléfono es {usuario['telefono']}.")
