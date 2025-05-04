import pytesseract
from PIL import Image
import spacy
import requests

# Carregar modelo NLP
spacy.cli.download("pt_core_news_sm")
nlp = spacy.load("pt_core_news_sm")

# Função de validação de conteúdo online
def validate_social_content(url):
    if not url:
        return None
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            return False
        content = response.text.lower()
        return "furia" in content
    except:
        return False

# Função de análise de sentimento básico via SpaCy
def analyze_sentiment(text):
    if not text:
        return "🤔", "Sem comentário"
    doc = nlp(text)
    positive_keywords = ["ótimo", "excelente", "sensacional", "gostei", "top", "massa", "bom", "incrível", "gosto", "amo"]
    negative_keywords = ["ruim", "péssimo", "horrível", "não gostei", "decepcionante", "fraco"]

    pos_count = sum(1 for token in doc if token.lemma_.lower() in positive_keywords)
    neg_count = sum(1 for token in doc if token.lemma_.lower() in negative_keywords)

    if pos_count > neg_count:
        return "😄", f"Positivo ({pos_count} positivo(s), {neg_count} negativo(s))"
    elif neg_count > pos_count:
        return "😞", f"Negativo ({pos_count} positivo(s), {neg_count} negativo(s))"
    else:
        return "😐", "Neutro"

# Função para realizar OCR no upload do documento
def process_ocr(doc_upload):
    ocr_text = ""
    ocr_valid = False
    try:
        image = Image.open(doc_upload)
        ocr_text = pytesseract.image_to_string(image)
        if any(keyword in ocr_text.lower() for keyword in ["cpf", "rg"]):
            ocr_valid = True
        return ocr_text, ocr_valid
    except Exception as e:
        raise ValueError(f"Ocorreu um erro ao processar o documento: {e}")  


