import pandas as pd

df = pd.read_csv('centros_sanitarios-updated.csv')

df_grouped = df.groupby('centro_nro_registro').agg({
    'centro_tipo': 'first',
    'alergologia': lambda x: ', '.join(x.dropna().map(str)),
    'cardiologia': lambda x: ', '.join(x.dropna().map(str)),
    'cirugia_mayor_ambulatoria': lambda x: ', '.join(x.dropna().map(str)),
    'cirugia_menor_ambulatoria': lambda x: ', '.join(x.dropna().map(str)),
    'dermatologia': lambda x: ', '.join(x.dropna().map(str)),
    'endocrinologia': lambda x: ', '.join(x.dropna().map(str)),
    'enfermeria': lambda x: ', '.join(x.dropna().map(str)),
    'farmacia': lambda x: ', '.join(x.dropna().map(str)),
    'fisioterapia': lambda x: ', '.join(x.dropna().map(str)),
    'medicina_general': lambda x: ', '.join(x.dropna().map(str)),
    'neumologia': lambda x: ', '.join(x.dropna().map(str)),
    'neurologia': lambda x: ', '.join(x.dropna().map(str)),
    'nutricion_y_dietetica': lambda x: ', '.join(x.dropna().map(str)),
    'oncologia': lambda x: ', '.join(x.dropna().map(str)),
    'otorrinolaringologia': lambda x: ', '.join(x.dropna().map(str)),
    'pediatria': lambda x: ', '.join(x.dropna().map(str)),
    'psicologia_clinica': lambda x: ', '.join(x.dropna().map(str)),
    'psiquiatria': lambda x: ', '.join(x.dropna().map(str)),
    'rehabilitacion': lambda x: ', '.join(x.dropna().map(str)),
    'reumatologia': lambda x: ', '.join(x.dropna().map(str)),
    'urgencias': lambda x: ', '.join(x.dropna().map(str)),
    'vacunacion': lambda x: ', '.join(x.dropna().map(str)),
    'direccion_completa': 'first',
    'direccion_vial_tipo': 'first',
    'direccion_vial_nombre': 'first',
    'direccion_vial_nro': 'first',
    'direccion_codigo_postal': 'first',
    'municipio_nombre': 'first',
    'localizacion_coordenada_x': 'first',
    'localizacion_coordenada_y': 'first'
}).reset_index()

df_grouped.to_csv("centros_sanitarios-updated-updated.csv")
