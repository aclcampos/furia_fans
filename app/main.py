import streamlit as st
import pandas as pd
from datetime import datetime
import os
from utils import validate_social_content, analyze_sentiment, process_ocr

# --- Configuração Inicial ---
st.set_page_config(page_title="FURIA Fan Connect", page_icon="🎮")

# --- CSS Customizado ---
st.markdown("""
    <style>
    body { background-color: #0f0f0f; color: white; }
    .reportview-container { background: #0f0f0f; color: white; }
    .stButton>button { background-color: #FFD700; color: black; border-radius: 8px; }
    .stTextInput>div>div>input, .stTextArea>div>textarea, .stNumberInput>div>input {
        background-color: #1a1a1a; color: white;
    }
    .footer { background-color: #1a1a1a; color: white; text-align: center; padding: 10px 0; position: fixed; width: 100%; bottom: 0; }
    .footer a { color: #FFD700; font-size: 14px; margin-right: 15px; text-decoration: none; }
    .footer a:hover { text-decoration: underline; }
    </style>
""", unsafe_allow_html=True)

# --- Banner ---
st.image("assets/furia.jpg", use_column_width=True)

# --- Título ---
st.title("🎮 FURIA Fan Connect")
st.subheader("Cadastre-se e conecte-se com a Nação FURIA! 🖤")

# --- Coleta de dados ---
st.header("📋 Dados Básicos")
name = st.text_input("Nome completo")
cpf = st.text_input("CPF")
email = st.text_input('E-mail')
address = st.text_input("Endereço completo")
city = st.text_input("Cidade")
age = st.number_input("Idade", min_value=10, max_value=100, step=1)

games = st.multiselect("Jogos que joga:", ["CS", "Valorant", "LoL", "Free Fire", "Dota 2"])
fav_player = st.text_input("Jogador FURIA favorito")

# --- Frequência e conteúdo ---
frequency = st.slider("Quantos dias por semana você joga?", 0, 7, 3)
content_types = st.multiselect("Que conteúdo curte?", ["Vídeos", "Highlights", "Memes", "Entrevistas"])

# --- Compra e eventos ---
buy_products = st.radio("Comprou produtos FURIA no último ano?", ["Sim", "Não"])
event_interest = st.radio("Participaria de eventos da FURIA?", ["Sim", "Não"])

# --- Upload documento (OCR) ---
st.header("📄 Upload de Documento")
doc_upload = st.file_uploader("Envie seu RG ou CPF escaneado (PNG, JPG ou JPEG)", type=["png", "jpg", "jpeg"])

ocr_text = ""
ocr_valid = False

if doc_upload is not None:
    try:
        ocr_text, ocr_valid = process_ocr(doc_upload)
        st.write("📝 Texto extraído do documento:")
        st.text(ocr_text)

        if ocr_valid:
            st.success("✅ Documento validado com sucesso!")
        else:
            st.warning("⚠️ Não foi possível identificar CPF ou RG no documento.")
    except Exception as e:
        st.error(f"Ocorreu um erro ao processar o documento: {e}")

# --- Redes Sociais ---
st.header("🔗 Suas Redes Sociais")
insta = st.text_input("Link do Instagram")
twitch = st.text_input("Link do Twitch")
steam = st.text_input("Link do Steam")
hltv = st.text_input("Link do HLTV/Liquipedia")

# --- Validações de redes sociais ---
validations = {
    "Instagram": validate_social_content(insta),
    "Twitch": validate_social_content(twitch),
    "Steam": validate_social_content(steam),
    "HLTV/Liquipedia": validate_social_content(hltv)
}

st.subheader("🔎 Validação das Redes Sociais")
for network, is_valid in validations.items():
    if is_valid is None:
        st.info(f"{network}: Não fornecido ou URL inválido")
    elif is_valid:
        st.success(f"{network}: Relevante")
    else:
        st.warning(f"{network}: Não Relevante")

# --- Feedback ---
st.header("📝 Deixe sua opinião sobre a FURIA")
feedback = st.text_area("Escreva sua opinião:")

emoji, analysis = analyze_sentiment(feedback)
st.write(f"Sentimento identificado: {emoji}")

# --- Botão de envio ---
if st.button("🔥 Enviar Cadastro"):
    data = {
        "nome": name,
        "cpf": cpf,
        "email": email,
        "endereco": address,
        "cidade": city,
        "idade": age,
        "jogos": ", ".join(games),
        "jogador_favorito": fav_player,
        "frequencia_jogo": frequency,
        "conteudos": ", ".join(content_types),
        "compra_produtos": buy_products,
        "interesse_evento": event_interest,
        "instagram": insta,
        "twitch": twitch,
        "steam": steam,
        "hltv": hltv,
        "ocr_text": ocr_text,
        "ocr_valid": "Sim" if ocr_valid else "Não",
        "redes_sociais_validacao": validations,
        "feedback": feedback,
        "feedback_analise": analysis,
        "data_envio": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    if not os.path.exists("fans_data.csv"):
        pd.DataFrame([data]).to_csv("fans_data.csv", index=False)
    else:
        df = pd.read_csv("fans_data.csv")
        df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
        df.to_csv("fans_data.csv", index=False)

    st.success("🔥 Cadastro realizado com sucesso!")

# --- Visualizar cadastros (Admin) ---
if st.checkbox("👀 Ver cadastros"):
    if os.path.exists("fans_data.csv"):
        df = pd.read_csv("fans_data.csv")
        st.dataframe(df)
    else:
        st.info("Nenhum cadastro realizado ainda.")

# --- Rodapé ---
st.markdown("""
<div class="footer">
    <a href="https://www.instagram.com/furiagg?igsh=b3VzcjVnZGc5eTEy" target="_blank">Instagram</a>
    <a href="https://twitter.com/furia" target="_blank">Twitter</a>
    <a href="https://www.twitch.tv/furiatv" target="_blank">Twitch</a>
    <a href="https://www.youtube.com/channel/UCE4elIT7DqDv545IA71feHg" target="_blank">YouTube</a>
</div>
""", unsafe_allow_html=True)
