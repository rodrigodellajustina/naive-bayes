import dash
import dash_core_components as dcc
import dash_html_components as html

dados = {'Ano':['2001', '2002', '2003'],
         'Qtd':[43,44,45]}

mgr_options = [2001,2002,2003,2004,2005]

app = dash.Dash()

app.layout = html.Div([
    html.H2("Licitações por Ano"),
    html.Div(
        [
            dcc.Dropdown(
                id="licitacao",
                options=[{
                    'label': i,
                    'value': i
                } for i in mgr_options],
                value='Todas as Licitações'),
        ],
        style={'width': '25%',
               'display': 'inline-block'}),
    dcc.Graph(id='funnel-graph'),
])

@app.callback(
    dash.dependencies.Output('funnel-graph', 'figure'),
    [dash.dependencies.Input('licitacao', 'value')])
def update_graph(licitacao):
    if licitacao == "Todas as Licitações":
        df_plot = dados.copy()
    else:
        df_plot = dados[dados['Ano'] == licitacao]

    return {
        'data':[
                {'x': dados['Ano'], 'y': dados['qtd'],
                 'type': 'bar', 'name':'Licitação por ano'}
            ],
        'layout':{
                'title':'Licitação por ano'
            }
    }




if __name__ == '__main__':
    app.run_server(debug=True)