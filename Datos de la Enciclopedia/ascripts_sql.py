import pandas as pd

pokemones = pd.read_csv(r"C:\Users\olald\OneDrive\Documentos\GitHub\SparkData_proyecto.pokemon\Datos de la Enciclopedia\pokemones_sql.csv")

with open('inserts_pokemones.sql', 'w', encoding='utf-8') as f:
    f.write("-- INSERTS para tabla Pokemones\n\n")

    for _, row in pokemones.iterrows():
        f.write(f"INSERT INTO pokemones (no_pokedex, nombre, altura_m, peso_kg, id_tipo, id_clasificacion, legendario, prob_captura, salud, velocidad, generacion) "
                f"VALUES ({row['no_pokedex']}, '{row['nombre']}', {row['altura_m']}, {row['peso_kg']}, {row['id_tipo']}, {row['id_clasificacion']}, " 
                f"{row['legendario']}, {row['prob_captura']}, {row['salud']}, {row['velocidad']}, {row['generacion']});\n")
        
print(f"Archivo 'inserts_pokemones.sql' generado con {len(pokemones)} registros")

tipos = pd.read_csv(r"C:\Users\olald\OneDrive\Documentos\GitHub\SparkData_proyecto.pokemon\Datos de la Enciclopedia\tipos_sql.csv")

with open('inserts_tipos.sql', 'w', encoding='utf-8') as f:
    f.write("-- INSERTS para tabla tipos\n\n")

    for _, row in tipos.iterrows():
        f.write(f"INSERT INTO tipos (id_tipo, descripcion) "
                f"VALUES ({row['id_tipo']}, '{row['descripcion']}');\n")
        
print(f"Archivo 'inserts_tipos.sql' generado con {len(tipos)} registros")

clasificaciones = pd.read_csv(r"C:\Users\olald\OneDrive\Documentos\GitHub\SparkData_proyecto.pokemon\Datos de la Enciclopedia\clasificacion_sql.csv")

with open('inserts_clasificacion.sql', 'w', encoding='utf-8') as f:
    f.write("-- INSERTS para tabla clasificacion\n\n")

    for _, row in clasificaciones.iterrows():
        f.write(f"INSERT INTO clasificacion (id_clasificacion, descripcion) "
                f"VALUES ({row['id_clasificacion']}, '{row['descripcion']}');\n")
        
print(f"Archivo 'inserts_clasificacion.sql' generado con {len(clasificaciones)} registros")

defensas = pd.read_csv(r"C:\Users\olald\OneDrive\Documentos\GitHub\SparkData_proyecto.pokemon\Datos de la Enciclopedia\defensas_sql.csv")

with open('inserts_defensas.sql', 'w', encoding='utf-8') as f:
    f.write("-- INSERTS para tabla defensas\n\n")

    for _, row in defensas.iterrows():
        f.write(f"INSERT INTO defensas (id_defensa, no_pokedex, defensa, defensa_especial) "
                f"VALUES ({row['id_defensa']}, {row['no_pokedex']}, {row['defensa']}, {row['defensa_especial']});\n")
        
print(f"Archivo 'inserts_defensas.sql' generado con {len(defensas)} registros")

ataques = pd.read_csv(r"C:\Users\olald\OneDrive\Documentos\GitHub\SparkData_proyecto.pokemon\Datos de la Enciclopedia\ataques_sql.csv")

with open('inserts_ataques.sql', 'w', encoding='utf-8') as f:
    f.write("-- INSERTS para tabla ataques\n\n")

    for _, row in ataques.iterrows():
        f.write(f"INSERT INTO ataques (id_ataque, no_pokedex, ataque, ataque_especial) "
                f"VALUES ({row['id_ataque']}, {row['no_pokedex']}, {row['ataque']}, {row['ataque_especial']});\n")
        
print(f"Archivo 'inserts_ataques.sql' generado con {len(ataques)} registros")

contraataques = pd.read_csv(r"C:\Users\olald\OneDrive\Documentos\GitHub\SparkData_proyecto.pokemon\Datos de la Enciclopedia\contraataques_sql.csv")

with open('inserts_contraataques.sql', 'w', encoding='utf-8') as f:
    f.write("-- INSERTS para tabla contraataques\n\n")

    for _, row in contraataques.iterrows():
        f.write(f"INSERT INTO contraataques (id_contraataque, no_pokedex, normal, insecto, siniestro, dragon, electrico, hada, lucha, fuego, volador, " 
                f"fantasma, planta, tierra, hielo, veneno, psiquico, roca, acero, agua) "
                f"VALUES ({row['id_contraataque']}, {row['no_pokedex']}, {row['normal']}, {row['insecto']}, {row['siniestro']}, {row['dragon']}, "
                f"{row['electrico']}, {row['hada']}, {row['lucha']}, {row['fuego']}, {row['volador']}, {row['fantasma']}, {row['planta']}, {row['tierra']}, "
                f"{row['hielo']}, {row['veneno']}, {row['psiquico']}, {row['roca']}, {row['acero']}, {row['agua']});\n")
        
print(f"Archivo 'inserts_contraataques.sql' generado con {len(contraataques)} registros")