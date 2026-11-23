#Importamos ABC y abstractmethod
from abc import ABC, abstractmethod
from registro import registrar_evento

#Creamos la clase Entidad, con (ABC) indicamos que será una clase abstracta
class Entidad(ABC):
    
    #creamos el método que se ejecuta cuando creamos un objeto
    def __init__(self, identificacion, nombre):
        
        #Validamos los datos
        if not identificacion:
            raise ValueError("La identificación es obligatoria")

        if not nombre or not nombre.strip():
            raise ValueError("El nombre es obligatorio")
        
        #Guardamos los atributos    
        self.identificacion = identificacion
        self.nombre = nombre

    #Creamos el método abstracto
    @abstractmethod
    def mostrar_informacion(self):
        pass

#Creamos la clase Cliente que está heredando de Entidad
class Cliente(Entidad):

    #creamos el método que se ejecuta cuando creamos un objeto y recibe cuatro datos
    def __init__(self, identificacion, nombre, correo, telefono):

        #llamamos al constructor de la clase padre
        super().__init__(identificacion, nombre)

        #Aplicamos encapsulación para proteger los datos personales del cliente para evitar que sean modificados directamente desde fuera de la clase
        self.__correo = self.validar_correo(correo)
        self.__telefono = self.validar_telefono(telefono)
        
        registrar_evento(
            f"Cliente registrado: {self.nombre} - ID: {self.identificacion}")

    #Validamos el correo electrónico
    def validar_correo(self, correo):

        if not correo or "@" not in correo:
            raise ValueError("El correo electrónico no es válido") #generamos una excepción

        if "." not in correo.split("@")[-1]:
            raise ValueError("El correo debe tener un dominio válido")

        return correo

    #Validamos el teléfono
    def validar_telefono(self, telefono):

        telefono = str(telefono).strip()

        if not telefono.isdigit():
            raise ValueError("El teléfono debe contener solo números")

        if len(telefono) < 7 or len(telefono) > 15:
            raise ValueError("El teléfono debe tener entre 7 y 15 dígitos")

        return telefono

    #Mostrar la información del cliente
    def mostrar_informacion(self):

        return (
            f"Identificación: {self.identificacion}\n"
            f"Nombre: {self.nombre}\n"
            f"Correo: {self.__correo}\n"
            f"Teléfono: {self.__telefono}"
        )
    
    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono