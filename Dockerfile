FROM python:3.12-slim-bookworm

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    HOST=0.0.0.0 \
    PORT=8080

COPY pyproject.toml ./
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir \
        $(python3 -c "import tomllib; print(' '.join(tomllib.load(open('pyproject.toml', 'rb'))['project']['dependencies']))")

COPY app ./app
COPY config ./config
COPY run.py ./

EXPOSE 8080

CMD ["python", "run.py"]
