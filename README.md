
## Installation
```bash
pip install git+ssh://git@github.com/windborne/py_grapher.git
```

## Usage
Example:
```python
from py_grapher import Plotter

with Plotter() as plt:
    x_values = [0, 1, 2]
    y_values = [5, 6, 7]
    plt.plot(x_values, x_values)
```

When initializing `Plotter`, you can optionally pass in a file name to save the graph in.
If you pass nothing in, it will default to writing `render.html` in the current working directory.

With a `with` statement, the plotter will automatically render on exit.
You can also trigger manual rendering by calling the `render()` method.

The `plot` method takes in three arguments:
 - x_values, a list or np array of x axis values
 - y_values, which it expects to have the same length as x_values
 - name, an optional parameter for the name of the series

## Developing

### Updating the javascript
To rebuild the frontend, run `npm run build`. 
This will update py_grapher/index.html with the latest version.

You can upgrade the underlying grapher engine by updating the version in package.json, then re-running `npm install`, or by running `npm upgrade @windborne/grapher`. This requires that you or someone else has pushed a new version.

If it can't install the grapher engine for authentication reasons, you need to authenticate with github packages as an npm registry. 
See [github documentation](https://help.github.com/en/github/managing-packages-with-github-packages/configuring-npm-for-use-with-github-packages#authenticating-to-github-packages) for instructions.  
