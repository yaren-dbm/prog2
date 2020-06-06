import json



def speichern(datei, grösse, gewicht, name):

    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)

    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[grösse] = {"gewicht": gewicht, "grösse": name}


    # print(datei_inhalt)


    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file)




def aktivitaet_speichern(grösse, gewicht, name):

    datei_name = "aktivitaeten.json"
    speichern(datei_name, grösse, gewicht, name)

    return grösse, gewicht, name




def aktivitaeten_laden():
    datei_name = "aktivitaeten.json"

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)

    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt