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

def bmi():

    bmi = ''

    if request.method == 'POST':

        gewicht = float(request.form.get('gewicht'))

        grösse = float(request.form.get('grösse'))

        bmi = bmi_rechner(gewicht, grösse)

    return render_template("index.html", bmi=bmi)



def bmi_rechner(gewicht, grösse):

    return round((gewicht / ((grösse / 100) ** 2)), 1)

    

if __name__ == "__main__":
    app.run(debug=True, port=5000)













