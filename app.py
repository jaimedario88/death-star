from flask import Flask, request
import json

app = Flask(__name__)


db = []


def parse_data(raw_data: str):
    split_data = raw_data.split(",")

    for i, data in enumerate(split_data):
        if i == 0:
            timestamp = data
        else:
            data = data.replace("(", "").replace(")", "")
            data = data.split("|")
            ship_type = data[0]
            mbm_measure = data[1]

    return {"timestamp": timestamp, "ship_type": ship_type, "mbm": mbm_measure}


@app.route("/listen", methods=["POST"])
def listen():
    raw_data = request.get_data(as_text=True)

    sensor_data = parse_data(raw_data)

    db.append(sensor_data)

    with open("file.txt", "a") as my_file:
        my_file.write(raw_data)
        my_file.write("\n")
    return "OK!"
