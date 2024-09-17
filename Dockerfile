# Stage 1: Builder
FROM python:3-alpine AS builder

WORKDIR /app

RUN python3 -m venv venv
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Run collectstatic
RUN python manage.py collectstatic --noinput

# Stage 2: Runner
FROM python:3-alpine AS runner

ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV PORT=8000

WORKDIR /app

COPY --from=builder /app /app

EXPOSE ${PORT}

CMD gunicorn --bind :${PORT} --workers 2 tech_rahis.wsgi