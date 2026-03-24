CREATE DATABASE enciclopedia_pokemon;
USE enciclopedia_pokemon;

CREATE TABLE tipos (
    id_tipo INT PRIMARY KEY,
    descripcion VARCHAR(50)
);

CREATE TABLE clasificacion (
    id_clasificacion INT PRIMARY KEY,
    descripcion VARCHAR(100)
);

CREATE TABLE pokemones (
    no_pokedex INT PRIMARY KEY,
    nombre VARCHAR(100),
    altura_m FLOAT,
    peso_kg FLOAT,
    id_tipo INT,
    id_clasificacion INT,
    legendario BOOLEAN,
    prob_captura FLOAT,
    salud INT,
    velocidad INT,
    generacion INT,
    
    FOREIGN KEY (id_tipo) REFERENCES tipos(id_tipo),
    FOREIGN KEY (id_clasificacion) REFERENCES clasificacion(id_clasificacion)
);

CREATE TABLE defensas (
    id_defensa INT PRIMARY KEY,
    no_pokedex INT,
    defensa INT,
    defensa_especial INT,
    
    FOREIGN KEY (no_pokedex) REFERENCES pokemones(no_pokedex)
);

CREATE TABLE ataques (
    id_ataque INT PRIMARY KEY,
    no_pokedex INT,
    ataque INT,
    ataque_especial INT,
    
    FOREIGN KEY (no_pokedex) REFERENCES pokemones(no_pokedex)
);

CREATE TABLE contraataques (
    id_contraataque INT PRIMARY KEY,
    no_pokedex INT,
    
    normal FLOAT,
    insecto FLOAT,
    siniestro FLOAT,
    dragon FLOAT,
    electrico FLOAT,
    hada FLOAT,
    lucha FLOAT,
    fuego FLOAT,
    volador FLOAT,
    fantasma FLOAT,
    planta FLOAT,
    tierra FLOAT,
    hielo FLOAT,
    veneno FLOAT,
    psiquico FLOAT,
    roca FLOAT,
    acero FLOAT,
    agua FLOAT,
    
    FOREIGN KEY (no_pokedex) REFERENCES pokemones(no_pokedex)
);
