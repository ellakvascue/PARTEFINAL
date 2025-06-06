FROM python:3.10-slim
WORKDIR /app
COPY buro_api.py .
RUN pip install flask
EXPOSE 5003
CMD ["python", "buro_api.py"]
