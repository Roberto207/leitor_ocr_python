from PIL import Image
import pytesseract
import csv
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Se o Tesseract estiver instalado em um caminho específico (Windows)
# Descomente e ajuste a linha abaixo com o caminho correto:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Caminho da imagem JPG
caminho_imagem = "SEU_CAMINHO_AQUI"#COLOQUE AQUI O CAMINHO DA SUA IMAGEM

# Abre a imagem
imagem = Image.open(caminho_imagem)

# Usa OCR pra extrair o texto da imagem
texto_extraido = pytesseract.image_to_string(imagem)

# Divide o texto em linhas
linhas = texto_extraido.split('\n')

# Cria um CSV e escreve cada linha extraída
with open('saida.csv', mode='w', newline='', encoding='utf-8') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    for linha in linhas:
        if linha.strip():  # Ignora linhas em branco
            writer.writerow([linha])

print("✅ Arquivo CSV criado com sucesso como 'saida.csv'")

