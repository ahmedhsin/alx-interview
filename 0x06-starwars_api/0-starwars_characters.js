#!/usr/bin/node
const request = require('request');
const error = new Error('Something went wrong');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2] +'/';
const promise = new Promise((resolve, reject) => {
  request(url, (err, res, data) => {
    if (err) reject(error);
    resolve(data);
  });
});

promise.then((res) => {
  res = JSON.parse(res);
  res = res.characters;
  const promises = [];
  res.forEach((url) => {
    const npromise = new Promise((resolve, reject) => {
      request(url, (err, res, data) => {
        if (err) reject(error);
        data = JSON.parse(data);
        let num = url.split('/');
        num = parseInt(num[num.length - 2]);
        resolve([num, data.name]);
      });
    });
    promises.push(npromise);
  });
  Promise.all(promises).then((data) => {
    data.sort((f, s) => f[0] - s[0]);
    data.forEach((ele) => console.log(ele[1]));
  }, (err) => {
    console.log(err);
  });
}, (err) => {
  console.log(err);
});
