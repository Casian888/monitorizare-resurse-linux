
FROM python:3.9-slim

# directorul in care lucreaza containerul
WORKDIR /app

# instalare bib necesare
RUN pip install psutil matplotlib

# copy la scriptul in container
COPY monitor.py .

# rulam aplicatia fara buffer
CMD ["python", "-u", "monitor.py"]