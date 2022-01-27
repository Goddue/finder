def scale(json_response):
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    coords = [toponym["boundedBy"]["Envelope"]["lowerCorner"], toponym["boundedBy"]["Envelope"]["upperCorner"]]
    return abs(float(coords[0].split()[0]) - float(coords[1].split()[0])) * 0.5


