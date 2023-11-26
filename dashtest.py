import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Carregue os dados
caminho_arquivo = 'dados_temperatura_global.csv'
dados = pd.read_csv(caminho_arquivo)

# Inicialize o aplicativo Dash
app = dash.Dash(__name__)

# Layout do aplicativo
app.layout = html.Div([
    html.H1("Variação da Temperatura Global ao Longo do Tempo"),
    
    dcc.Graph(
        id='grafico-temperatura',
        figure=px.line(dados, x=dados.index, y=dados.columns[1])
    )
])

# Inicie o servidor
if __name__ == '__main__':
    app.run_server(debug=True)
