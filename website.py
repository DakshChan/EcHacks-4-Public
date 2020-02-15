from flask import Flask, render_template, request
import json
import requests
import tdData
import greenAlt

app = Flask(__name__)
configFile = open("config.txt", "r")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/loggedIn', methods=['POST'])
def signIn():
    try:
        number = request.form['num']
        data = tdData.filtered_resp(number)
        greenData = set()
        for i in range(len(data)):
            greenData.add(greenAlt.get_green_alt(data, i))

        print(greenData)
        size = len(greenData)

        data2 = []
        for i in range(len(data[0])):
            data2.append([])
            for j in range(len(data)):
                data2[i].append(data[j][i])


    except:
        return "You Done Goofed"
    if len(data) == 0:
        return "You Done Goofed, there is no data"

    return render_template("heatmap.html", googlekey=json.load(configFile)['google'], ina=str(data2[0]), inb=str(data2[1]), inc=str(data2[2]), data=data, greenData=greenData, size=size)

if __name__ == "__main__":
    app.run(debug=True)
