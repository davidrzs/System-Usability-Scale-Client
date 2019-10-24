from flask import Flask, render_template, session, request, redirect
from forms import Step1, Step2
from flask_session import Session

app = Flask(__name__,template_folder="templates")
app.secret_key = "SKEMWNU9ueELhRdABnmXaNwQqx2TThcB"
app.config['SESSION_TYPE'] = 'filesystem'
sess = Session()
sess.init_app(app)

@app.route('/')
def hello_world():
    res = redirectUserCorrectlyFromWithinSurvey("/")
    
    if(res != None):
        return res
    
    return render_template('/index.html')

@app.route("/saveSurvey")
def saveSurvey(methods=('GET', 'POST')):
    #todo
    print(session["user"])
    return session["user"]

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
    res = redirectUserCorrectlyFromWithinSurvey("/sus/1")
    if(res != None):
        return res 
    form = Step1()
    if form.validate_on_submit():
        session["user"]["part1"] = True
        session["user"]["answer1"] = form.name.data;
        print(session)
        # we need to store the info from the survey
        return redirect('/sus/2')
    return render_template('sus1.html', form=form)

@app.route('/sus/2', methods=('GET','POST'))
def page2():
    print("yay")
    res = redirectUserCorrectlyFromWithinSurvey("/sus/2")
    if(res != None):
        return res 
    form = Step2()
    if form.validate_on_submit():
        session["user"]["part2"] = True
        session["user"]["answer2"] = form.name.data;
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