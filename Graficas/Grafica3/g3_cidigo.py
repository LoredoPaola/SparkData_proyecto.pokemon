import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import numpy as np

# 1. CONEXIÓN A MYSQL
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="alfaybella53",
    database="enciclopedia_pokemon"
)

# 2. CONSULTA
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

# 3. FILTRAR TOP 10
df['balance'] = df['ataque'] + df['defensa']
top10_comp = df.sort_values(by='balance', ascending=False).head(10)

# 4. CONFIGURACIÓN DE LA GRÁFICA
plt.figure(figsize=(12, 7))

x = np.arange(len(top10_comp['nombre'])) 
width = 0.35 

# CAMBIO DE COLORES: Fortaleza -> Verde (#2ecc71) | Debilidad -> Azul (#3498db)
rects1 = plt.bar(x - width/2, top10_comp['ataque'], width, label='Fortaleza (Ataque)', color='#2ecc71', edgecolor='black')
rects2 = plt.bar(x + width/2, top10_comp['defensa'], width, label='Debilidad (Defensa)', color='#3498db', edgecolor='black')

# 5. PERSONALIZACIÓN
plt.title('Comparativa: Fortaleza (Atk) vs Debilidad (Def) - Top 10', fontsize=14, fontweight='bold')
plt.xlabel('Pokémon y su Tipo', fontsize=12)
plt.ylabel('Puntos de Estadística', fontsize=12)

labels = [f"{n}\n({t})" for n, t in zip(top10_comp['nombre'], top10_comp['tipo'])]
plt.xticks(x, labels, rotation=45)

plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.3)

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.annotate(f'{int(height)}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), 
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=9)

autolabel(rects1)
autolabel(rects2)

plt.tight_layout()
plt.show()

# 6. CERRAR CONEXIÓN
conexion.close()