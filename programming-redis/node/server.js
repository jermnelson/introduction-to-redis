var app = require('express')(),
  redis = require('redis'),
  swig = require('swig'),
  client = redis.createClient();

app.engine('html', swig.renderFile);
app.set('view engine', 'html');
app.set('views', __dirname + '/views');

// Disabling all caching (both Express and Swig
app.set('view cache', false);
swig.setDefaults({ cache: false });

app.get('/', function (req, res) {
  client.info(function(err, reply) {
    var info = reply;
    res.render('index', { info: info });

  });
});

app.listen(1337);
console.log('Application Started on http://localhost:1337/');
