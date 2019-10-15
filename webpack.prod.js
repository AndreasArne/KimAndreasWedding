const merge = require('webpack-merge');
const common = require('./webpack.common.js');

module.exports = merge(common, {
    watch: false,
    mode: 'production',
    plugins: [
        new webpack.DefinePlugin({
            API_URL: JSON.stringify("https://bröllop.arnesson.dev/api")
        })
    ]
})