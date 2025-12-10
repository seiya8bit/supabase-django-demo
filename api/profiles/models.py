from uuid import uuid4

from django.db import models


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    full_name = models.CharField(max_length=255, blank=True, default="")
    avatar_url = models.URLField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "profiles"
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self) -> str:
        return self.full_name or str(self.id)
