import dash
import dash_core_components as dcc
import dash_html_components as html
import psycopg2

try:
    minhacon = psycopg2.connect(host='localhost',
                                user='postgres',
                                password='pgsql',
                                dbname='dwcorrecao',
                                port=5495)
    print('Conexão ok')
except:
    minhacon = 0
    print('Conexão com problemas')


curFatoLicitacao = minhacon.cursor()
curFatoLicitacao.execute("select ano, count(*) as qtd "
                         "from fato_licitacao "
                         "group by ano")

registros = curFatoLicitacao.fetchall()


ano = []
qtd = []
for licitacoes in registros:
    print('Ano = '+ str(licitacoes[0])+' Qtd = '+str(licitacoes[1]))
    ano.append(licitacoes[0])
    qtd.append(licitacoes[1])

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Exemplo Gráfico'),


    dcc.Graph(
        figure={
            'data':[
                {'x': ano , 'y': qtd,
                 'type': 'bar', 'name':'Licitação por ano'}
            ],
            'layout':{
                'title':'Licitação'
            }

        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True, port=9954)