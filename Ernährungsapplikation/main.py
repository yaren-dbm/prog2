from flask import Flask
from flask import render_template
from flask import request
import daten



app = Flask("Ernährungsapplikation")




@app.route("/berechnung", methods=['GET', 'POST'])

def berechnung():

    if request.method == 'POST':

        name = request.form["name"]
        gewicht = request.form["gewicht"]
        grösse = float(request.form["grösse"])
        bmi = round((float(gewicht) / ((float(grösse) / 100) ** 2)),1)

           

        if bmi <= 18.5:
            untergewicht = "Du bist untergewichtig. Dein persönlicher BMI ist: " + str(bmi)
            return render_template("index.html", untergewicht=untergewicht)
        elif bmi >=18.5 and bmi <=24.9:
            normalgewicht = "Du hast eine Normalgewicht. Dein persönlicher BMI ist: " + str(bmi)
            return render_template("index.html", normalgewicht=normalgewicht)
        elif bmi >=25 and bmi <=29.9:
            übergewicht = "Du bist übergewichtig. Dein persönlicher BMI ist: " + str(bmi)
            return render_template("index.html", übergewicht=übergewicht)
        elif bmi >=30:
            fettleibigkeit = "Du leidest unter Fettleibigkeit (Adipositas). Dein persönlicher BMI ist: " + str(bmi)
            return render_template("index.html", fettleibigkeit=fettleibigkeit)
        else:
            allgemein =  "Dein persönlicher BMI ist: " + str(bmi)
            return render_template("index.html", allgemein=allgemein)
    

    return render_template("index.html")




@app.route("/speichern", methods=['GET', 'POST'])

def aktivitaet_speichern():

    if request.method == 'POST':

        name = request.form["name"]
        gewicht = request.form["gewicht"]
        grösse = request.form["grösse"]

        name, gewicht, grösse = daten.aktivitaet_speichern(name, gewicht, grösse)

    return render_template("index.html")




@app.route("/auswertung")

def auswertung():
    aktivitaeten=daten.aktivitaeten_laden()
    

    return render_template("auswertung.html", aktivitaeten=aktivitaeten)






if __name__ == "__main__":
    app.run(debug=True, port=5000)

