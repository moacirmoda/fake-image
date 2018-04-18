import os
from app import app, create_fake_image
import unittest
import tempfile
from PIL import Image
from io import BytesIO


class AppTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        
    def test_should_create_fake_image(self):
        img = create_fake_image(200, 300)
        assert isinstance(img, Image.Image)
        assert img.width == 200
        assert img.height == 300
    
    def test_should_return_png_image(self):
        response = self.app.get('/250x350')
        assert response.status_code == 200
        assert response.mimetype == 'image/png'

        img_io = BytesIO(response.data)
        img = Image.open(img_io)
        assert img.width == 250
        assert img.height == 350

        response = self.app.get('/250')
        img_io = BytesIO(response.data)
        img = Image.open(img_io)
        assert img.width == 100
        assert img.height == 100

        response = self.app.get('/')
        img_io = BytesIO(response.data)
        img = Image.open(img_io)
        assert img.width == 100
        assert img.height == 100

if __name__ == '__main__':
    unittest.main()
