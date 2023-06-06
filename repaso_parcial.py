class NoHaySaldoException (Exception):
    pass
class UsuarioDesactivadoException (Exception):
    pass
class EstadoNoExistenteException (Exception):
    pass
PRECIO_TICKET = 70
PRIMARIO = PRECIO_TICKET * 0.5   
DESACTIVADO= 'desactivado'
ACTIVADO = 'activado'
SECUNDARIO= (PRECIO_TICKET - (PRECIO_TICKET * 0.4))
    
class Sube():
    def __init__(self):
        self.saldo = 1000
        self.grupo_beneficiario= None
        self.estado= ACTIVADO
    def obtener_precio_ticket(self):
        if self.grupo_beneficiario == SECUNDARIO:
            return SECUNDARIO
        if self.grupo_beneficiario == PRIMARIO:
            return PRIMARIO
        else:
            return PRECIO_TICKET
        
    def pagar_pasaje(self):
        if self.grupo_beneficiario != None:
          if self.grupo_beneficiario == PRIMARIO:
              self.saldo >= 35  
              self.saldo = (self.saldo -self.obtener_precio_ticket())
              return self.saldo
          if self.grupo_beneficiario == SECUNDARIO:
            self.saldo >= 42 
            self.saldo = (self.saldo - self.obtener_precio_ticket())
            return self.saldo
        if self.saldo < 70: 
            raise (NoHaySaldoException('saldo insuficiente'))  
        if self.estado == 'desactivado':
            raise UsuarioDesactivadoException ('sube desactivada')  
        self.saldo = (self.saldo -self.obtener_precio_ticket())
        return self.saldo
    
    def cambiar_estado(self, estado):
        self.estado = estado
        if self.estado == ACTIVADO:
            self.estado == DESACTIVADO
        if self.estado == DESACTIVADO:
            self.estado == ACTIVADO
        if estado != ACTIVADO and estado != DESACTIVADO:
            raise EstadoNoExistenteException ('extado no existente')

        pass


