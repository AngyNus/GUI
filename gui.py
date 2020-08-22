import difflib
from difflib import get_close_matches
import keyword

from appJar import gui

import json


def search(entries):
    found = []
    related = []
    events = ['ACNH', 'AnimalCrossing', 'AnimalCrossingNewHorizons', 'NintendoSwitch', 'BTS','BTSARMY', 'BestFanArmy', 'iHeartAwards', 'BhulaDunga', 'COVID19', 'Coronavirus', 'CoronavirusLockdown', 'coronavirus','KomaramBheemNTR', 'RRRMotionPoster', 'RamCharan', 'RoudramRanamRudhiram', 'SeethaRAMaRajuCHARAN' ]
    with open('C:\\Users\\silve\\PycharmProjects\\untitled\\dat.json') as f:
        data = json.load(f)
        # print(data["events"])

    # find same Hashtags in DB
        for discrete in data["discrete"]:
            print("discrete param: ", discrete)
            for word in entries.values():
                if word == discrete:  # if input is in the file, show it to user
                    print("found in DB: ", word)
                    found.append(word)
    # find related hashtags
    for word in entries.values():
        match = get_close_matches(word, events)
        if match:
            related.extend(match)
    # print("Related Hashtags: ", related)
    app.infoBox("found in DB: ", related)
    return found








# getting the input text


def press(btn):
    if btn == "Cancel":
        app.stop()
    else:
        entries = app.getAllEntries() # getting all the inputs
        print(entries)
        found = search(entries)
        app.infoBox("found in DB: ", found)
        print(found)





if __name__ == '__main__':

    # logoPath = 'logo.gif'

    # gui look
    app = gui("TopTweets", "600x400")
    app.setBg("light blue")
    app.setFont(18)
    # app.setIcon(logoPath)
    app.setTransparency(90)
    app.setOnTop(stay=True)
    app.setResizable(canResize=True)
    app.setStretch("both")
    app.setSticky("ew")

    app.addLabel("title", "Welcome to TopTweets!")
    app.setLabelBg("title", "light blue")

    words = ["bla", "bli", "blo"]

    app.addLabelEntry("Search      ")
    app.addLabelEntry("HashTags")
    app.addLabelEntry("Date        ")
    app.addLabelEntry("Time        ")

    app.addButtons(["Search", "Cancel"], press)

    app.go()
