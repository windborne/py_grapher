import React from 'react';
import ReactDOM from 'react-dom';
import Grapher from "@windborne/grapher";

const rootEl = document.createElement('div');
document.body.appendChild(rootEl);

window.renderGrapher = (props) => {
    ReactDOM.render(<Grapher {...props} />, rootEl);
};
