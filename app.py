from flask import Flask
from PIL import Image, ImageDraw
from flask import send_file
from io import BytesIO


def create_fake_image(width, height, color='#ffffff', text=None):
    if not text:
        text = "{}x{}".format(width, height)
    
    img = Image.new('RGBA', (width, height), color)

    draw = ImageDraw.Draw(img)
    w, h = draw.textsize(text)
    draw.text(((width - w)/2,(height - h)/2), text, fill="#000000")

    return img


app = Flask(__name__)


@app.route('/', defaults={'size': None})
@app.route('/<size>')
def index(size):
    try:
        width, height = size.split("x")
        width = int(width)
        height = int(height)
    except:
        width, height = (100, 100)

    pil_img = create_fake_image(width, height)
    img_io = BytesIO()
    pil_img.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')
