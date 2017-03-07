'use strict';

const express = require('express');

// Constants
const PORT = 8080;

// App
const app = express();
app.get('/', function (req, res) {
  let name = req.query.name;
  if(!name){
    name = "world";
  }
  res.send('Hello 1 ' + name + "\n");
});

app.listen(PORT);
console.log('Running on http://localhost:' + PORT);
