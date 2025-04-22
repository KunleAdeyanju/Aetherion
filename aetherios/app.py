
from flask import render_template, session # type: ignore

from aetherios.models import Aetherios, ImageGen
from flask_socketio import SocketIO # type: ignore

from . import create_app
app = create_app()
socketio = SocketIO(app)