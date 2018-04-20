from flask import Flask
from PIL import Image, ImageDraw
from flask import send_file
from io import BytesIO
import os


def create_fake_image(width, height, color='#ffffff', text=None):
    if not text:
        text = "{}x{}".format(width, height)
    
    img = Image.new('RGBA', (width, height), color)

    draw = ImageDraw.Draw(img)
    w, h = draw.textsize(text)
    draw.text(((width - w)/2 , (height - h)/2), text, fill="#FFFF00")

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


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
