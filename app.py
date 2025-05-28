from flask import Flask, request, jsonify
from flask_cors import CORS # Para permitir solicitudes desde el frontend
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv() # Cargar variables de entorno del archivo .env

app = Flask(__name__)
CORS(app) # Habilitar CORS para todas las rutas

# Configura la API de Gemini
GEMINI_API_KEY = os.getenv("AIzaSyB70WAK5AMuLVJPhdmASEQv-_JzdF1W50c")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY no está configurada en el archivo .env")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash') # O 'gemini-1.5-pro-latest' si tienes acceso

@app.route('/improve_text', methods=['POST'])
def improve_text():
    data = request.json
    text_to_improve = data.get('text', '')

    if not text_to_improve:
        return jsonify({"error": "No se proporcionó texto para mejorar"}), 400

    prompt = f"Corrige la gramática y el estilo del siguiente texto, y sugiere mejoras para que sea más claro y conciso:\n\n{text_to_improve}\n\nTexto mejorado:"
    try:
        response = model.generate_content(prompt)
        # Acceder de forma segura a la respuesta
        improved_text = response.text if response.candidates else "No se pudo generar una mejora."
        return jsonify({"improved_text": improved_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/complete_text', methods=['POST'])
def complete_text():
    data = request.json
    current_text = data.get('text', '')
    instruction = data.get('instruction', '') # Opcional: una instrucción para la generación

    if not current_text and not instruction:
        return jsonify({"error": "Se necesita texto actual o una instrucción para completar"}), 400

    prompt = f"Basado en el siguiente texto y/o instrucción, genera una continuación:\n\nTexto actual: {current_text}\nInstrucción: {instruction}\n\nContinuación:"
    try:
        response = model.generate_content(prompt)
        generated_text = response.text if response.candidates else "No se pudo generar una continuación."
        return jsonify({"generated_text": generated_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '_main_':
    app.run(debug=True, port=5000) # Ejecutar en http://127.0.0.1:5000
