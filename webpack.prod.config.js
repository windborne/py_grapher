const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const HtmlWebpackInlineSourcePlugin = require('html-webpack-inline-source-plugin');

module.exports = {
    mode: 'production',
    entry: './js/index.js',
    devtool: 'source-map',
    output: {
        path: path.resolve(__dirname, 'py_grapher'),
        filename: 'bundle.js'
    },
    optimization: {
        minimize: true
    },
    module: {
        rules: [
            {
                test: /(js|grapher).*\.s?css$/,
                use: ['style-loader', 'css-loader', 'sass-loader']
            },
            {
                test: /(js|grapher).*\.js$/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ["@babel/preset-env", "@babel/preset-react"]
                    }
                }
            },
            {
                test: /(js|grapher).*\.(vert|frag|glsl)$/,
                use: 'webpack-glsl-loader'
            }
        ]
    },
    plugins: [
        new HtmlWebpackPlugin({
            inlineSource: '.(js|css)$'
        }),
        new HtmlWebpackInlineSourcePlugin()
    ]
};
