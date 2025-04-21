
from flask import Blueprint, render_template, request, redirect, url_for

from pyexpat.errors import messages
from flask import render_template, request, redirect, url_for, flash, session
from flask import render_template, request, redirect, url_for, flash, session
from flask_login import current_user, login_user, logout_user
from flask_login.utils import login_required

from models import Aetherios

rt = Blueprint('routes', __name__)

@rt.route('/')
def appear():
    return "helloworld"
