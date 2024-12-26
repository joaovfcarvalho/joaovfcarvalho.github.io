# Jogo do Ou

# Você Prefere? - Um Jogo de Escolhas Divertidas

Este repositório contém o código-fonte para um jogo web "Você Prefere?", onde os jogadores são apresentados a duas alternativas engraçadas e precisam escolher uma delas. O jogo é construído usando [Streamlit](https://streamlit.io/) e utiliza a API do [Google AI Gemini](https://ai.google.dev/tutorials/python_quickstart) para gerar alternativas criativas e imprevisíveis.

## 🕹️ Funcionalidades

*   **Três Modos de Jogo:**
    *   **Boas:** Escolha entre duas opções positivas e vantajosas.
    *   **Ruins:** Decida entre duas alternativas desagradáveis ou constrangedoras.
    *   **Boas + Ruins:** Enfrente dilemas com um lado positivo e um negativo.
*   **Geração de Alternativas com IA:** As alternativas são geradas dinamicamente usando o modelo de linguagem Gemini da Google AI, garantindo uma experiência sempre nova e divertida.
*   **Exemplos Personalizados:** O modelo de IA é treinado com um conjunto de exemplos fornecidos em `exemplos.txt` para refinar o estilo e o tom do humor.
*   **Interface Simples e Intuitiva:** Desenvolvida com Streamlit para uma experiência de usuário agradável.
*   **Registro de Respostas:** As escolhas dos jogadores são salvas em um arquivo `responses.csv` para análise posterior (opcional).

## 🚀 Como Jogar

O jogo está hospedado no GitHub Pages e pode ser acessado através deste link: [LINK DO SEU JOGO AQUI](https://seu-usuario.github.io/) (substitua `seu-usuario` pelo seu nome de usuário do GitHub).

Basta clicar no link e começar a jogar! Escolha uma das duas alternativas apresentadas ou clique em "Nova Escolha" para gerar um novo par de opções.

## 🛠️ Desenvolvimento

### Pré-requisitos

*   [Python 3.8+](https://www.python.org/downloads/)
*   [Git](https://git-scm.com/downloads)
*   [Chave de API do Google AI Gemini](https://makersuite.google.com/app/apikey)

### Estrutura do Repositório

*   `jogo_do_ou.py`: Código principal do jogo em Streamlit.
*   `requirements.txt`: Lista de dependências do projeto.
*   `exemplos.txt`: Arquivo contendo exemplos de alternativas para treinar a IA.
*   `.streamlit/secrets.toml`: Arquivo de configuração para a chave de API do Gemini (opcional, se você usar segredos do repositório).
*   `setup.sh`: Script de configuração para o GitHub Pages.
*   `README.md`: Este arquivo.

### Configuração

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/seu-usuario/seu-usuario.github.io.git
    cd seu-usuario.github.io
    ```

2. **Crie um ambiente virtual (recomendado):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure a chave de API do Gemini:**

    *   **Opção 1: Usando `.streamlit/secrets.toml` (menos seguro):**
        *   Crie o arquivo `.streamlit/secrets.toml`.
        *   Adicione a seguinte linha, substituindo `"sua_chave_de_api_aqui"` pela sua chave:

            ```toml
            GEMINI_API_KEY = "sua_chave_de_api_aqui"
            ```

    *   **Opção 2: Usando segredos do repositório (recomendado):**
        *   No seu repositório no GitHub, vá em **Settings > Secrets and variables > Actions**.
        *   Clique em **New repository secret**.
        *   **Name:** `GEMINI_API_KEY`
        *   **Secret:** Cole sua chave de API.

5. **Execute o jogo localmente:**

    ```bash
    streamlit run jogo_do_ou.py
    ```

### Branches

*   `main`: Contém a versão estável e atual do jogo.
*   `v1`: Contém a versão antiga do jogo (antes da integração com o Gemini).

### Tags

*   `v1.0`: Marca a versão antiga do jogo (antes da integração com o Gemini).

## 🤝 Contribuição

Contribuições são bem-vindas! Se você quiser melhorar o jogo, siga estas etapas:

1. Faça um fork do repositório.
2. Crie um novo branch para sua funcionalidade (`git checkout -b feature/sua-funcionalidade`).
3. Faça commit das suas alterações (`git commit -m "Adiciona funcionalidade X"`).
4. Envie o branch (`git push origin feature/sua-funcionalidade`).
5. Abra um Pull Request.

## 📝 Licença

Este projeto está licenciado sob a [MIT License](LICENSE) - consulte o arquivo [LICENSE](LICENSE) para obter detalhes. (Você pode alterar a licença conforme necessário).

## ✉️ Contato

Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para abrir uma issue neste repositório.

---

**Lembre-se de substituir:**

*   `seu-usuario` pelo seu nome de usuário do GitHub.
*   `LINK DO SEU JOGO AQUI` pelo link real do seu jogo no GitHub Pages.
*   Informações de licença, se necessário.

Este `README.md` fornece uma boa visão geral do seu projeto, instruções de como jogar e informações para desenvolvedores que desejam contribuir ou executar o jogo localmente. Ele também explica a estrutura de branches e tags para manter o controle das versões.