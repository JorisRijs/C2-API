from core.main import bp

@bp.route('/')
def index():
    return 'this is the main blueprint'
