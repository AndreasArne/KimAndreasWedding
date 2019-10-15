const path = require('path');
const merge = require('webpack-merge');
const common = require('./webpack.common.js');
const webpack = require('webpack');

module.exports = merge(common, {
    watch: true,
    mode: 'development',
    resolve: {

    },
    devServer: {
        contentBase: path.join(__dirname, 'dist'),
        historyApiFallback: true
    },
    plugins: [
        new webpack.DefinePlugin({
            API_URL: JSON.stringify("http://localhost:8000")
        })
    ]
})