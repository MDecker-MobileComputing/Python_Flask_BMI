# Python+Flask: BMI-Berechnung #

<br>

Dieses Repository enthält ein Python-Programm, das mit [Flask](https://flask.palletsprojects.com/en/stable/) einen REST-Endpunkt bereitstellt.

<br>

----

## Anwendung ausführen ##

<br>

Abhängigkeiten installieren und ausführen (Variante 1):
```
pip install -r requirements.txt
```

<br>

Abhängigkeiten installieren und ausführen (Variante 2):
```
py -m pip install -r requirements.txt
```

<br>

Programm starten:
```
python bmi_app.py
```

<br>

Beispielaufe bei lokaler Ausführung:
* http://localhost:8080/bmi?kg=75&cm=180
* http://localhost:8080/bmi?kg=110&cm=175

<br>

Beispiel für JSON-Antwort:
```
{
    "bmi"      : 23.1,
    "erfolg"   : true,
    "nachricht": "Normalgewicht"
}
```

<br>

----

## Docker-Image bauen und ausführen ##

<br>

Image anhand [Dockerfile](Dockerfile) bauen:
```
docker build -t python-bmi-api .
```

<br>


Container für Image erzeugen und starten
```
docker run -p 8080:8080 python-bmi-api
```

<br>

----

## License ##

<br>

See the [LICENSE file](LICENSE.md) for license rights and limitations (BSD 3-Clause License).

<br>
