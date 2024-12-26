import streamlit as st
import google.generativeai as genai
import pandas as pd

# Configure o modelo do Gemini
genai.configure(api_key=st.secrets.GEMINI_API_KEY)

# Define o modelo e a temperatura
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

# Ajusta as configurações de segurança (opção mais permissiva)
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_ONLY_HIGH"
    },
]

# For Gemini 1.5 Pro
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

# Função para gerar alternativas com prompt aprimorado
def generate_alternatives(game_type):
    # Carrega os exemplos do arquivo
    with open("exemplos.txt", "r") as f:
        examples = f.read()

    prompt = f"""
Você é um assistente de um jogo de escolhas chamado 'Você Prefere?'.
Seu objetivo é gerar duas alternativas únicas, interessantes e dentro do tema proposto.

**Tipo de Jogo:** {game_type}

**Formato da Resposta:**

A resposta DEVE conter SOMENTE as duas alternativas, cada uma em uma linha separada, SEM numeração ou qualquer outro texto adicional.

**Exemplos de alternativas (leia com atenção para entender o estilo e o tipo de humor):**

{examples}

**Gere agora duas alternativas para o tipo de jogo: {game_type}**
"""
    response = model.generate_content(prompt)
    text = response.text.strip()
    alternatives = text.split('\n')

    # Validação para garantir duas alternativas limpas
    while len(alternatives) != 2 or not all(alternatives):
        response = model.generate_content(prompt)
        text = response.text.strip()
        alternatives = text.split('\n')

    return alternatives

# Função para salvar a resposta (mantém a mesma lógica)
def save_response(choice, alternative1, alternative2):
    data = {'choice': [choice], 'alternative1': [alternative1], 'alternative2': [alternative2], 'game_type': [st.session_state.game_type]}
    df = pd.DataFrame(data)
    if 'responses.csv' in st.session_state:
        existing_df = st.session_state['responses.csv']
        updated_df = pd.concat([existing_df, df], ignore_index=True)
        st.session_state['responses.csv'] = updated_df
        updated_df.to_csv('responses.csv', index=False)
    else:
        st.session_state['responses.csv'] = df
        df.to_csv('responses.csv', index=False)

# Inicializar dataframe na primeira execução
if 'responses.csv' not in st.session_state:
    st.session_state['responses.csv'] = pd.DataFrame(columns=['choice', 'alternative1', 'alternative2', 'game_type'])

# Configuração do Streamlit
st.title("Jogo do Ou")

# Seleção do tipo de jogo
game_type = st.selectbox("Escolha o tipo de jogo:", ["Boas", "Ruins"]) # Removido "Boas + Ruins"

# Armazena o tipo de jogo no estado da sessão
st.session_state.game_type = game_type

# Gerar alternativas iniciais
if 'alternatives' not in st.session_state or st.session_state.game_type != game_type:
    st.session_state['alternatives'] = generate_alternatives(game_type)

alternatives = st.session_state['alternatives']
alternative1 = alternatives[0]
alternative2 = alternatives[1]

# Exibir alternativas
st.write("Você prefere...")
col1, col2 = st.columns(2)
with col1:
    if st.button(alternative1):
        save_response(alternative1, alternative1, alternative2)
        st.session_state['alternatives'] = generate_alternatives(game_type)
        st.experimental_rerun()
with col2:
    if st.button(alternative2):
        save_response(alternative2, alternative1, alternative2)
        st.session_state['alternatives'] = generate_alternatives(game_type)
        st.experimental_rerun()

# Botão para gerar novas alternativas
if st.button("Nova escolha"):
    st.session_state['alternatives'] = generate_alternatives(game_type)
    st.experimental_rerun()