from pathlib import Path
import mimetypes

from django.conf import settings
from django.http import FileResponse, Http404


FRONTEND_DIR = Path(settings.BASE_DIR) / "frontend"
ASSETS_DIR = FRONTEND_DIR / "assets"


def frontend(request):
    index_file = FRONTEND_DIR / "index.html"

    if not index_file.exists():
        raise Http404(
            f"React frontend build not found: {index_file}"
        )

    return FileResponse(
        index_file.open("rb"),
        content_type="text/html",
    )


def frontend_asset(request, path):
    asset_file = ASSETS_DIR / path

    # Prevent paths from escaping the assets directory
    try:
        asset_file.resolve().relative_to(ASSETS_DIR.resolve())
    except ValueError:
        raise Http404("Invalid asset path")

    if not asset_file.is_file():
        raise Http404(
            f"Frontend asset not found: {path}"
        )

    content_type, _ = mimetypes.guess_type(str(asset_file))

    return FileResponse(
        asset_file.open("rb"),
        content_type=content_type or "application/octet-stream",
    )