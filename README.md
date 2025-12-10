# Supabase + Django Web API Server

Startup instructions for the Django Web API server.

## Getting started

```sh
cd api

# Install dependencies (if not yet)
uv sync

# Apply migrations
uv run python manage.py migrate

# Start the server
uv run python manage.py runserver localhost:8000

# Health check
curl http://localhost:8000/health
```

## Supabase local environment (Docker)

```sh
cd supabase
npm install
npm run local:start
```
