const plugins = [
  [
    'babel-plugin-import',
    {
      libraryName: '@mui/material',
      libraryDirectory: '',
      camel2DashComponentName: false,
    },
    'core',
  ],
  [
    'babel-plugin-import',
    {
      libraryName: '@mui/icons-material',
      libraryDirectory: '',
      camel2DashComponentName: false,
    },
    'icons',
  ],  
  [
    'babel-plugin-transform-imports',
    {
      '@material-ui/core': {
        'transform': '@material-ui/core/${member}',
        'preventFullImport': true
      }
    }
  ],
  
];

module.exports = { plugins,
  presets:[
    "@babel/preset-env",
    "@babel/preset-react",
],
"exclude": "node_modules/**'",
};