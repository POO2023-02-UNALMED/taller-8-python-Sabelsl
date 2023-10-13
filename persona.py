class Persona:
    def __init__(self, nombre, edad, altura, sexo):
        self._nombre = nombre
        self._edad = edad
        self._altura = altura
        self._sexo = sexo
    
    def setNombre(self, nombre):
        self._nombre = nombre
    def getNombre(self):
        return self._nombre
    
    def setEdad(self, edad):
        self._edad = edad
    def getEdad(self):
        return self._edad
    
    def setAltura(self, altura):
        self._altura = altura
    def getAltura(self):
        return self._altura
    
    def setSexo(self, sexo):
        self._sexo = sexo
    def getSexo(self):
        return self._sexo