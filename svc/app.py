from chalice import Chalice
import os

app = Chalice(app_name='awshelper')


@app.route('/')
def index():
    return {'hello': 'world'}


@app.route('/geturl')
def get_geturl():
    bucket = os.environ.get('bucket', None)

    if bucket:
        return {'get': 'url'}
    else:
        return {'error': 'bucket not found'}


@app.route('/posturl')
def get_posturl():
    bucket = os.environ.get('bucket', None)

    if bucket:
        return {'port': 'url'}
    else:
        return {'error': 'bucket not found'}
