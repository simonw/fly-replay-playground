FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 8080
CMD ["uvicorn", "app:app", "--port", "8080", "--host", "0.0.0.0"]