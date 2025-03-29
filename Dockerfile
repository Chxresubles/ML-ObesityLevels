FROM python:3.12-alpine AS builder

ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY pyproject.toml .
COPY ./mlobesitylevels ./mlobesitylevels

RUN apk add --no-cache gcc g++ musl-dev && \
    pip install --no-cache-dir --no-compile .

FROM python:3.12-alpine AS runtime

ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY ./output/model.pkl ./output/preprocessor.pkl ./output/
COPY ./scripts/score.py .
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages

RUN apk add --no-cache libgomp libstdc++

CMD ["python", "score.py"]
