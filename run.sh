#!/bin/bash
# automatizarea build-ului rulare save logurilor si a graficului

NumeImagine="system-monitor-app"
NumeContainer="statistici-rulare"
FisierLog="rezultate_statistici.txt"

echo "1. Construim imaginea Docker (poate dura un timp)..."
docker build -t $NumeImagine .

echo "2. Rulam containerul..."
# -v $(pwd):/app 
# | tee $FisierLog 
docker run --name $NumeContainer --rm -v $(pwd):/app $NumeImagine | tee $FisierLog

echo ""
echo "3. Rularea s-a terminat! Verifica folderul curent pentru rezultate:"
echo "   -> Fisierul imagine: grafic_resurse.png"
echo "   -> Fisierul log: $FisierLog"