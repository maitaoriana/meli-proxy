from requests import get
from app import app

MELI_URL = 'https://api.mercadolibre.com/'


@app.route('/', defaults={'url': ''})
@app.route('/<path:url>')
def proxy(url):
    return get(f'{MELI_URL}{url}').content

