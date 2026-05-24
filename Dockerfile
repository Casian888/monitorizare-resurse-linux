
FROM python:3.9-slim


WORKDIR /app


RUN pip install psutil matplotlib plotext


COPY monitor.py .


CMD ["python", "-u", "monitor.py"]