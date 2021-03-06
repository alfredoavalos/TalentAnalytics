from bokeh.plotting import figure, ColumnDataSource
from bokeh.resources import CDN
from bokeh.layouts import gridplot
from bokeh.embed import components
import holoviews as hv
from math import pi
import pandas as pd
import numpy as np
from datetime import date

hv.extension("bokeh")

def charts(file, tipo):

    df = pd.read_excel(file, sheet_name = 'DATA')

    if tipo == 'empleado':

        categorical_fields = ['sexo','estado_civil','nacionalidad','categoria_ocupacional',\
        'tipo_contrato','sindicalizado','regimen_salud','regimen_pensionario','situación_educativa',\
        'tipo_institucion_educativa','motivo_cese']

        df['edad'] = df['fecha_nacimiento'].apply(calculate_age)
        df['antiguedad'] = df['fecha_ingreso'].apply(calculate_age)

        plots = []

        plots.extend([categorical_barplot(df, field) for field in categorical_fields])
        plots.extend([scatter_bonos(df),histograma(df, 'edad'),histograma(df, 'antiguedad')])

        script, div = components(gridplot(plots, ncols=2), CDN)
        return script, div

    if tipo == u'desempeño':

        categorical_fields = ['sexo','estado_civil','nacionalidad','categoria_ocupacional',\
        'tipo_contrato','sindicalizado','regimen_salud','regimen_pensionario','situación_educativa',\
        'tipo_institucion_educativa','motivo_cese']

        df['edad'] = df['fecha_nacimiento'].apply(calculate_age)
        df['antiguedad'] = df['fecha_ingreso'].apply(calculate_age)

        plots = []

        plots.extend([categorical_barplot(df, field) for field in categorical_fields])
        plots.extend([scatter_bonos(df),histograma(df, 'edad'),histograma(df, 'antiguedad')])

        script, div = components(gridplot(plots, ncols=2), CDN)
        return script, div

    if tipo == 'vacante':

        categorical_fields = ['sexo','estado_civil','nacionalidad','categoria_ocupacional',\
        'tipo_contrato','sindicalizado','regimen_salud','regimen_pensionario','situación_educativa',\
        'tipo_institucion_educativa','motivo_cese']

        df['edad'] = df['fecha_nacimiento'].apply(calculate_age)
        df['antiguedad'] = df['fecha_ingreso'].apply(calculate_age)

        plots = []

        plots.extend([categorical_barplot(df, field) for field in categorical_fields])
        plots.extend([scatter_bonos(df),histograma(df, 'edad'),histograma(df, 'antiguedad')])

        script, div = components(gridplot(plots, ncols=2), CDN)
        return script, div

    if tipo == 'potencial':

        categorical_fields = ['sexo','estado_civil','nacionalidad','categoria_ocupacional',\
        'tipo_contrato','sindicalizado','regimen_salud','regimen_pensionario','situación_educativa',\
        'tipo_institucion_educativa','motivo_cese']

        df['edad'] = df['fecha_nacimiento'].apply(calculate_age)
        df['antiguedad'] = df['fecha_ingreso'].apply(calculate_age)

        plots = []

        plots.extend([categorical_barplot(df, field) for field in categorical_fields])
        plots.extend([scatter_bonos(df),histograma(df, 'edad'),histograma(df, 'antiguedad')])

        script, div = components(gridplot(plots, ncols=2), CDN)
        return script, div

    if tipo == 'hogan':

        categorical_fields = ['sexo','estado_civil','nacionalidad','categoria_ocupacional',\
        'tipo_contrato','sindicalizado','regimen_salud','regimen_pensionario','situación_educativa',\
        'tipo_institucion_educativa','motivo_cese']

        df['edad'] = df['fecha_nacimiento'].apply(calculate_age)
        df['antiguedad'] = df['fecha_ingreso'].apply(calculate_age)

        plots = []

        plots.extend([categorical_barplot(df, field) for field in categorical_fields])
        plots.extend([scatter_bonos(df),histograma(df, 'edad'),histograma(df, 'antiguedad')])

        script, div = components(gridplot(plots, ncols=2), CDN)
        return script, div

def datasummary(file):

    df = pd.read_excel(file, sheet_name = 'DATA')
    total_missings = {}
    for key in df.keys():
        total_missings[key] = df[key].isnull().sum()
    missings_df = pd.DataFrame.from_dict(total_missings, orient='index').rename(columns={0:'N° de Faltantes'})
    missings_df['N° de Registros'] = df.count()
    return missings_df[missings_df['N° de Faltantes'] > 0].to_html(classes="table table-hover")

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def scatter_bonos(df):
    f = figure(plot_width=500, plot_height=300, title=u'Distribución de Porcentaje de Bono por Valor de Cargo', x_range=df['valor_cargo'].unique())
    f.scatter(x=df['valor_cargo'].unique(), y= df['porcentaje_bono'])
    return f

def violin_areas(df):
    violin = hv.Violin(df, ('nombre_area', 'Area'), ('edad', 'Edad'))
    violin.options(height=500, width=500)
    return hv.renderer('bokeh').instance(mode='server').get_plot(violin).state

def violin_sueldos(df):
    violin = hv.Violin(df, ('valor_cargo', 'Valor de Cargo'), ('sueldo_basico', 'Sueldo'))
    violin.options(height=500, width=500)
    return hv.renderer('bokeh').instance(mode='server').get_plot(violin).state

def histograma(df,field):
    hist, edges = np.histogram(df[field].values, density=True, bins='auto')
    f = figure(plot_width=500, plot_height=300, title='Distribución de {}'.format(field))
    f.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], fill_color="#036564", line_color="#033649")
    return f

def categorical_barplot(df,field):
    #y is the categorical field name, x is the value count percentage
    #.format(' '.join(field.split('_')).lower().title())
    df = df[~pd.isnull(df[field])]
    f = figure(plot_width=500, plot_height=300, title=u'Distribución de {}'.format(' '.join(field.split('_')).lower().title()), y_range=df[field].unique())
    f.hbar(y=df[field].unique(), height=0.2, right=df[field].value_counts()/df.shape[0])
    return f
