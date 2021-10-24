from flask import Flask, request, send_file
from laplacian import Laplacian
from PIL import Image
import numpy as np

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='KRUTOY_PROJECT_LAPAA',
)

@app.route('/get-edges', methods=['POST', 'GET'])
def process():
    # if request.method == 'POST':
    if 'file' in request.files:
        file = request.files['file']
        print('File получен')

    with open('source\input_image-1.jpg', "rb") as image:
        b = bytearray(image.read())
    
    out = Laplacian(b).run()
    return send_file(out.tobytes(), attachment_filename='tiger.jpg')



if __name__ == '__main__':
    app.run(debug=False, port=5050)