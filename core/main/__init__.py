from flask import Blueprint

bp = Blueprint('C2', __name__)

from core.main import routes
