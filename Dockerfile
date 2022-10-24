ARG PYTHON_VERSION=3.10

FROM python:${PYTHON_VERSION}
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-venv \
    python3-dev \
    python3-setuptools \
    python3-wheel

RUN mkdir -p /app
WORKDIR /app

COPY release.sh /release.sh
COPY requirements.txt .
RUN pip install -r requirements.txt

ENV DJANGO_SETTINGS_MODULE=iwdsync.settings_live
COPY . .

RUN python manage.py collectstatic --no-input

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "iwdsync.wsgi"]
