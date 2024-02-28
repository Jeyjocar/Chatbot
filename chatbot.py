"""CREACION DE UN CHATBOT"""
import pyttsx3

#1- Crear el entorno virtual (ALICE)
#2- Importar la libreria pyttsx3
#3- Se importa la libreria pyttsx3

motor_voz = pyttsx3.init()
voices = motor_voz.getProperty("voices") #Se obtienen las propiedades de las voces de la librería

for idm, voice in enumerate(voices):
   print("voz# {}".format(idm + 0))
   print("id {}".format(voice.id)) 
   print("nombre {}".format(voice.name)) 
   print("idioma {}".format(voice.languages[0] if voice.languages else "lenguaje desconocido"))
   print("género {}".format(voice.gender))
   print("edad {}".format(voice.age))
   print("\n")

indice_voz = 0
motor_voz.setProperty('voice', voices[indice_voz].id)
texto = "Bienvenido, soy tu asistente virtual"  
motor_voz.say(texto)
motor_voz.runAndWait()  
