from bokeh.plotting import figure, ColumnDataSource
from bokeh.resources import CDN
from bokeh.layouts import gridplot
from bokeh.embed import components
from math import pi
import pandas as pd
import numpy as np
from datetime import date


def charts(file, tipo):

    df = pd.read_excel(file, sheet_name = 'DATA')

    if tipo == 'headcount':

        source_genero = ColumnDataSource(data = dict(x=df['GENERO'].unique().tolist(), y=(df['GENERO'].value_counts()/df.shape[0]).values.tolist()))

        df['edad'] = df['FEC_NACIMIENTO'].apply(calculate_age)
        measured = df['edad'].values
        hist, edges = np.histogram(measured, density=True, bins='auto')

        s1 = figure(plot_width=250, plot_height=250, title=u'Distribución de Géneros', x_range=df['GENERO'].unique().tolist())
        s1.vbar(x='x', top='y', width=0.9, source=source_genero)

        s2 = figure(plot_width=250, plot_height=250, title='Distribución de Edades')
        s2.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], fill_color="#036564", line_color="#033649")

        plots = [s1,s2]

        script, div = components(gridplot(plots, ncols=3), CDN)
        return script, div

def datasummary(file):

    df = pd.read_excel(file, sheet_name = 'DATA')
    total_missings = {}
    for key in df.keys():
        total_missings[key] = df[key].isnull().sum()
    missings_df = pd.DataFrame.from_dict(total_missings, orient='index').rename(columns={0:'N° de Faltantes'})
    missings_df['N° de Registros'] = df.count()
    return missings_df.T.to_html()

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
