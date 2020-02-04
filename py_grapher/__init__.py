import webbrowser
import pathlib
import json
import os

class Plotter:
    def __init__(self, output_name='render.html'):
        self.series = []
        self.output_name = output_name

    def __enter__(self):
        self.series = []

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.render()

    def script_contents(self):
        return 'renderGrapher({ series: ' + json.dumps(self.series) + '});'

    def render(self):
        base_dir = pathlib.Path(__file__).parent.absolute()

        with open(str(base_dir) + '/index.html', 'r') as file :
            html_contents = file.read()
        
        html_contents = html_contents.replace('</body>', '<script>' + self.script_contents() + '</script></body>')

        with open(self.output_name, 'w') as file:
            file.write(html_contents)

        webbrowser.open('file://' + str(os.getcwd()) + '/' + self.output_name, new=2)

    def index(self, x_series):
        return x_series

    def plot(self, x_series, y_series, name=None):
        data = []
        for i in range(len(x_series)):
            data.append([float(x_series[i]), float(y_series[i])])

        self.series.append({
            'name': name,
            'data': data
        })
