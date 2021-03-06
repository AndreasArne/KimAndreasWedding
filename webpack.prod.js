const merge = require('webpack-merge');
const common = require('./webpack.common.js');
const webpack = require('webpack');

module.exports = merge(common, {
    watch: false,
    mode: 'production',
    plugins: [
        new webpack.DefinePlugin({
            API_URL: JSON.stringify("https://brollop.arnesson.dev/api")
        })
    ]
})