import React from 'react';
import ReactDOM from 'react-dom';
import Grapher from "@windborne/grapher";

const rootEl = document.createElement('div');
document.body.appendChild(rootEl);

window.renderGrapher = (props) => {
    ReactDOM.render(<Grapher 
      customBoundsSelectors={props.boundsSelectors}
      exportStateController={(s) => window.s = s}
      //defaultBoundsCalculator='initial'
    	{...props} 
    />, rootEl);
};
