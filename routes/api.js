"use strict";
const express = require('express');
const router = express.Router();


/* GET api listing. */
router.get('/', (req, res) => {
  res.send('api works');
});

router.get('/movies', (req, res) => {
  //res.send('sending movies list');
  res.send({"title": "Toy Story",
            "summary": "A story of a boy and his toys that come to life",
            "poster": "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
            "trailer": "https://www.youtube.com/watch?v=KYz2wyBy3kc"})
});

router.get('/sports', (req, res) => {
  let sports = mongoUtil.sports();
  sports.find({}).toArray((err, docs) => {
    // console.log(JSON.stringify(docs));

    // let sportNames = docs.map((sport) => sport.name);
    //sports component is expecting as javascript object with name property
    //no need to map to array like in the video

    res.json( docs );
  });

  // res.send([
  //   {name: "Weightlifting"},
  //   {name: "Cycling"},
  //   {name: "Gymnastics"}
  // ]);
});



module.exports = router;
