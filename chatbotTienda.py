import tkinter as tk
import random

# Definir las respuestas del chatbot
respuesta = {
    "guitarras": [
        "¡Descubre nuestras increíbles promociones en guitarras eléctricas y acústicas!",
        "¿Estás buscando una nueva guitarra? Tenemos una gran selección de modelos y marcas.",
        "Las mejores ofertas en guitarras están aquí. ¡No te las pierdas!"
    ],
    "instrumentos": [
        "Explora nuestra amplia variedad de instrumentos musicales: pianos, baterías, teclados y más.",
        "Encuentra el instrumento perfecto para ti, ya sea que seas un principiante o un músico experimentado.",
        "¡Ven y descubre el mundo de la música con nuestra colección de instrumentos de alta calidad!"
    ],
    "grabación": [
        "Equipa tu estudio de grabación con los mejores equipos: micrófonos, interfaces, monitores y más.",
        "¿Listo para llevar tu música al siguiente nivel? Tenemos todo lo que necesitas para grabar y producir.",
        "Descubre nuestras ofertas en equipos de grabación. ¡Haz que tus grabaciones suenen profesionales!"
    ],
    "promociones": [
        "¡No te pierdas nuestras promociones actuales en todos nuestros productos!",
        "Consulta nuestras promociones vigentes para obtener descuentos y ofertas especiales.",
        "Visita nuestra tienda para descubrir las promociones disponibles en una amplia variedad de artículos."
    ],

    "compra": [
        "Puedes realizar una compra en nuestra tienda en línea.",
        "Visita nuestro sitio web para ver nuestra selección de productos y realizar una compra.",
        "¿Listo para comprar? ¡Dirígete a nuestra tienda en línea ahora mismo!"
    ],

    "hola": ["¡Hola!", "¡Hola! ¿Cómo estás?", "¡Hola! ¿En qué puedo ayudarte?"],

    "adios": ["¡Adiós!", "¡Hasta luego!", "¡Nos vemos pronto!"]
}

respuestaDos = [
    "Lo siento, no entiendo tu pregunta.",
    "Perdón, no entendí lo que dijiste.",
    "Lo siento, ¿Necesitas conocer una promoción o consultar algun producto?",
    "Disculpa, no capté tu consulta.",
    "Lo siento, no pude entender lo que quisiste decir.",
    "Perdona, ¿Necesitas conocer una promoción o consultar algun producto?"
]

respuestaTres = [
    "¿En qué puedo ser de ayuda?",
    "¿En qué puedo servirte hoy?",   
    "¿Qué puedo hacer para facilitarte las cosas?"    
]

# Mensaje inicial de bienvenida
mensaje_inicial = "¡Hola! Bienvenido a instrumentos_chidos.com.mx \n\n" + random.choice(respuestaTres)

# Definir la función para el chatbot
def chatbot_response(message):
    message = message.lower()
    for keyword, lista_respuesta in respuesta.items():
        if keyword in message:
            return random.choice(lista_respuesta)
    return random.choice(respuestaDos)

# Definir la función para mostrar el mensaje inicial de bienvenida
def mostrar_mensaje_inicial():
    label.config(text=mensaje_inicial)
    entry.delete(0, tk.END)  # Limpiar la caja de texto

# Definir la función para mostrar las respuestas del chatbot en una ventana
def mostrar_respuesta(event=None):  # El argumento event=None permite llamar a la función con y sin evento
    entrada_usuario = entry.get()
    if entrada_usuario.lower() == "cerrar":
        root.destroy()  # Cerrar la ventana si el usuario ingresa "adiós"
    else:
        respuesta = chatbot_response(entrada_usuario)
        label.config(text="Chatbot: \n" + respuesta)
        entry.delete(0, tk.END)  # Limpiar la caja de texto

# Definir la función para regresar al mensaje inicial
def regresar_mensaje_inicial():
    label.config(text=mensaje_inicial)
    entry.delete(0, tk.END)  # Limpiar la caja de texto

# Crear la ventana principal
root = tk.Tk()
root.title("Tu tienda")

# Crear y colocar los elementos en la ventana
label = tk.Label(root, text=mensaje_inicial)
label.pack()

entry = tk.Entry(root, width=50)
entry.pack()

button_enviar = tk.Button(root, text="Enviar", command=mostrar_respuesta)
button_enviar.pack()

button_finalizar = tk.Button(root, text="Finalizar", command=regresar_mensaje_inicial)
button_finalizar.pack()

# Enlazar la tecla "Enter" con la función mostrar_respuesta
root.bind('<Return>', mostrar_respuesta)

# Ejecutar el bucle de eventos
root.mainloop()
