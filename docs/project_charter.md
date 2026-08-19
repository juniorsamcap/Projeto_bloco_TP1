# Documentação do Projeto - Dashboard ODS 13

## 1. Definição do Problema de Negócio

### Problema de Negócio
A falta de centralização e de visualização simples de dados meteorológicos e climáticos dificulta o acompanhamento do aumento de temperaturas, da variação de umidade e da ocorrência de eventos extremos por parte de cidadãos, pesquisadores e gestores locais. 

### Fundamentação e Contexto Social
A relevância deste projeto apoia-se no fortalecimento do ecossistema do Terceiro Setor brasileiro — inspirado por iniciativas mapeadas em portais como o *Observatório do 3º Setor* e por redes de engajamento como o *Conecta Brasil*. Nestas plataformas, evidencia-se que a falta de dados ambientais acessíveis e estruturados em formato visual prejudica a tomada de decisão ágil e o planejamento de ações de impacto socioambiental por parte de ONGs e voluntários.

### Metas e Indicadores de Sucesso (KPIs)
* **Meta Principal:** Desenvolver e publicar uma aplicação web interativa em Python/Streamlit que consolide e apresente indicadores climáticos de forma intuitiva.
* **KPI 1 (Desempenho):** Tempo de renderização dos gráficos e dashboards inferior a 3 segundos.
* **KPI 2 (Disponibilidade):** Garantir 98% de taxa de sucesso nas requisições aos dados climáticos.
* **KPI 3 (Usabilidade):** Permitir a filtragem e atualização da visualização por cidade e período temporal em até 3 cliques.

### ODS Atendido
* **ODS 13 – Ação Contra a Mudança Global do Clima:** A aplicação atende ao ODS 13 ao democratizar o acesso a informações meteorológicas e climáticas, promovendo conscientização pública e fornecendo dados essenciais para o planejamento preventivo contra os impactos das mudanças climáticas regionais.

### Público-Alvo
* Cidadãos interessados no monitoramento do clima local.
* Gestores de ONGs ambientais e projetos sociais.
* Pesquisadores e estudantes da área socioambiental.

---

## 2. Metodologia e Ciclo de Vida do Projeto

A condução técnica do projeto integra a abordagem orientada a dados do **CRISP-DM** com o gerenciamento ágil e estruturado do **TDSP (Team Data Science Process)**.

### Mapeamento CRISP-DM
1. **Business Understanding (Entendimento do Negócio):** Mapeamento das dores do Terceiro Setor, definição das métricas climáticas relevantes e alinhamento do escopo ao ODS 13.
2. **Data Understanding (Entendimento dos Dados):** Identificação das fontes de dados meteorológicos (arquivos CSV históricos e/ou requisições à API Open-Meteo) para verificar consistência e granularidade.
3. **Data Preparation (Preparação dos Dados):** Limpeza de dados nulos, conversão de tipos de datas e estruturação das tabelas utilizando a biblioteca **Pandas**.
4. **Modeling (Modelagem/Visualização):** Construção da camada de apresentação e gráficos dinâmicos de linha, barra e métricas no **Streamlit**.
5. **Evaluation (Avaliação):** Validação da usabilidade da interface, checagem dos KPIs de desempenho e testes de navegação dos filtros.
6. **Deployment (Implantação):** Publicação do código-fonte no **GitHub** mantendo a `.venv` isolada e deploy contínuo na nuvem via **Streamlit Cloud**.

---

### Mapeamento das Fases do TDSP
1. **Entendimento do Negócio (Business Understanding):** Definição do problema, levantamento do público-alvo, escopo do projeto de bloco e criação do arquivo de documentação.
2. **Aquisição e Compreensão dos Dados (Data Acquisition and Understanding):** Conexão com as fontes de dados climáticos, ingestão de dados para o ambiente virtual de desenvolvimento e análise exploratória inicial.
3. **Modelagem e Desenvolvimento (Modeling):** Engenharia de recursos (cálculo de médias móveis, máximas e mínimas) e desenvolvimento do painel interativo (`app.py`).
4. **Implantação (Deployment):** Configuração do pipeline de entrega contínua integrando o repositório do GitHub com o ambiente de hospedagem do Streamlit.
5. **Aceite do Cliente/Usuário (Customer Acceptance):** Disponibilização do link público do dashboard e validação final dos requisitos em relação às diretrizes do Projeto de Bloco.