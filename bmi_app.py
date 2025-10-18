from flask import Flask, request, jsonify
from os import getenv

app = Flask(__name__)

PORT_NUMMER = 8080

HTTP_STATUS_BAD_REQUEST = 400
HTTP_STATUS_OK = 200


@app.route('/bmi')
def bmi():
    # URL-Parameter abfragen
    kg_str = request.args.get('kg')
    cm_str = request.args.get('cm')

    if kg_str is None:
        return jsonify({
            'erfolg': False,
            'nachricht': 'Bitte URL-Parameter >kg< angeben.'
        }), HTTP_STATUS_BAD_REQUEST

    if cm_str is None:
        return jsonify({
            'erfolg': False,
            'nachricht': 'Bitte URL-Parameter >cm< angeben.'
        }), HTTP_STATUS_BAD_REQUEST

    # in ganze Zahlen umwandeln und validieren
    try:
        kg = int(kg_str)
    except (ValueError, TypeError):
        return jsonify({
            'erfolg': False,
            'nachricht': f'Wert "{kg_str}" für URL-Parameter >kg< ist keine Zahl.'
        }), HTTP_STATUS_BAD_REQUEST

    try:
        cm = int(cm_str)
    except (ValueError, TypeError):
        return jsonify({
            'erfolg': False,
            'nachricht': f'Wert "{cm_str}" für URL-Parameter >cm< ist keine Zahl.'
        }), HTTP_STATUS_BAD_REQUEST

    # eigentliche Berechnung (cm -> m conversion handled same as JS: *10000)
    bmi_value = kg / (cm * cm) * 10000

    # auf eine Nachkommastelle runden
    bmi_value = round(bmi_value * 10) / 10

    if bmi_value < 18.5:
        interpretation = 'Untergewicht'
    elif bmi_value < 25.0:
        interpretation = 'Normalgewicht'
    elif bmi_value < 30.0:
        interpretation = 'Prä-Adipositas'
    elif bmi_value < 35.0:
        interpretation = 'Moderate Adipositas'
    elif bmi_value < 40.0:
        interpretation = 'Starke Adipositas'
    else:
        interpretation = 'Extreme Adipositas'

    return jsonify({
        'erfolg': True,
        'bmi': bmi_value,
        'nachricht': interpretation
    }), HTTP_STATUS_OK


if __name__ == "__main__":    
    port = int(getenv("PORT", "8080"))
    # Bind to all interfaces so Docker port mapping works
    app.run(host="0.0.0.0", port=port)
