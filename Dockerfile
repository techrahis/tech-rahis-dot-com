FROM python:3-alpine AS builder

WORKDIR /app

RUN python3 -m venv venv
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

# Stage 2
FROM python:3-alpine AS runner

ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV PORT=8000

WORKDIR /app

COPY --from=builder /app/venv venv
COPY blogs blogs
COPY core core
COPY helpers helpers
COPY projects projects
COPY static static
COPY tech_rahis tech_rahis
COPY templates templates
COPY manage.py .

EXPOSE ${PORT}

CMD gunicorn --bind :${PORT} --workers 2 tech_rahis.wsgi