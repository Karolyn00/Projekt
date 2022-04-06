from io import BytesIO
from flask import Flask, send_file
app = Flask(__name__)

def serve_pil_image(img):
	img_io = BytesIO()
	img.save(img_io, 'JPEG', quality=70)
	img_io.seek(0)
	return send_file(img_io, mimetype='image/jpeg')


from PIL import Image
from random import randint

@app.route('/')
def hello_world():
	width = 640
	height = 400
	img = Image.new('RGB', (width, height), (255,255,255))
	farba = (randint(0, 255), randint(0, 255), randint(0, 255))
	for x in range(200, 401):
		for y in range(100, 201):
			img.putpixel((x, y), farba)
	return serve_pil_image(img)
