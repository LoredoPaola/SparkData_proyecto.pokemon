import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# 1. Configurar conexión a tu base de datos MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'charlotte23',
    'database': 'enciclopedia_pokemon'
}

try:
    print("Extrayendo estadísticas detalladas desde MySQL...")
    conexion = mysql.connector.connect(**db_config)
    
    # 2. SQL Enriquecido: Ahora traemos Ataque, Ataque Especial, Velocidad y Multiplicador
    query = """
        SELECT p.nombre, 
               t.descripcion AS tipo_principal,
               a.ataque,
               a.ataque_especial,
               p.velocidad,
               (a.ataque + a.ataque_especial + p.velocidad) AS poder_ofensivo,
               c.psiquico AS multiplicador_psiquico
        FROM pokemones p
        JOIN ataques a ON p.no_pokedex = a.no_pokedex
        JOIN contraataques c ON p.no_pokedex = c.no_pokedex
        JOIN tipos t ON p.id_tipo = t.id_tipo
        WHERE p.generacion <= 7 
          AND p.legendario = 0
          AND c.psiquico <= 0.5 
        ORDER BY poder_ofensivo DESC
        LIMIT 4;
    """
    
    df = pd.read_sql(query, conexion)
    
    # 3. Cálculo Matemático de Contribución al Daño
    poder_total_equipo = df['poder_ofensivo'].sum()
    df['aporte_dano'] = (df['poder_ofensivo'] / poder_total_equipo * 100).round().astype(int)
    df.loc[3, 'aporte_dano'] = 100 - df['aporte_dano'][0:3].sum() # Ajuste al 100%

    # 4. Crear "Fichas Técnicas" (Etiquetas enriquecidas con multi-línea)
    etiquetas_detalladas = []
    for index, fila in df.iterrows():
        # Traducir el multiplicador numérico a texto legible
        resistencia = "INMUNE (0x daño)" if fila['multiplicador_psiquico'] == 0.0 else "RESISTE (0.5x daño)"
        
        # Armar el bloque de texto
        texto = (f"{fila['nombre'].upper()} - Daño: {fila['aporte_dano']}%\n"
                 f"Tipo: {fila['tipo_principal'].capitalize()} | {resistencia}\n"
                 f"⚔️ Atk: {fila['ataque']} | 🔮 SpA: {fila['ataque_especial']} | 💨 Vel: {fila['velocidad']}")
        etiquetas_detalladas.append(texto)

    # 5. Generar Gráfico de Anillo
    # Hacemos la figura un poco más ancha (14, 8) para que quepa todo el texto
    fig, ax = plt.subplots(figsize=(14, 8), subplot_kw=dict(aspect="equal"))
    
    colores = ["#E6E631", "#38D059", '#5880E0', '#78D0D0']
    
    wedges, texts = ax.pie(df['aporte_dano'], colors=colores, startangle=90, 
                           wedgeprops=dict(width=0.35, edgecolor='white', linewidth=2))

    # Círculo blanco central
    centre_circle = plt.Circle((0,0), 0.65, fc='white')
    fig.gca().add_artist(centre_circle)

    # Texto central impactante
    plt.text(0, 0.1, "100%", ha='center', va='center', fontsize=38, fontweight='bold', color='#2F4F4F')
    plt.text(0, -0.15, "VICTORIA\nCOMBINADA", ha='center', va='center', fontsize=12, fontweight='bold', color='#696969')
    plt.text(0, -0.4, "Análisis de Stats Ofensivas", ha='center', va='center', fontsize=9, color='gray')

    # 6. Colocar las Fichas Técnicas alrededor del anillo
    bbox_props = dict(boxstyle="round,pad=0.5", fc="#F8F9FA", ec="gray", lw=0.5, alpha=0.9)
    kw = dict(arrowprops=dict(arrowstyle="-", color="gray", lw=1.5), bbox=bbox_props, zorder=0, va="center")

    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        
        # Determinar si el texto va a la izquierda o derecha
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = f"angle,angleA=0,angleB={ang}"
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        
        # Posicionar el texto un poco más lejos (1.45) para dar espacio a la ficha
        ax.annotate(etiquetas_detalladas[i], xy=(x, y), xytext=(1.45*np.sign(x), 1.3*y),
                    horizontalalignment=horizontalalignment, fontsize=10, fontfamily='monospace', **kw)

    ax.set_title("Estrategia de Incursión vs Mewtwo (Desglose Analítico)", fontsize=18, fontweight='bold', pad=40)
    plt.axis('off')

    # 7. Guardar y mostrar
    os.makedirs('graficas_proyecto', exist_ok=True)
    ruta_archivo = os.path.join('graficas_proyecto', 'anillo_escuadron_detallado.png')
    
    plt.tight_layout()
    plt.savefig(ruta_archivo, dpi=300, transparent=False, bbox_inches='tight')
    print(f"\n¡Gráfica detallada guardada en: {ruta_archivo}!")
    
    plt.show()

except mysql.connector.Error as err:
    print(f"Error MySQL: {err}")
finally:
    if 'conexion' in locals() and conexion.is_connected():
        conexion.close()