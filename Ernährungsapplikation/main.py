from flask import Flask
from flask import render_template
from flask import request
import daten



app = Flask("Ernährungsapplikation")



@app.route("/startseite.html")
def startseite():
    return render_template('startseite.html')

@app.route("/index.html")
def rechner():
    return render_template('index.html')

@app.route("/auswertung.html")
def auswertung():
    return render_template('auswertung.html')
    
 


@app.route('/index.html', methods=['GET', 'POST'])

def index():

    bmi = ''

    if request.method == 'POST' and 'gewicht' in request.form:

        gewicht = float(request.form.get('gewicht'))

        grösse = float(request.form.get('grösse'))

        bmi = bmi_rechner(gewicht, grösse)

    return render_template("index.html", bmi=bmi)



def bmi_rechner(gewicht, grösse):

    return round((gewicht / ((grösse / 100) ** 2)), 2)






@app.route("/speichern/", methods=['GET', 'POST'])

def aktivitaet_speichern():

    if request.method == 'POST':

        aktivitaet = request.form['aktivitaet']

        zeitpunkt, aktivitaet = daten.aktivitaet_speichern(aktivitaet)

        rueckgabe_string = "Gespeichert: " + aktivitaet + " um " + str(zeitpunkt)

        return rueckgabe_string



    return render_template("index.html")



@app.route("/liste")

def auflisten():

    aktivitaeten = daten.aktivitaeten_laden()



    aktivitaeten_liste = ""

    for key, value in aktivitaeten.items():

        zeile = str(key) + ": " + value + "<br>"

        aktivitaeten_liste += zeile



    return aktivitaeten_liste





if __name__ == "__main__":
    app.run(debug=True, port=5000)