from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Documento base: calendario académico 2025 de la UNAL
documento_base = """
PRIMER PERÍODO ACADÉMICO DE 2025
1. Inscripción de asignaturas: Hasta el 30 de marzo
2. Iniciación de clases: 31 de marzo
3. Semana santa: Del 14 al 20 de abril
4. Examen de admisión Pregrado: 27 de abril
   Examen de admisión Posgrado: 23 de mayo
5. Finalización de clases: 26 de julio
6. Reporte del 100% de calificaciones al SIA: Hasta las 8:00 p.m. del 29 de julio

SEGUNDO PERÍODO ACADÉMICO DE 2025
1. Inscripción de asignaturas: Hasta el 24 de agosto
2. Iniciación de clases: 25 de agosto
3. Examen de admisión Pregrado: 21 de septiembre
   Examen de admisión Posgrado: 17 de octubre
4. Finalización de clases: 13 de diciembre
5. Reporte del 100% de calificaciones al SIA: Hasta las 8:00 p.m. del 16 de diciembre

CEREMONIAS DE GRADO 2025
Inscripción de candidatos a grado (primera ceremonia): Del 10 al 24 de abril
Primera ceremonia de grados: Del 3 al 13 de junio
Inscripción de candidatos a grado (segunda ceremonia): Del 10 al 25 de septiembre
Segunda ceremonia de grados: Del 10 al 21 de noviembre

PARÁGRAFO: Las actividades de posgrado como Tesis o Proyectos pueden tener modificación de notas hasta la fecha de finalización de clases del siguiente periodo académico, a las 5:00 p.m.
"""

# Preprocesamiento
fragmentos = [line.strip() for line in documento_base.strip().split('\n') if line.strip()]
vectorizer = TfidfVectorizer()
matriz_tfidf = vectorizer.fit_transform(fragmentos)

# Función para responder preguntas
def responder_pregunta(pregunta):
    pregunta_vec = vectorizer.transform([pregunta])
    similitudes = cosine_similarity(pregunta_vec, matriz_tfidf)
    idx_mejor = np.argmax(similitudes)
    return fragmentos[idx_mejor]

# Interfaz de consola
def chat_calendario():
    print("🧠 Chat UNAL - Calendario Académico 2025")
    print("Escribe tu pregunta (escribe 'salir' para terminar):\n")
    while True:
        pregunta = input("Tú: ")
        if pregunta.lower() in ("salir", "exit"):
            print("👋 Hasta luego.")
            break
        respuesta = responder_pregunta(pregunta)
        print("UNALBot:", respuesta, "\n")

# Iniciar el chat
chat_calendario()
