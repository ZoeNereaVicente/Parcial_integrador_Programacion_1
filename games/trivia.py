import random
# Lista de diccionarios con las preguntas para jugar.
# Al ser una constante que NO va cambiar, se define en mayúsculas.
PREGUNTAS = [
  {
    "categoria": "Historia",
    "pregunta": "¿En qué año el hombre pisó la Luna por primera vez?",
    "opciones": ["1969", "1972", "1963", "1954"],
    "respuesta": "1969"
  },  
  {
    "categoria": "Historia",
    "pregunta": "¿En qué año cayó el Muro de Berlin?",
    "opciones": ["1560", "1976", "1989", "2002"],
    "respuesta": "1989"
  },
  {
    "categoria": "Historia",
    "pregunta": "¿Qué filósofo griego afirmó: Sólo se que no se nada?",
    "opciones": ["Platón", "Aristóteles", "Epicuro", "Sócrates"],
    "respuesta": "Sócrates"
  },
  {
    "categoria": "Entretenimiento",
    "pregunta": "¿Qué película ganó el Oscar a Mejor Película en 2020?",
    "opciones": ["Joker", "Parasite", "1917", "Había una vez en Hollywood"],
    "respuesta": "Parasite"
  },
  {
    "categoria": "Entretenimiento",
    "pregunta": "¿De quién es la canción Watermelon Sugar?",
    "opciones": ["Bruno Mars", "Justin Bieber", "Post Melone", "Harry Styles"],
    "respuesta": "Harry Styles"
  },
  {
    "categoria": "Entretenimiento",
    "pregunta": "¿Que prenda le otorgada a Dobby en Harry Potter le permite ganar su libertad?",
    "opciones": ["Un calcetín", "Una corbata", "Un guante", "Una remera"],
    "respuesta": "Un calcetín"
  },
  {
    "categoria": "Ciencia",
    "pregunta": "¿Cuál es la arteria de mayor diámetro?",
    "opciones": ["Ilíaca", "Radio", "Carótida", "Aorta"],
    "respuesta": "Aorta"
  },
  {
    "categoria": "Ciencia",
    "pregunta": "¿Quién descubrió la pasteurización?",
    "opciones": ["Charles Darwin", "Louis Pasteur", "Robert Hooke", "Gregor Mendel"],
    "respuesta": "Louis Pasteur"
  },
  {
    "categoria": "Ciencia",
    "pregunta": "¿A qué especie de animal pertenece la serpiente?",
    "opciones": ["Reptil", "Mamífero", "Ave", "Insecto"],
    "respuesta": "Reptil"
  },
  {
    "categoria": "Geografía",
    "pregunta": "¿En qué provinvia Argentina se encuentra San Martín de los Andes?",
    "opciones": ["Chubut", "Mendoza", "Neuquén", "Río Negro"],
    "respuesta": "Neuquén"
  },
  {
    "categoria": "Geografía",
    "pregunta": "¿Cuál es la capital de Uruguay?",
    "opciones": ["Montevideo", "Punta del Este", "Canelones", "Cabo Polonio"],
    "respuesta": "Montevideo"
  },
  {
    "categoria": "Geografía",
    "pregunta": "¿Cuál es la capital de Uruguay?",
    "opciones": ["Montevideo", "Punta del Este", "Canelones", "Cabo Polonio"],
    "respuesta": "Montevideo"
  },
  {
    "categoria": "Deportes",
    "pregunta": "¿Qué deporte practicaba Michael Phelps?",
    "opciones": ["Salto en alto", "Cricket", "Tenis", "Natación"],
    "respuesta": "Natación"
  },
  {
    "categoria": "Deportes",
    "pregunta": "¿Cuál es el nombre completo del tenista Del Potro?",
    "opciones": ["Juan Martin", "Juan Carlos", "Juan Manuel", "Rodrigo"],
    "respuesta": "Juan Martin"
  },
  {
    "categoria": "Deportes",
    "pregunta": "¿Cuál es la competencia deportiva que consta de cinco pruebas atléticas?",
    "opciones": ["Decatlón", "Pentatlón", "Maratón", "Carrera de cinco"],
    "respuesta": "Pentatlón"
  },
]

def validar_pregunta(preg):
  '''
  Valida que el diccionario de la pregunta tenga el formato correcto:
  - Que las opciones sean cuatro.
  - Que la respuesta correcta exista en las opciones de la pregunta.

  Retorna un dato booleano.
  '''
  try:
    return len(preg['opciones']) == 4 and preg['respuesta'] in preg['opciones']
  except (KeyError, TypeError):
    return False
  
