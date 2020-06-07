from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import daten

#Folgende Funktionen konnten nicht geladen werden:

#import natsort import natsorted, ns
#import pandas as pd
#from plotly.offline import plot
#import plotly.graph_objects as go
#import plotly.express as px



app = Flask("Ernährungsapplikation")


#Begrüssungsseite
@app.route("/startseite") 
def startseite():
    return render_template('startseite.html', title='Herzlich Willkommen')



#Berechnung und Auswertung BMI
@app.route("/berechnung", methods=['GET', 'POST']) 

def berechnung():

    if request.method == 'POST': #aufgrund Formular

        name = request.form["name"]
        gewicht = request.form["gewicht"]
        grösse = float(request.form["grösse"])
        bmi = round((float(gewicht) / ((float(grösse) / 100) ** 2)),1)
        #Formel BMI Berechnung, die 1 hinten steht für die Rundung um 1 Kommastelle

           
        #mehr als 2 Bedingungen, if / elif / else
        if bmi <= 18.5:
            untergewicht = "Du bist untergewichtig. Dein persönlicher BMI ist: " + str(bmi)
            return render_template("index.html", untergewicht=untergewicht)
        elif bmi >=18.5 and bmi <=24.9:
            normalgewicht = "Du hast ein Normalgewicht. Dein persönlicher BMI ist: " + str(bmi)
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



#Speicherung der Eingaben
@app.route("/speichern", methods=['GET', 'POST'])

def eingaben_speichern():

    if request.method == 'POST':

        name = request.form["name"]
        gewicht = request.form["gewicht"]

        name, gewicht = daten.eingaben_speichern(name, gewicht)

        return redirect("/auswertung") 

    return render_template("index.html")



#Ausgabe der Tabelle
@app.route("/auswertung") 
def auswertung():
    eingaben = daten.eingaben_laden()
    sortiert = sorted(eingaben.items()) #sortiert = natsorted(eingaben.items()) -->Diese Funktion war hier gedacht, jedoch funktionierte der "import" nicht
    nummeriert = enumerate(sortiert,start = 1) #Nummerierung startet mit der Nummer 1
    #div = viz()

    return render_template("auswertung.html", nummeriert=nummeriert)
    #viz_div=div (Dies würde in der Klammer am Schluss stehen, für die Datenvisualisierung, welche nicht funktioniert hat)





#Barplot
"""Fehlermeldung:
ModuleNotFoundError: No module named 'plotly.graph_objects'; 'plotly' is not a package
--> obwohl ich auf Anaconda pip install plotly getätigt habe

def data():    
    data = daten.eingaben_laden()

    data_df = pd.DataFrame.from_dict(data, orient="index")
    data_df = data_df.reset_index()

    data_df.columns = ["Gewicht", "Name"]

    data_df = data_df.sort_values(by=["Gewicht"])

    return data_df


def viz():
    data_df = data()

    fig = px.bar(
        data_df,
        x = data_df.Gewicht, y=data_df.Name,
        orientation = "h",
        height=400,
        width=800

        )


    fig.layout.template = "plotly_white"

    div = plot(fig, output_type = "div")

    return div
"""



"""
@app.route("/auswertung")   --->Diese Funktion hat nicht funktioniert

def auswertung():
    eingaben = daten.eingaben_laden()

    eingaben_liste = ""

    for key, value in eingaben.items():
        zeile = key + ": " + value + "<br>"
        eingaben_liste += zeile

    return eingaben_liste
"""



if __name__ == "__main__":
    app.run(debug=True, port=5000)

