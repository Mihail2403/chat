FROM python:3.10.6-alpine

WORKDIR /my_site
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFERRED=1
COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -U 'Twisted[tls,http2]'
