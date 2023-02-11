from chalice import Chalice
from utils import get_short_url, get_long_url, store_url

app = Chalice(app_name='url-shortener')


@app.route('/shorten', methods=['POST'])
def shorten():
    url = app.current_request.json_body['url']
    short_url = get_short_url()
    store_url(short_url, url)
    return {'url': short_url}


@app.route('/{short_url}')
def redirect(short_url):
    long_url = get_long_url(short_url)
    return app.current_response.redirects(long_url)
