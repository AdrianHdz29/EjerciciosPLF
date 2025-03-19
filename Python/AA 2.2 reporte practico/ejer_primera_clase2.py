# Autenticacion de usuarios
# Funciones de primera clase
def autenticar_por_password(usuario, password):
    return usuario == "admin" and password == "1234"
def autenticar_por_token(token):
    return token == "TOKEN-SECRETO"

def gestionar_autenticacion(metodo, *args):
    return metodo(*args)

# Uso de funciones de primera clase:
usuario_valido = gestionar_autenticacion(autenticar_por_password, input("Otorgue su usuario:  "), input("Otorgue su contraseña:  "))
token_valido = gestionar_autenticacion(autenticar_por_token, "TOKEN-SECRETO")

print("Acceso con password:", usuario_valido)
print("Acceso con token:", token_valido)