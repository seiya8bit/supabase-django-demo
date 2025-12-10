from django.http import JsonResponse
from django.urls import path
from postgrest.exceptions import APIError

from .supabase_client import get_client


def health(request):
    return JsonResponse({"status": "ok"})


def profiles(request, user_id: str):
    if request.method != "GET":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    supabase = get_client()
    try:
        response = (
            supabase.table("profiles")
            .select("*")
            .eq("id", user_id)
            .single()
            .execute()
        )
    except APIError as exc:
        if getattr(exc, "code", "") == "PGRST116":
            return JsonResponse({"error": "Profile not found"}, status=404)
        raise

    if not response.data:
        return JsonResponse({"error": "Profile not found"}, status=404)

    return JsonResponse(response.data)


urlpatterns = [
    path("health", health),
    path("profiles/<str:user_id>", profiles),
]
