import tempfile
from flask import Flask, request, make_response
from flask.views import MethodView
import subprocess
import os

app = Flask(__name__)


def gpx2png(filename: str, output_fn: str):
    cur_dir = os.getcwd()
    try:
        dir_name = '/tmp'
        os.chdir(dir_name)
        subprocess.run(['/usr/bin/perl', '/usr/src/converter.pl', '-o', output_fn, '-z', '-9', filename],
                       check=True)
    finally:
        os.chdir(cur_dir)


def read_image(fn):
    with open(fn, 'rb') as f:
        return f.read()


class UploadAPI(MethodView):
    def get(self):
        return "Post a raw GPX to this service to convert it into a PNG"

    def post(self):
        tempfile.NamedTemporaryFile()
        with tempfile.NamedTemporaryFile() as f:
            data = request.get_data()
            f.write(data)
            f.seek(0)
            f.flush()

            fd, out = tempfile.mkstemp(suffix=b".png")
            os.close(fd)

            try:
                gpx2png(filename=str(f.name), output_fn=out)
                image = read_image(out)
                r = make_response(image)
                r.headers['Content-Type'] = 'image/png'
                return r
            finally:
                if os.path.exists(out):
                    os.unlink(out)


upload_view = UploadAPI.as_view('upload_api')
app.add_url_rule('/', view_func=upload_view, methods=['GET', 'POST', ])
