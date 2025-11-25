from games import *

def jugar(juego_elegido):
  """Esta función se encarga de validar a que juego llamar de acuerdo al parametro que recibe"""
  match juego_elegido:
    case 'Adivinanza':
      jugar_adivinanza()
      return False
    
    case 'Trivia':
      jugar_trivia()
      return False
    
    case 'Batalla Naval':
      jugar_batalla_naval()
      return False
      
    case 'Memoria':
      return print("funcion jugar_memoria")
    
    case 'Piedra, Papel o Tijera':
      jugar_piedra_papel_tijera()
      return False
    
    # Caso default
    case _:
      print(f"❌ Hubo un error al cargar el juego: {juego_elegido}.")
      return True
