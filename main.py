# Install:
# pip install "unstructured[local-inference]"
# pip install "unstructured[all-docs]" for EPUB/PDF/Office
# pip install openai
# brew install poppler

"""
from unstructured.partition.pdf import partition_pdf
import openai

print("Start")
# 1. Extraer texto de un PDF
elements = partition_pdf(filename="documento.pdf")
texto = "\n".join([str(el) for el in elements])

# 2. Usar un LLM (por ejemplo, OpenAI GPT-3.5/4)
openai.api_key = "SOME_API_KEY"

respuesta = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Eres un asistente útil."},
        {"role": "user", "content": texto}
    ]
)

print(respuesta.choices[0].message.content)
"""

# Warning control
import warnings
warnings.filterwarnings('ignore')

from IPython.display import JSON
import json

# Función de partición local para PDF
from unstructured.partition.pdf import partition_pdf
from unstructured.staging.base import elements_to_json

# Archivo local
filename = "example_files/CoT.pdf"

# Particionar PDF localmente con opciones similares a la API
elements = partition_pdf(
    filename=filename,
    strategy="hi_res",  # usa OCR y análisis visual
    pdf_infer_table_structure=True,
    languages=["eng"]
)

# Mostrar los primeros elementos como JSON
json_output = elements_to_json(elements[:3])
JSON(json.loads(json_output))
