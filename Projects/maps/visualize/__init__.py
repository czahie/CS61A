import http.server
import json
import webbrowser
import socket

from abstractions import *
from utils import distance

def draw_map(centroids, restaurants, ratings):
    """Write a JSON file containing inputs and load a visualization.

    Arguments:
    centroids -- A sequence of positions
    restaurants -- A sequence of restaurants
    ratings -- A dictionary from restaurant names to ratings
    """
    data = []
    locations = set()
    for restaurant in restaurants:
        p = tuple(restaurant_location(restaurant))
        cluster = min(enumerate(centroids), key=lambda v: distance(p, v[1]))[0]
        name = restaurant_name(restaurant)
        rating = ratings[name]
        if p not in locations:
            data.append({
                'x': p[0],
                'y': p[1],
                'weight': rating,
                'name': name,
                'cluster': cluster,
            })
            locations.add(p)
    with open('visualize/voronoi.json', 'w') as f:
        json.dump(data, f)
    load_visualization('voronoi.html')

port = 8000
base_url = 'http://localhost:{0}/visualize/'.format(port)

def load_visualization(url):
    """Load the visualization located at URL."""
    if not check_port():
        print('Address already in use! Check if recommend.py is running in a separate terminal.')
        return
    server = start_threaded_server()
    webbrowser.open_new(base_url + url)
    try:
        server.join()
    except KeyboardInterrupt:
        print('\nKeyboard interrupt received, exiting.')

class SilentServer(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        return

def check_port():
    sock = socket.socket()
    success = sock.connect_ex(('localhost', port))
    sock.close()
    return success

def start_server():
    server, handler = http.server.HTTPServer, SilentServer
    httpd = server(('', port), handler)
    sa = httpd.socket.getsockname()
    print('Serving HTTP on', sa[0], 'port', sa[1], '...')
    print('Type Ctrl-C to exit.')
    try:
        httpd.serve_forever()
    finally:
        httpd.server_close()

import threading
def start_threaded_server():
    thread = threading.Thread(target=start_server)
    thread.daemon = True
    thread.start()
    return thread
