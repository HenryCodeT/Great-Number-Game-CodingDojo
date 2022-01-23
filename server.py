from flask import Flask, redirect, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route("/",methods=['GET'])
def inicio():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
        print("session number creado", session['number']) 	
        if 'number_guest' not in session:
            session['number_guess']= 0
            print("session number guest creado", session['number_guess'])
    print("renderizando pagina index")
    return render_template("index.html")

@app.route("/guess",methods=['POST'])
def random_guess_post():
    print(request.form['number'])
    session['number_guess']=request.form['number']
    print("post a guess.html")
    return redirect("/guess")

@app.route("/guess",methods=['GET'])
def random_guess_get():
    condition = ""
    if int(session['number_guess']) > int(session['number']):
        condition = 'high'
    elif int(session['number_guess']) < int(session['number']):
        condition = 'low'
    else:
        condition = 'guessed'
    print("renderizando pagina guess.html")
    return render_template("guess.html",condition=condition)

@app.route("/clear",methods=['GET'])
def clear_session():
    session.clear()
    print("renderizando pagina")
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)