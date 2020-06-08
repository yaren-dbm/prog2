import json



def speichern(datei, key, value, name):

    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)

    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[name] = str(gewicht)


    # print(datei_inhalt)


    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file)




def eingaben_speichern(name, gewicht):

    datei_name = "auswertung.json"

    speichern(datei_name, name, gewicht)

    return name, gewicht




def eingaben_laden():
    datei_name = "auswertung.json"

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)

    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt