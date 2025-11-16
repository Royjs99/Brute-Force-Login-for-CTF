# Brute-Force-Login-for-CTF
Esta herramienta permite realizar un ataque de fuerza bruta a un panel de login del CTF NODECEPTION.

## Características
- Manejo de errores de conexión
- Manejo de diccionarios

## Validación de Contraseñas
La herramienta está diseñada para probar contraseñas que cumplan:
- **Longitud mínima**: 8 caracteres
- **Al menos 1 número** 
- **Al menos 1 letra mayúscula**

## Instalación de requests
pip3 install requests

## Uso de la herramienta
python3 login_brute_force.py -e user@email.com -u http://IP -d /dictionary.txt

## Ejemplo de uso
python3 login_brute_force.py -e admin@mail.com -u http://192.168.1.133/login.php -d /dictionary.txt

python3 login_brute_force.py --email admin@mail.com --url http://192.168.1.133/login.php --dictionary /rockyou.txt

## Parámetros
**-e; --email** indica el email al cual se va a atacar.
**-u; --url** indica la dirección del panel de inicio de sesión.
**-d; --dictionary** indica la ubicación del diccionario de contraseñas.

## Avisos
La herramienta ha sido desarrollada para fines educativos, queda en responsabilidad del usuario el uso indebido del programa.
