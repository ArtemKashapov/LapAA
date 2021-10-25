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

        b = bytearray(file.read())
        print('Картинка открыта')

    out = Laplacian(b).run()

    print('Картинка обработана')

    Image.fromarray(np.uint8(out), 'L').save("source\output.jpeg")
    return send_file("source\output.jpeg", )


if __name__ == '__main__':
    app.run(debug=False, port=5050)
