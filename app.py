import pandas as pd
import streamlit as st 

# Título do Projeto
st.title("🌍 Dashboard ODS 13 - Monitoramento Climático")

#Descrição do problema de negócio
st.header("📌 Sobre o Projeto")
st.divider()
st.subheader("Problema de Negócio")
st.write(
    "A falta de centralização e de visualização simples de dados meteorológicos "
    "dificulta o acompanhamento de variações de temperatura e umidade. "
    "Isso prejudica a tomada de decisão de ONGs, gestores locais e voluntários."
    )
st.divider()
st.subheader("Objetivo do Projeto")
st.write(
    "• Democratizar o acesso a informações climáticas regionais.\n"
    "• Facilitar a análise de dados meteorológicos através de um painel simples e interativo.\n"
    "• Apoiar ações socioambientais alinhadas ao ODS 13 (Ação Contra a Mudança Global do Clima)."
)  

# Links úteis

st.header("🔗 Links Úteis e Fontes de Inspiração")

st.markdown("- [Conecta Brasil](https://conectabrasil.org/home) - Plataforma de engajamento e apoio a causas sociais.")
st.markdown("- [Observatório do 3º Setor](https://observatorio3setor.org.br/carrossel/lista-conheca-projetos-sociais-de-15-causas-diferentes/) - Divulgação de projetos socioambientais.")
st.markdown("- [ODS 13 - Nações Unidas](https://brasil.un.org/pt-br/sdgs/13) - Detalhes sobre a meta global contra mudanças climáticas.")      

# 4. Tabela demo com dados fictícios somente para demonstração

st.header("📊 Amostra dos Dados do Projeto")
st.write("Abaixo está uma amostra simplificada dos dados meteorológicos que serão utilizados e analisados ao longo do projeto:")

#Criando a tabela em forma de dicionário do python
dados_exemplo = {
    "Data": ["2026-08-15", "2026-08-16", "2026-08-17", "2026-08-18", "2026-08-19"],
    "Cidade": ["São Paulo", "São Paulo", "São Paulo", "São Paulo", "São Paulo"],
    "Temperatura (°C)": [24.5, 26.0, 28.2, 23.0, 25.5],
    "Umidade (%)": [65, 60, 55, 75, 70],
    "Precipitação (mm)": [0.0, 0.0, 2.5, 12.0, 0.0]
}

#criando o dataframe com o dicionário
df= pd.DataFrame(dados_exemplo)

#exibindo a tabela no Stremlit
st.dataframe(df)
