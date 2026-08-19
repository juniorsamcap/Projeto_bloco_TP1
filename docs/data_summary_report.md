# Data Summary Report (Esboço Inicial)

## 1. Fontes de Dados Mapeadas

| Fonte | Tipo de Dado | Método de Coleta | Objetivo de Uso |
| :--- | :--- | :--- | :--- |
| **Open-Meteo API** | Meteorológico (Histórico e Previsão) | API REST (JSON via Python `requests`) | Obter séries temporais de temperatura, umidade e precipitação por coordenadas geográficas. |
| **Dados Amostrais (CSV Local)** | Histórico Metrológico Local | Arquivo `.csv` tabular | Servir de *fallback* para simulações e renderização rápida na fase Demo da aplicação. |

## 2. Variáveis Principais
* `datetime`: Data e hora da medição.
* `temperature_2m`: Temperatura do ar a 2 metros de altura (°C).
* `relative_humidity_2m`: Umidade relativa do ar (%).
* `precipitation`: Precipitação acumulada (mm).