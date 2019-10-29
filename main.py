from flask import Flask, render_template, session, request, redirect, flash, Response
from forms import Step1, Step2
from flask_session import Session
from database import Database
import os
import sys

if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    app = Flask(__name__, template_folder=template_folder)
else:
    app = Flask(__name__)

app.secret_key = "SKEMWNU9ueELhRdABnmXaNwQqx2TThcB"
app.config['SESSION_TYPE'] = 'filesystem'
sess = Session()
sess.init_app(app)

database = Database()

@app.route('/')
def init():
    if database.getLocale() == None:
        redirect("/choose_language")
    return render_template('/index.html')

@app.route("/saveSurvey")
def saveSurvey(methods=('GET', 'POST')):
    # get rid of internal variables -> we don't need to store them
    session["user"].pop("part1")
    session["user"].pop("part2")
    # we add all of it to the database
    database.addDataToDatabase(session.get("user"))
    # remove the user from the session object
    session["user"] = None
    database.toCsvFile()
    flash("Herzlichen Dank. Ihre Daten wurden gespeichert.")
    # redirect to thank you page
    return redirect("/thank-you")

@app.route("/exportToCSVDownload")
def exportToCSVDownload():
    csv = database.toCsvDownload()
    return Response(csv, mimetype='text/csv')

@app.route("/exportToCSVFile")
def exportToCSVFile():
    database.toCsvFile()
    flash("Daten erfolgreich in Datei exportiert")
    return redirect("/")

@app.route("/newSurvey")
def createNewSurvey():
    session["user"] = {"part1":False, "part2":False}
    return redirect("/sus/1")

@app.route('/sus/1', methods=('GET', 'POST'))
def page1():
    form = Step1()
    if form.validate_on_submit():
        session["user"]["part1"] = True
        # now we store the data from the survey in the session
        session["user"]["q1"] = form.q1.data;
        session["user"]["q2"] = form.q2.data;
        session["user"]["q3"] = form.q3.data;
        session["user"]["q4"] = form.q4.data;
        session["user"]["q5"] = form.q5.data;
        session["user"]["q6"] = form.q6.data;
        session["user"]["q7"] = form.q7.data;
        session["user"]["q8"] = form.q8.data;
        session["user"]["q9"] = form.q9.data;
        session["user"]["q10"] = form.q10.data;
        # we now redirect the user to part 2
        return redirect('/sus/2')
    return render_template('sus1.html', form=form)

@app.route('/sus/2', methods=('GET','POST'))
def page2():
    """
    Renders the second part of the survey. The survey comes from a form 'Step2' which contains all the needed fields.
    Upon sucessful completion we store the results in the session and redirect to '/saveSurvey' which then saves the survey.
    """
    form = Step2()
    if form.validate_on_submit():
        session["user"]["part2"] = True
        session["user"]["open1"] = form.open1.data;
        session["user"]["open2"] = form.open2.data;
        session["user"]["open3"] = form.open3.data;
        session["user"]["open4"] = form.open4.data;
        session["user"]["open5"] = form.open5.data;
        session["user"]["open6"] = form.open6.data;
        # we need to store the info from the survey
        return redirect('/saveSurvey')
    return render_template('sus2.html', form=form)

def redirectUserCorrectly():
    if("user" not in session):
        return
    if(not session["user"]["part1"]):
        return redirect("/sus/1")
    if(not session["user"]["part2"]):
        return redirect("/sus/2")
    elif(session["user"]["part1"] and session["user"]["part2"]):
        return redirect("/saveSurvey")


@app.route("/cancel")
def cancel():
    """
    If the user want to cancel the form this function gets called.
    It deletes everything the user has entered and returns to the index page.
    """
    session.pop('user', None)
    flash("Ausfüllen der Umfrage abgebrochen")
    return redirect("/")


@app.route("/thank-you")
def thank_you():
    """
    A function which just renders a thank you page. Gets called at the end of the survey AFTER saving the data.
    """
    return render_template('thank-you.html')

if __name__ == '__main__':
    app.run(debug=False)
