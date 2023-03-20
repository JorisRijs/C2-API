from core.C2 import bp

@bp.route('/')
def index():
    return 'this is the main blueprint'
