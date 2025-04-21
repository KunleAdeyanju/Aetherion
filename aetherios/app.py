
from flask import render_template, session

from aetherios.models import Aetherios, ImageGen
from flask_socketio import SocketIO

from . import create_app
app = create_app()
socketio = SocketIO(app)