#!/bin/bash

NumeImagine="system-monitor-app"
NumeContainer="statistici-rulare"

echo "1. Construim imaginea Docker..."
docker build -t $NumeImagine .

echo "2. Conectam containerul la monitorul sistemului Linux..."
             
xhost +local:root

echo "3. Rulam containerul..."

docker run --name $NumeContainer --rm \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v $(pwd):/app \
  $NumeImagine

echo ""
echo "4. Terminat! Fisierele generate ('rezultate_statistici.txt' si 'grafic_resurse.png') au fost salvate."