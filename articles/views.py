from django.shortcuts import render
from .models import Article
import uuid, os
from django.conf import settings
from django.core.files.storage import default_storage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

def home(request):
    articles = Article.objects.filter(status=Article.PUBLISHED)[:20]
    return render(request, "articles/home.html", {"articles": articles})

@csrf_exempt
@require_POST
def editor_upload(request):
    f = request.FILES.get("file")
    if not f:
        return JsonResponse({"error": "no file"}, status=400)

    ext = os.path.splitext(f.name)[1].lower()
    filename = f"{uuid.uuid4().hex}{ext}"
    rel_path = f"articles/inline/{filename}"
    default_storage.save(rel_path, f)

    return JsonResponse({"src": settings.MEDIA_URL + rel_path})