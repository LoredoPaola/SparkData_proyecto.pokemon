import pandas as pd
import matplotlib.pyplot as plt

# 1. Crear los datos externos (Ratio de captura de 3 a 255)
# Un ratio de 3 equivale a una probabilidad de captura del 0.4% con una Pokéball normal a salud completa.
datos_pokemon = {
    'Pokemon': [
        'Mewtwo (Legendario)', 'Lugia (Legendario)', 'Ho-Oh (Legendario)', 
        'Arceus (Dios Pokémon)', 'Darkrai (Singular)', 'Deoxys (Singular)', 
        'Groudon (Legendario)', 'Kyogre (Legendario)', 'Rayquaza (Legendario)', 
        'Beldum (Normal/Acero)', 'Pidgey (REFERENCIA)'
    ],
    'Ratio_Captura': [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 255]
}

# 2. Convertir a DataFrame de Pandas
df = pd.DataFrame(datos_pokemon)

# Invertir el orden para que el Top 1 quede arriba en la gráfica horizontal
df = df.iloc[::-1].reset_index(drop=True)

# 3. Configurar la gráfica
plt.figure(figsize=(10, 6))

# Dibujar barras horizontales. Pintaremos a Pidgey de verde (fácil) y al resto de rojo (difícil)
colores = ['#4CAF50' if x == 255 else '#E3350D' for x in df['Ratio_Captura']]
barras = plt.barh(df['Pokemon'], df['Ratio_Captura'], color=colores, edgecolor='black')

# 4. Personalización y textos
plt.title('Top 10 Pokémon más difíciles de capturar (vs Pidgey)', fontsize=15, fontweight='bold')
plt.xlabel('Ratio de Captura (Más bajo = Más difícil)', fontsize=12)
plt.ylabel('Pokémon', fontsize=12)

# Añadir el número exacto a un lado de cada barra
for barra in barras:
    ancho = barra.get_width()
    plt.text(ancho + 5, barra.get_y() + barra.get_height()/2, 
             f'{int(ancho)}', va='center', fontsize=10)

plt.grid(axis='x', linestyle='--', alpha=0.5)

# Mostrar la gráfica
plt.tight_layout()
plt.show()