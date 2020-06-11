import webbrowser
import pathlib
import json
import os
import datetime
class Plotter:
    def __init__(self, output_name=None,title=None,format_time=None):
        self.series = []
        self.bounds = []
        self.used_axis = set()
        self.title = title
        self.output_name = output_name
        self.output_dir = "py_grapher"
        self.format_time = format_time
        os.makedirs(self.output_dir,exist_ok=True)
        if self.output_name is None:
            if self.title is not None:
                self.output_name = self.title + ".html"
            else:
                self.output_name = "grapher.html"



    def __enter__(self):
        self.series = []

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.render()

    def script_contents(self):
        return 'renderGrapher({ series: ' + json.dumps(self.series) + ', boundsSelectors: ' + '[%s]'%(','.join(self.bounds)) + '}' + ');'

    def render(self):
        base_dir = pathlib.Path(__file__).parent.absolute()

        with open(str(base_dir) + '/index.html', 'r') as file :
            html_contents = file.read()
        
        html_contents = html_contents.replace('</body>', '<script>' + self.script_contents() + '</script></body>')
        
        if self.title is not None:
            html_contents = html_contents.replace('<title>Webpack App</title>','<title>%s</title>'%self.title)

        outfile = os.path.join(self.output_dir,self.output_name)
        with open(outfile, 'w') as file:
            file.write(html_contents)

        webbrowser.open('file://' + str(os.getcwd()) + '/' + outfile, new=2)

    def index(self, x_series):
        return x_series

    def addBounds(self, xmin, xmax, name=None):
        if name is None:
            name = 'bounds%d' % len(self.bounds)
        self.bounds.append(
        """{
        label: "%s",
        calculator: () => {
            return {
                minX: %d,
                maxX: %d
            }; 
        }
        }""" % (name,xmin,xmax))

    def getNextAxis(self):
        i = 0
        while "left-%d"%i in self.used_axis:
            i +=1
        return "left-%d"%i

    def plot(self, x_series, y_series, name=None, axis=None):
        data = []
        for i in range(len(x_series)):
            if self.format_time:
                x = datetime.datetime.fromtimestamp(x_series[i]).isoformat()
            else:
                x = float(x_series[i])
            data.append([x, float(y_series[i])])
        if axis is None:
            axis = self.getNextAxis()
        self.used_axis.add(axis)
        self.series.append({
            'name': name,
            'data': data,
            'axis': axis
        })
