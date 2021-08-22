FROM python:3.8.0

WORKDIR /usr/src/imdb_graph_api

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/imdb_graph_api

CMD ["python", "src/app.py"]