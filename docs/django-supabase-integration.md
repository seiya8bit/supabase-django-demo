# Supabase request flow with PostgREST auth

Before any Supabase operation, extract the `Authorization` header from the incoming
request, parse its bearer token, and set it on PostgREST:

```python
# Pseudocode snippet
auth_header = request.headers.get("Authorization", "")
token = auth_header.replace("Bearer ", "").strip()
supabase.postgrest.auth(token)
```

By calling `supabase.postgrest.auth(token)` prior to queries, PostgREST receives the
JWT and Row Level Security (RLS) becomes effective for the subsequent database calls.
After the token is set, perform your usual Supabase queries; they will now respect the
RLS policies enforced by PostgREST.
