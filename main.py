from io import BytesIO
from flask import Flask, send_file
app = Flask(__name__)

def serve_pil_image(img):
	img_io = BytesIO()
	img.save(img_io, 'JPEG', quality=70)
	img_io.seek(0)
	return send_file(img_io, mimetype='image/jpeg')


@app.route("/", methods=["GET", "POST"])

def hello():
        global zakladna_stranka
        if request.method == "GET":
                a, b = float(request.form["sirka"]), float(request.form["vyska"])
                return obrazok(a, b)
        return zakladna_stranka

from PIL import Image
from random import randint

@app.route('/')
def obrazok(a, b):
	width = 640
	height = 400
	img = Image.new('RGB', (width, height), (255,255,255))
	farba = (int(request.args.get('r')), int(request.args.get('g')), int(request.args.get('b')))
	for x in range((width - a)/2, (width + a)/2 + 1):
		for y in range((height - b)/2, (height + b)/2 + 1):
			img.putpixel((x, y), farba)
	return serve_pil_image(img)
app.run()

#...............................................................................
zakladna_stranka = """
<!DOCTYPE html>
<html>
<head>
	<title>Formulár</title>
</head>
<body>
	<h1>Zadaj rozmery obdĺžnika:</h1>
	<form class="form-horizontal" action="/" method="GET">
		<input type="text" name="sirka" id="sirka">
		<input type="text" name="vyska" id="vyska">
		<input type="text" name="farba" id="farba">
		<input type="submit" value="Zobraziť obrázok">
	</form>
</body>
</html>
"""
