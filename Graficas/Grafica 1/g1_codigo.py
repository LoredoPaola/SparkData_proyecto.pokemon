
# GRAFICA 1: TOP 10 MEJORES POKEMON POR TIPO

import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

# CONEXION A MYSQL
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="k1mpata7a",
    database="enciclopedia_pokemon"
)

# CONSULTA 
query = """
SELECT 
    p.nombre,
    t.descripcion AS tipo,
    a.ataque,
    d.defensa,
    p.velocidad
FROM pokemones p
JOIN tipos t ON p.id_tipo = t.id_tipo
JOIN ataques a ON p.no_pokedex = a.no_pokedex
JOIN defensas d ON p.no_pokedex = d.no_pokedex
"""

df = pd.read_sql(query, conexion)

# CREAR SCORE
df['score'] = df['ataque'] + df['defensa'] + df['velocidad']

#  TOP 10 GLOBAL 
top10 = df.sort_values(by='score', ascending=False).head(10)

print("Top 10 Pokemon:")
print(top10)


# COLORES POR TIPO 
colores_tipo = {
    'fire': 'red',
    'water': 'blue',
    'grass': 'green',
    'electric': 'yellow',
    'rock': 'gray',
    'psychic': 'purple',
    'ice': 'cyan',
    'dragon': 'orange',
    'ground': 'brown',
    'bug': 'olive',
    'steel': 'silver'
}

# Asignar colores
colores = [colores_tipo.get(t, 'black') for t in top10['tipo']]

# CREAR GRAFICA
plt.figure()

plt.bar(top10['nombre'], top10['score'], color=colores)

# Etiquetas con tipo
labels = [f"{n}\n({t})" for n, t in zip(top10['nombre'], top10['tipo'])]
plt.xticks(range(len(labels)), labels, rotation=45)

# Títulos
plt.title("Top 10 Mejores Pokemon por Tipo")
plt.xlabel("Pokemon (Tipo)")
plt.ylabel("Score")

plt.tight_layout()

# Mostrar 
plt.show()

# CERRAR CONEXION

conexion.close()