from flask import Flask, jsonify
import csv
app = Flask(__name__)
airports = {}
with open("airports.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    print("CSV headers:", reader.fieldnames)  # Debug line

    for row in reader:
        icao = row["ident"].upper()
        airports[icao] = {
            "ICAO": row["ident"],
            "Name": row["name"],
            "Location": row["municipality"]
        }
@app.route("/airport/<icao>")
def get_airport(icao):
    icao = icao.upper()
    if icao in airports:
        return jsonify(airports[icao])
    else:
        return jsonify({"error": "Airport not found"}), 404

if __name__ == "__main__":
    app.run(port=5000, debug=True)
