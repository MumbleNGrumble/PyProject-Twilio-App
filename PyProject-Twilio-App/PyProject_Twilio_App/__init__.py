"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)
app.config.from_object('config')

import PyProject_Twilio_App.views
