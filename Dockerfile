# Folosim o imagine de baza usoara de Python
FROM python:3.9-slim

# Setam directorul de lucru in interiorul containerului
WORKDIR /app

# Copiem scriptul Python din masina gazda in container
COPY monitor.py .

# Comanda care se va executa la pornirea containerului
CMD ["python", "-u", "monitor.py"]