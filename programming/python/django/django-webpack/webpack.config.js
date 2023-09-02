var path = require("path");
var BundleTracker = require('webpack-bundle-tracker');
var MiniCssExtractPlugin = require('mini-css-extract-plugin');


module.exports = {
  context: __dirname,
  entry: './assets/js/index',
  output: {
    path: path.resolve('./assets/bundles/'),
    publicPath: 'http://localhost:3000/dist/',
    filename: "[name]-[hash].js",
    chunkFilename: "[name]-[hash].js"
  },
  
  mode: 'development',

  plugins: [
    new BundleTracker({filename: './webpack-stats.json'}),
    new MiniCssExtractPlugin({
      filename: '[name]-[hash].css',
      chunkFilename: '[name]-[hash].css',
    }),
  ],

  module: {
    rules: [
      // we pass the output from babel loader to react-hot loader
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
        },
      },
      // {
      //   test: /\.css$/,
      //   use: [MiniCssExtractPlugin.loader, 'css-loader'],
      // },
      {
        test: /\.s[ac]ss$/i,
        use: [
          // Creates `style` nodes from JS strings
          "style-loader",
          // Translates CSS into CommonJS
          "css-loader",
          // Compiles Sass to CSS
          "sass-loader",
        ],
      },
      {
        test: /\.md$/,
        use: 'raw-loader'
      },
    ],
  },

  resolve: {
    modules: ['node_modules'],
    extensions: ['.js', '.jsx']
  },
  devServer: {
    static: path.resolve(__dirname, './dist'),
    port: 3000,
    hot: true,
    compress: true,
    historyApiFallback: true,
    headers: { 'Access-Control-Allow-Origin': '*' },
  },
}
