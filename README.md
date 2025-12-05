# TITULO DEL DESIGN DOC
Link: [Link a este design doc](https://github.com/Skianyan/proyecto-backend-1/blob/main/README.md)

Author(s): Ricardo H.

Status: Draft

Ultima actualización: 2025-10-14

## Contenido
- Goals
- Non-Goals
- Background
- Overview
- Detailed Design
  - Solucion 1
    - Frontend
    - Backend
  - Solucion 2
    - Frontend
    - Backend

## Links
- [Proyecto en GitHub](https://github.com/Skianyan/proyecto-backend-1)

## Objetivo
El proyecto consiste de una página web en la cual se pueden visualizar datos del DENUE en un mapa interactivo está enfocado en la longevidad de los negocios.

Este proyecto busca utilizar la información que nos provee el INEGI para estudiar la durabilidad de negocios de diferentes giros, en áreas especificadas y en espacios de tiempo especificados.

## Goals
- Leer datos del DENUE en un programa Python para analizar la duración de los negocios.
- Plasmar estos datos en un mapa, el cual muestre concentraciones de negocios de alta longitud.
- Habilidad de filtrar negocios por tipo de negocio
- Habilidad de filtrar negocios por rango de fechas en las que fueron inscritas al DENUE
  
## Non-Goals
- Consultar bases de datos relacionadas con negocios aparte de las oficiales del INEGI.
- Crear una aplicación web adaptable a moviles.
- Crear un sistema con logins.
- Un CRUD hacia la base de datos (solo leer datos).
  

## Background
El Directorio Estadístico Nacional de Unidades Económicas. (DENUE) es un directorio de negocios que proporciona información de negocios registrados en un sector de méxico, 
el directorio cuenta con información importante como lo es el giro del negocio, ubicación (dirección y coordenadas), información de contacto, etc.

El INEGI hace un estudio al que le denomina demografia de los negocios, en la cual calcula
estadisticas sobre la mortalidad de los negocios y los publica en su pagina.
https://www.inegi.org.mx/temas/dn/

## Overview
El proyecto consiste de una pagina web programada en Python utilizando la tecnologia Flask, la cual lee de una
base de datos de excel, mysql o postgres dependiendo de la api que se consulta (diferente /api/csv, por ejemplo).
Su entorno grafico consiste de un mapa en el cual se despliegan diferentes pines, estos son cargados solamente cuando
se encuentra a un nivel especifico de zoom, para prevenir sobrecarga de datos.
Los pines se pueden filtrar a partir de datos cosas como año de inscripcion, tipo de negocio.


## Solution 1
### Frontend
Utilizamos OpenStreetMaps y Leaflet para desplegar mapas y insertar los pines.
OpenStreetMaps, como su nombre implica es un mapa de uso libre bajo una licencia abierta, perfecta para un proyecto pequeño como el nuestro.
Leaflet.js es una librería de javascript que nos permite manipular mediante css lo que desplegamos en un mapa, en nuestro caso mediante pines
los cuales muestren información sobre el negocio al presionarlos.

### Backend
Se utilizan archivos .csv separados por tablas, utilizamos la funcionalidad de "merge" que tiene la libreria de pandas para
unirlos en una


