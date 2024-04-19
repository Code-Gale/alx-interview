#!/usr/bin/node

const request = require('request');

const exactOrder = (actors, x) => {
  if (x === actors.length) return;
  request(actors[x], function (err, res, body) {
    if (err) {
      console.error(err);
      return;
    }
    console.log(JSON.parse(body).name);
    exactOrder(actors, x + 1);
  });
};

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, body) {
  if (err) {
    console.error(err);
    return;
  }
  const actors = JSON.parse(body).characters;
  exactOrder(actors, 0);
});
