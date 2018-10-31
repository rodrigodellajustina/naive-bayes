import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:pgsql@localhost:5495/dwcorrecao")

#Get data from database. Use groupby here to get the least amount of data from db,
#this will give us more speed
df = pd.read_sql('''
                    select ano, sum(valor_total) as valor_total From fato_licitacao
                    group by ano
                    
                    ''', con=engine)
df = df.fillna('')

#Let's sort the data so we can see values from smaller to bigger
df = df.sort_values(['valor_total'])

#We do all the plotting here
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

init_notebook_mode(connected=True)

iplot([go.Bar(
            x=df['ano'],
            y=df['valor_total'],
)])