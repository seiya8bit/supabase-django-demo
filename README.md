# Supabase + Django Web API Server

Django-based Web API backed by Supabase with Row-Level Security (RLS).
Python dependencies are managed with uv.

## Backend Setup
1) Initialize backend directory: `mkdir -p api && cd api && uv init --python 3.14`
2) Install Django and dependencies: `uv add django`
3) Configure Supabase env vars (see below) and Django settings for RLS-backed access.

## Quick Start
- Backend: `cd api && uv run python manage.py migrate && uv run python manage.py runserver 0.0.0.0:8000`
- Health check: open `http://localhost:8000/health` or `curl http://localhost:8000/health`

## Env Vars
- `SUPABASE_URL`
- `SUPABASE_ANON_KEY`
- `SUPABASE_SERVICE_ROLE_KEY` (server-only if needed)
- `DJANGO_SECRET_KEY`

## Notes
- RLS must be enabled and policies defined on Supabase tables.
- Keep service-role keys on the server side only.
- React/Vite frontend removed; repository now focuses solely on the Django API.
