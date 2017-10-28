"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, flash, redirect
from PyProject_Twilio_App import app
from .forms import SMSForm
from .twilio_app import SendSMS


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/smsForm', methods=['GET', 'POST'])
def smsForm():
    form = SMSForm()

    if form.validate_on_submit():
        flash("To: %s, Body: %s" % (form.to.data, form.body.data))
        SendSMS(to=form.to.data, body=form.body.data)
        return redirect('/')

    return render_template(
        "smsForm.html",
        title="SMS Form",
        year=datetime.now().year,
        message="SMS form page description.",
        form=form
    )