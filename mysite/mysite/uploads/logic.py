import pandas as pd
from datetime import datetime

#@TODO cambiar NRO_DNI a nro_documento
#Generamos los campos por defecto para la validación, aquellos archivos que no cuenten con
#estos campos serán rechazados
fields = {
    'headcount': ['EMPRESA','UNIDAD','NOMBRE','FEC_INGRESO','FEC_CESE','NRO_DNI',\
    'FEC_NACIMIENTO','GENERO','PUESTO','AREA','NIVEL','MOT_CESE', 'periodo', 'nro_documento'],\

    'empleado': ['unidad_negocio','periodo','tipo_documento','nro_documento','empresa','fecha_nacimiento',\
    'apellidos_nombres','sexo','estado_civil','nacionalidad','direccion','categoria_ocupacional','tipo_contrato',\
    'sindicalizado','regimen_salud','regimen_pensionario','situación_educativa','tipo_institucion_educativa',\
    'nombre_institucion_educativa','carrera','fecha_ingreso','fecha_cese','motivo_cese','sueldo_basico','porcentaje_bono',\
    'nombre_cargo','metodo_valorizacion','valor_cargo'],\

    u'desempeño': ['unidad_negocio','nro_documento','periodo','empresa','apellidos_nombres',\
    'calificacion_objetivos','calificacion_cometencias','calificacion_desempeno'],\

    'potencial': ['unidad_negocio','nro_documento','periodo','empresa','apellidos_nombres',\
    'calificacion_desempeno','calificacion_potencial','posicion_matriz'],\

    'desarrollo': ['unidad_negocio','nro_documento','periodo','empresa','apellidos_nombres',\
    'tipo_desarrollo','descripcion','fecha_inicio','fecha_fin'],\

    'vacante': ['unidad_negocio','empresa','periodo','codigo_vacante','nombre_cargo','metodo_valorizacion',\
    'valor_cargo','fecha_inicio_proceso','fecha_cierre_proceso','estado_proceso','nro_documento_ingreso',\
    'apellidos_nombres_ingreso','origen_candidato',],\

    'hogan': [],\
}

errors = [
    'El archivo cuenta con filas sin documento de identidad',\
    'El archivo tiene documentos de identidad duplicados',\
    'El archivo no tiene los campos de la plantilla completos',\
    'El archivo esta vacío',\
    'El archivo no corresponde al periodo indicado'\
]

def handle_uploaded_file(file,tipo, periodo):

    try:
        df = pd.read_excel(file,sheet_name='DATA')
    except:
        return False

    if null_check(df) and duplicate_check(df) and field_check(df,tipo) and non_empty_check(df) and time_check(df, periodo):
        return True, []
    else:
        return False, dict(zip(errors,[null_check(df), duplicate_check(df), field_check(df,tipo), non_empty_check(df), time_check(df,periodo)]))

def non_empty_check(df):
    return df.shape[0] > 0

def null_check(df):
    return df[pd.isnull(df['nro_documento'])].shape[0] == 0

def duplicate_check(df):
    return df[df['nro_documento'].duplicated()].shape[0] == 0

def field_check(df,tipo):
    ok = True
    for key in df.keys():
        if key not in fields[tipo]:
            ok = False
    return ok

def time_check(df, periodo):
    return (df['periodo'] == periodo).apply(lambda x: 1 if x else 0).sum() == df.shape[0]
