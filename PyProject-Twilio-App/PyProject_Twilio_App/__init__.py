"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import PyProject_Twilio_App.views
