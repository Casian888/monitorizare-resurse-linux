#!/bin/bash
# Script pentru automatizarea build-ului si rularii containerului

NumeImagine="system-monitor-app"
NumeContainer="statistici-rulare"
FisierLog="rezultate_statistici.txt"

echo "1. Construim imaginea Docker..."
docker build -t $NumeImagine .

echo "2. Rulam containerul si vizualizam log-urile in timp real..."
# Comanda docker run porneste aplicatia. 
# Flag-ul --rm sterge containerul dupa ce executia se termina, pastrand curatenia.
# Redirectionam log-urile atat in terminal cu 'tee', cat si in fisierul de log.
docker run --name $NumeContainer --rm $NumeImagine | tee $FisierLog

echo ""
echo "3. Rularea s-a terminat. Statisticile au fost salvate in fisierul: $FisierLog"

# Folosim comanda tail pentru a citi ultimele 2 linii din fisier
echo "Ultimele 2 inregistrari din fisier ($FisierLog):"
tail -n 2 $FisierLog