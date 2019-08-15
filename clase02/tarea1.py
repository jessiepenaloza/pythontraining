Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Empleado():
    nombre = ""
    apellido = ""
    sueldo = ""
    
    def __init__(self, nombre, apellido, sueldo):
        self.nombre = nombre
        self.apellido = apellido
        self.sueldo = int(sueldo)
    
    def obtener_nombre_apellido_sueldo(self):
        return f"{self.nombre}, {self.apellido} y cobra {self.sueldo}"

>>> empleado = Empleado("María", "Casas", 10000)
>>> empleado.obtener_nombre_apellido_sueldo()
'María, Casas y cobra 10000'
>>> 
