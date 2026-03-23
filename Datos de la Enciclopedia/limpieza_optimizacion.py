# Importar libreria para manipulacion de los datos
import pandas as pd

# Leer el archivo CSV
df = pd.read_csv(r"C:\Users\olald\OneDrive\Documentos\GitHub\SparkData_proyecto.pokemon\Datos de la Enciclopedia\datos_pokemon_original.csv")

# Rellenar datos faltantes con la media
df['altura_(m)'] = df['altura_(m)'].fillna(df['altura_(m)'].mean().round(2)) 
df['peso_(kg)'] = df['peso_(kg)'].fillna(df['peso_(kg)'].mean().round(2))

# Limpieza y asignacion de id a cada tipo de pokemon
tipos_limpio = df[['tipo1']].drop_duplicates()
tipos_limpio.rename(columns={'tipo1': 'descripcion'}, inplace=True)
tipos_limpio.sort_values(by='descripcion', ascending=True, inplace=True)
tipos_limpio.insert(0, 'id_tipo', range(1, len(tipos_limpio) + 1))

tipos_lista = sorted(tipos_limpio['descripcion'])
id_con_tipo = []
n = 0
for tipo in tipos_lista:
    n += 1
    tipo = [n, tipo]
    id_con_tipo.append(tipo)

# Limpieza y asignacion de id a cada clasificacion de pokemon
clasificacion_limpio = df[['clasificacion']].drop_duplicates().reset_index(drop=True)
clasificacion_limpio.rename(columns={'clasificacion':'descripcion'}, inplace=True)
clasificacion_limpio.sort_values(by='descripcion', ascending=True, inplace=True)
clasificacion_limpio.insert(0, 'id_clasificacion', range(1, len(clasificacion_limpio) + 1))

clasif_lista = sorted(clasificacion_limpio['descripcion'])
id_con_clasif = []
p = 0
for clasif in clasif_lista:
    p += 1
    clasif = [p, clasif]
    id_con_clasif.append(clasif)

# Funciones para reemplazar tipo y clasificacion con su id correspondiente en el csv pokemones
# por medio de iteración y comparaciones
def definir_tipo(pokemon_id):
    for tipo in id_con_tipo:
        if pokemon_id == tipo[1]:
            pokemon_id = tipo[0]
    return pokemon_id

def definir_clasificacion(pokemon_clasif):
    for clasificacion in id_con_clasif:
        if pokemon_clasif == clasificacion[1]:
            pokemon_clasif = clasificacion[0]
    return pokemon_clasif 

# Actualizacion nombre de columnas
pokemones_limpio = df[['No_Pokedex', 'nombre', 'altura_(m)', 'peso_(kg)', 'tipo1', 'clasificacion', 
                'es_legendario', 'Probabilidad_de_captura', 'Puntos_de_salud', 'velocidad', 'generacion']]
pokemones_limpio.rename(columns={'tipo1':'id_tipo', 
                          'altura_(m)':'altura_m', 
                          'peso_(kg)':'peso_kg', 
                          'clasificacion':'id_clasificacion', 
                          'es_legendario':'legendario', 
                          'Puntos_de_salud':'salud', 
                          'No_Pokedex':'no_pokedex', 
                          'Probabilidad_de_captura':'prob_captura'}, inplace=True)
# Aplicacion de las funciones para asignar id
pokemones_limpio['id_tipo'] = pokemones_limpio['id_tipo'].apply(definir_tipo)
pokemones_limpio['id_clasificacion'] = pokemones_limpio['id_clasificacion'].apply(definir_clasificacion)

# Asignacion de ids, se ordeno de forma ascendente en base a la defensa base
defensas_limpio = df[['No_Pokedex', 'defensa', 'defensa_especial']].reset_index(drop=True)
defensas_limpio.rename(columns={'No_Pokedex':'no_pokedex'}, inplace=True)
defensas_limpio.sort_values(by='defensa', ascending=True, inplace=True)
defensas_limpio.insert(0, 'id_defensa', range(1, len(defensas_limpio) + 1))

# Asignacion de ids, se ordeno de forma ascendente en base al ataque base
ataques_limpio = df[['No_Pokedex', 'ataque', 'ataque_especial']].reset_index(drop=True)
ataques_limpio.rename(columns={'No_Pokedex':'no_pokedex'}, inplace=True)
ataques_limpio.sort_values(by='ataque', ascending=True, inplace=True)
ataques_limpio.insert(0, 'id_ataque', range(1, len(ataques_limpio)+1))

# Asignacion de ids, renombrar columnas y se ordeno de forma ascendente en base al contraataque normal
contraataques_limpio = df[['No_Pokedex', 'contraataque_normal','contraataque_insecto', 'contraataque_siniestro', 'contraataque_dragon', 
                    'contraataque_electrico', 'contraataque_hada', 'contraataque_lucha', 'contraataque_fuego', 
                    'contraataque_volador', 'contraataque_fantasma', 'contraataque_planta', 'contraataque_tierra', 
                    'contraataque_hielo', 'contraataque_veneno', 'contraataque_psiquico', 
                    'contraataque_roca', 'contraataque_acero', 'contraataque_agua']].reset_index(drop=True)
contraataques_limpio.rename(columns={'No_Pokedex':'no_pokedex', 'contraataque_normal':'normal', 'contraataque_insecto':'insecto', 'contraataque_siniestro':'siniestro', 'contraataque_dragon':'dragon', 
                    'contraataque_electrico':'electrico', 'contraataque_hada':'hada', 'contraataque_lucha':'lucha', 'contraataque_fuego':'fuego', 
                    'contraataque_volador':'volador', 'contraataque_fantasma':'fantasma', 'contraataque_planta':'planta', 'contraataque_tierra':'tierra', 
                    'contraataque_hielo':'hielo', 'contraataque_veneno':'veneno', 'contraataque_psiquico':'psiquico', 
                    'contraataque_roca':'roca', 'contraataque_acero':'acero', 'contraataque_agua':'agua'}, inplace=True)
contraataques_limpio.sort_values(by='normal', ascending=True, inplace=True)
contraataques_limpio.insert(0, 'id_contraataque', range(1, len(contraataques_limpio)+1))

# Guardar cada Dataframe en un CSV para generar los inserts
tipos_limpio.to_csv('tipos_sql.csv', index=False, encoding='utf-8')
clasificacion_limpio.to_csv('clasificacion_sql.csv', index=False, encoding='utf-8')
pokemones_limpio.to_csv('pokemones_sql.csv', index=False, encoding='utf-8')
defensas_limpio.to_csv('defensas_sql.csv', index=False, encoding='utf-8')
ataques_limpio.to_csv('ataques_sql.csv', index=False, encoding='utf-8')
contraataques_limpio.to_csv('contraataques_sql.csv', index=False, encoding='utf-8')