def seleccionar_pregunta(pregs, intentos=0):
  '''
  Selecciona una pregunta de la lista de preguntas al azar.
  Si la pregunta no tiene un formato válido, vuelve a elegir una nueva.
  Recibe la lista de preguntas por parámetro, además suma intentos para no entrar en loop.
  '''
  # Validar que sea una lista.
  if not isinstance(pregs, list):
    raise TypeError("❌ El tipo de dato es incorrecto. Tiene que ser una lista.")
  
  # Validar que haya preguntas disponibles
  if len(pregs) == 0:
    raise ValueError("⚠️  No quedan preguntas disponibles.")
  
  # Caso base
  if intentos >= 2:
    raise ValueError("❌ No se puede obtener una pregunta con formato válido.")
  
  indice = random.randint(0, len(pregs) - 1)
  # Seleccionamos la pregunta y la eliminamos de la lista,
  # de esa forma, nos aseguramos que no se repita.
  pregunta = pregs.pop(indice)

  if validar_pregunta(pregunta):
    return pregunta
  
  print("⚠️  Pregunta inválida, buscando otra...\n")
  return seleccionar_pregunta(pregs, intentos + 1)

def mostrar_pregunta(preg):
  '''
  Crea la visual de la pregunta con las opciones de respuesta.
  Recibe la pregunta como parámetro.
  '''
  categoria = preg["categoria"]
  pregunta = preg["pregunta"]
  opciones = preg["opciones"]

  mensaje_a_mostrar = f'{categoria}: {pregunta}'
  # Calculamos el ancho de la tabla
  ancho = len(mensaje_a_mostrar) + 2
  linea = f'+{"-" * ancho}+'
  
  # TABLA
  print(linea)
  print(f'| {mensaje_a_mostrar} |')
  print(linea)
  for i, opcion in enumerate(opciones, start=1):
    opcion_a_mostrar = f'{i}- {opcion}'.ljust(ancho - 2)
    print(f'| {opcion_a_mostrar} |')
    print(linea)

def obtener_respuesta():
  '''
  Solicita y valida la respuesta del usuario.
  Permite hasta 3 intentos para ingresar una respuesta válida.
  Retorna la respuesta del usuario o SALIR si no es una respuesta válida.
  '''
  max_intentos = 3
  
  for i in range(max_intentos):
    rta = input('Indicá la opción correcta (1-4): ').strip().upper()
    
    if rta == "SALIR" or (rta.isdigit() and 1 <= int(rta) <= 4):
      return rta
    
    # Mostramos advertencia si no es el último intento
    if i < max_intentos - 1:
      intentos_restantes = max_intentos - (i + 1)
      print(f'⚠️  Opción inválida. Debe ser un valor entre 1 y 4 o SALIR.\nIntentos restantes: {intentos_restantes}\n')
  
  print('❌ Se agotaron los intentos.')
  return "SALIR"
  
def jugar_trivia():
  '''
  Función principal que ejecuta el juego de trivia.
  '''
  msj_fin = "\n📌 Juego finalizado."
  rta = ""
  rtas_correctas = 0
  # Hacemos una copia para no modificar la lista original.
  preguntas_para_jugar = PREGUNTAS.copy()

  print('''
  ===============================
              Trivia     
  ===============================           
  ''')
  print('''Instrucciones:
    - Respondé correctamente 3 preguntas para ganar.
    - Escribí SALIR para finalizar el juego en cualquier momento.
    - En caso de responder mal, el juego finaliza. 
  ''')

  while rta != "SALIR" and rtas_correctas < 3:
    try:
      pregunta = seleccionar_pregunta(preguntas_para_jugar)
    except (ValueError, TypeError) as e: 
      print(f'{e}\n{msj_fin}')
      return

    mostrar_pregunta(pregunta)
    print()
    rta = obtener_respuesta()

    if rta == "SALIR":
      print(f'\nSaliendo del juego... {msj_fin}')
    elif pregunta['opciones'][int(rta)-1] == pregunta['respuesta']:
      print("\n🤩 Respuesta correcta. ¡Seguí así!\n")
      rtas_correctas += 1
    else:
      print(f'\n😞 Respuesta incorrecta. {msj_fin}')
      return

  if rtas_correctas == 3:
    print(f'\n🎉 ¡Felicitaciones! Ganaste el juego 🎉 {msj_fin}')