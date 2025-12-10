# Supabase + Django Web API Server (Monorepo)

Django-based Web API backed by Supabase with Row-Level Security (RLS). Uses pnpm workspace for a React (Vite) frontend and Django backend; Python deps managed with uv.

## Monorepo Scaffold (short steps)
1) Initialize workspace: `pnpm init -y`
2) Add workspace file [`pnpm-workspace.yaml`](pnpm-workspace.yaml) with:
```
packages:
  - "apps/*"
```
3) Create frontend: `pnpm create vite apps/web --template react-ts`
4) Create backend dir: `mkdir -p apps/api && cd apps/api && uv init --python 3.11 && uv add django`
5) Root installs: `pnpm install`

## Quick Start
- Backend: `cd apps/api && uv run python manage.py migrate && uv run python manage.py runserver`
- Frontend: `cd apps/web && pnpm install && pnpm dev`

## Env Vars
- `SUPABASE_URL`
- `SUPABASE_ANON_KEY`
- `SUPABASE_SERVICE_ROLE_KEY` (server-only if needed)
- `DJANGO_SECRET_KEY`

## Notes
- RLS must be enabled and policies defined on Supabase tables.
- Keep service-role keys on the server side only.
