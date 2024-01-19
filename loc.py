from flask import Flask, request, jsonify
import math


app = Flask(__name__)

def haversine(lat1, lon1, lat2, lon2):
    radius = 6371000
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radius * c

def is_within(lat1, lon1, lat2, lon2, rang):
    distance = haversine(lat1, lon1, lat2, lon2)
    return distance <= rang

@app.route("/loc", methods=["POST"])
def loc():
    data = request.get_json()
    lat1, lon1 = data['lat1'], data['lon1']
    lat2, lon2 = data['lat2'], data['lon2']
    dist = data['dist']
    result = is_within(lat1, lon1, lat2,lon2, dist)
    return jsonify({'result': result})