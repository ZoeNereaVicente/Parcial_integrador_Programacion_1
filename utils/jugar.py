from games import *

def jugar(juego_elegido):
  """Esta función se encarga de validar a que juego llamar de acuerdo al parametro que recibe"""

  hayError = False
  match juego_elegido:
    case 'Adivinanza':
      return print("funcion jugar_adivinanza")
    
    case 'Trivia':
      return jugar_trivia()
    
    case 'Batalla Naval':
      return print("funcion jugar_batalla_naval")
      
    case 'Memoria':
      return print("funcion jugar_memoria")
    
    case 'Piedra, Papel o Tijera':
      return jugar_piedra_papel_tijera()
    
    # Caso default
    case _:
      print(f"❌ Hubo un error al cargar el juego: {juego_elegido}.")
      hayError = True
      return hayError
  return hayError
