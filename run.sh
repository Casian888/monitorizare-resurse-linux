#!/bin/bash

NumeImagine="system-monitor-app"
NumeContainer="statistici-rulare"

echo "1. Construim imaginea Docker..."
docker build -t $NumeImagine .

echo "2. Rulam containerul cu volum conectat..."

docker run --name $NumeContainer --rm -v $(pwd):/app $NumeImagine

echo ""
echo "3. Terminat! Fisierele generate ('rezultate_statistici.txt' si 'grafic_resurse.png') sunt aici:"
ls -la | grep -E "grafic_resurse.png|rezultate_statistici.txt"