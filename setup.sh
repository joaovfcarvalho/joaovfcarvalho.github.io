#!/bin/bash
mkdir -p ~/.streamlit

echo "[general]" > ~/.streamlit/credentials.toml
echo "email = \"jogodoou99999@gmail.com\"" >> ~/.streamlit/credentials.toml

echo "[server]" >> ~/.streamlit/config.toml
echo "headless = true" >> ~/.streamlit/config.toml
echo "enableCORS = false" >> ~/.streamlit/config.toml
echo "port = \$PORT" >> ~/.streamlit/config.toml

# Copie o arquivo de exemplos para o diretório onde o Streamlit está sendo executado
cp exemplos.txt .