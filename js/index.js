import React from 'react';
import ReactDOM from 'react-dom';
import Multigrapher from "@windborne/grapher/src/multigrapher.js";

const rootEl = document.createElement('div');
document.body.appendChild(rootEl);

window.renderGrapher = (props) => {
    ReactDOM.render(<Multigrapher
      customBoundsSelectors={props.boundsSelectors}
      exportStateController={(s) => window.s = s}
      //defaultBoundsCalculator='initial'
      sidebarEnabled={true}
      {...props} 
    />, rootEl);
};
