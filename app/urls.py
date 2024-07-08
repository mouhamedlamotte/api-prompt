from .users import user_bp
from .auth import auth_bp
from .prompts import prompt_bp
from .groups import group_bp
from .payement import transaction_bp

urlpatterns = [
    {
        "prefix": "/users",
        "blueprint": user_bp
    },
    {
        "prefix": "/auth",
        "blueprint": auth_bp
    },
    {
        "prefix": "/prompts",
        "blueprint": prompt_bp
    },
    {
        "prefix": "/groups",
        "blueprint": group_bp
    },
    {
        "prefix": "/transactions",
        "blueprint": transaction_bp
    }
]

def register_urls(app):
    for url in urlpatterns:
        app.register_blueprint(url.get("blueprint"), url_prefix=url.get("prefix"))