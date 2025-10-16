# TITULO DEL DESIGN DOC
Link: [Link a este design doc](#)

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
- Consideraciones
- Métricas

## Links
- [Un link](#)
- [Otro link](#)

## Objetivo
El proyecto consiste de una página web en la cual se pueden visualizar datos del DENUE en un mapa interactivo está enfocado en la longevidad de los negocios.

Este proyecto busca utilizar la información que nos provee el INEGI para estudiar la durabilidad de negocios de diferentes giros, en áreas especificadas y en espacios de tiempo especificados.

## Goals
- Leer datos del DENUE en un programa Python para analizar la duración de los negocios.
- Plasmar estos datos en un heatmap, el cual muestre concentraciones de negocios de alta longitud.
- Habilidad de filtrar negocios por tipo de negocio
- Habilidad de filtrar negocios por rango de fechas en las que fueron inscritas al DENUE
- Identificar negocios los cuales han estado inscritos por más de 1 año sin darse de baja
  
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
base de datos de excel, mysql o postgres dependiendo del branch del proyecto.
Su entorno grafico consiste de diferentes filtros los cuales afectan lo que se desplegara en un mapa central,
los datos a filtrar incluyen cosas como año de inscripcion, tipo de negocio, o solo desplegar negocios que
tengan cierto rango de longevidad.

## Detailed Design
_Usa diagramas donde veas necesario_

_Herramientas como [Excalidraw](https://excalidraw.com) son buenos recursos para esto_

_Cubre los cambios principales:_

 _- Cuales son las nuevas funciones que vas a escribir?_
 _- Porque necesitas nuevos componentes?_
 _- Hay código que puede ser reusable?_

_No elabores minuciosamente la implementación._

## Solution 1
### Frontend
_Frontend…_
### Backend
_Backend…_

## Solution 2
### Frontend
_Frontend…_
### Backend
_Backend…_

## Consideraciones
_Preocupaciones / trade-offs / tech debt_

## Métricas
_Que información necesitas para validar antes de lanzar este feature?_
