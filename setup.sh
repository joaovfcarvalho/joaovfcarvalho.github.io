#!/bin/bash
mkdir -p ~/.streamlit

echo "[general]" > ~/.streamlit/credentials.toml
echo "email = \"joaovfernandescarvalho@gmail.com\"" >> ~/.streamlit/credentials.toml

echo "[server]" >> ~/.streamlit/config.toml
echo "headless = true" >> ~/.streamlit/config.toml
echo "enableCORS = false" >> ~/.streamlit/config.toml
echo "port = \$PORT" >> ~/.streamlit/config.toml