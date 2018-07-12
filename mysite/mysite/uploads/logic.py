import pandas as pd

#Generamos los campos por defecto para la validación, aquellos archivos que no cuenten con
#estos campos serán rechazados
fields = {
    'headcount': ['EMPRESA','UNIDAD','NOMBRE','FEC_INGRESO','FEC_CESE','NRO_DNI',\
    'FEC_NACIMIENTO','GENERO','PUESTO','AREA','NIVEL','MOT_CESE'],\
    'dcp':[],\

    'empleado': ['empresa','tipo_documento','nro_documento','fecha_nacimiento','apellidos_nombres',\
    'sexo','estado_civil','nacionalidad','direccion','categoria_ocupacional','tipo_contrato',\
    'sindicalizado','regimen_salud','regimen_pensionario','situación_educativa','tipo_institucion_educativa',\
    'nombre_institucion_educativa','carrera','fecha_ingreso','fecha_cese','motivo_cese',\
    'sueldo_basico','porcentaje_bono','nombre_cargo','metodo_valorizacion','valor_cargo'],\

    u'desempeño': ['empresa','tipo_documento','nro_documento','apellidos_nombres',\
    'calificacion_objetivos','calificacion_cometencias','calificacion_desempeno'],\

    'potencial': ['empresa','tipo_documento','nro_documento','apellidos_nombres',\
    'calificacion_desempeno','calificacion_potencial','posicion_matriz'],\

    'desarrollo': [],\

    'vacante': [],\

    'hogan': [],\
}

def handle_uploaded_file(file,tipo):

    try:
        df = pd.read_excel(file,sheet_name='DATA')
    except:
        return False
    if null_check(df) and duplicate_check(df) and field_check(df,tipo):
        return True
    else:
        return False

def null_check(df):
    return df[pd.isnull(df['NRO_DNI'])].shape[0] == 0

def duplicate_check(df):
    return df[df['NRO_DNI'].duplicated()].shape[0] == 0

def field_check(df,tipo):
    ok = True
    for key in df.keys():
        if key not in fields[tipo]:
            ok = False
    return ok
