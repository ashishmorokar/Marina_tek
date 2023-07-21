const express = require('express');
const app = express();
const path = (process.env.CUSTOM_STATICS_PATH || 'movies');

const allowCrossDomain = function(req, res, next) {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS');
    res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization, Content-Length, X-Requested-With');

    // intercept OPTIONS method
    if ('OPTIONS' == req.method) {
      res.send(200);
    }
    else {
      next();
    }
};

app.use(allowCrossDomain);

app.get('/movies', function (req, res, next) {
    res.status(200);
    res.sendFile(`${__dirname}/movies/index.json`);
  });

const port = (process.env.PORT || 3000);
app.listen(port, function () {
  console.log('Example app listening on port ' + port + '!');
});