from flask import Flask, render_template, session, request, redirect, flash
from forms import Step1, Step2
from flask_session import Session
from database import Database


app = Flask(__name__,template_folder="templates")
app.secret_key = "SKEMWNU9ueELhRdABnmXaNwQqx2TThcB"
app.config['SESSION_TYPE'] = 'filesystem'
sess = Session()
sess.init_app(app)

database = Database()

@app.route('/')
def hello_world():
    res = redirectUserCorrectlyFromWithinSurvey("/")
    
    if(res != None):
        return res
    
    return render_template('/index.html')

@app.route("/saveSurvey")
def saveSurvey(methods=('GET', 'POST')):
    # this aids debugging
    flash(session["user"])
    # we now add all of it to the database
    a = session["user"]
    print(a)
    database.addDataToDatabase(session.get("user"))
    # remove the user from the session object
    session["user"] = None
    flash("Thank you. Your data has been saved")
    # redirect to thank you page
    return redirect("thank-you")

@app.route("/newSurvey")
def createNewSurvey():
    res = redirectUserCorrectlyFromWithinSurvey("/newSurvey")
    if(res != None):
        return res
    #usr = User()
    print("make new survey")
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
        # we now redirect the user to part 2
        return redirect('/sus/2')
    flash("Please finish filling out all questions correctly.")
    return render_template('sus1.html', form=form)

@app.route('/sus/2', methods=('GET','POST'))
def page2():
    form = Step2()
    if form.validate_on_submit():
        session["user"]["part2"] = True
        # we need to store the info from the survey
        return redirect('/saveSurvey')
    flash("Please finish filling out all questions correctly.")
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
    session["user"] = None
    flash("Cancelled filling out survey!")
    redirectUserCorrectlyFromWithinSurvey("/cancel")
    return redirect("/")

@app.route("/thank-you")
def thank_you():
    return render_template('thank-you.html')

def redirectUserCorrectlyFromWithinSurvey(currentPage):
    return
    """
    if(("user" not in session) and (currentPage == "/" or currentPage == "/newSurvey")):
        print("new user not yet created")
        return
    
    if(("user" not in session) and currentPage != "/"):
        print("redirect to home from somewhere")
        return redirect("/")
    
    if((not session["user"]["part1"] ) and currentPage != "/sus/1"):
        print("fuck1")
        print(session)
        return redirect("/sus/1")

    if((not session["user"]["part1"] ) and currentPage == "/sus/1"):
        print("fuck1")
        return
    
    if((session["user"]["part1"] and not session["user"]["part2"] ) and currentPage != "/sus/2"):
        return redirect("/sus/2")

    if((session["user"]["part1"] and not session["user"]["part2"] ) and currentPage == "/sus/2"):
        return
    
    if(session["user"]["part1"] and session["user"]["part2"]):
        return redirect("/saveSurvey")
    else:
        return
    """

if __name__ == '__main__':
    app.run(debug=True)