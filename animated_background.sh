#!/bin/bash

# Directorio donde están las imágenes
DIR=~/scripts/nyxbackground/frames

# Inicia un bucle infinito
while true; do
  # Recorre las imágenes de frame_0000.png a frame_0107.png
  for img in $DIR/frame_*.png; do
    feh --bg-fill "$img"  # Establece la imagen como fondo de pantalla
    sleep 0.02  #Espera 0.03 (60FPS), 0.02 (50FPS), 0.05 (20FPS) por cada imagen para efecto de animacion
  done
done

