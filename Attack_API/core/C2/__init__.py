from flask import Blueprint

bp = Blueprint('C2', __name__)

from core.C2 import routes