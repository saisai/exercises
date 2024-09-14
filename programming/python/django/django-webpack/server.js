const WebpackDevServer = require('webpack-dev-server');
const webpack = require('webpack');

const webpackConfig  = require('./webpack.config.js');
// webpackDevServer.addDevServerEntrypoints(config, options);
const compiler = webpack(webpackConfig );
// const server = new webpackDevServer(compiler, options);

const devServerOptions = { ...webpackConfig.devServer, open: true };
const server = new WebpackDevServer(devServerOptions, compiler);

// server.listen(3000, 'localhost', () => {
//   console.log('dev server listening on port 3000');
// });

const runServer = async () => {
  console.log('Starting server...');
  await server.start();
};
runServer();
