"use strict";
const express = require('express');
const router = express.Router();


// API listings
router.get('/', (req, res) => {
  res.send('api works');
});

// return movies list
router.get('/movies', (req, res) => {
  res.send({
            "title1": "Toy Story",
            "summary1": "A story of a boy and his toys that come to life",
            "poster1": "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
            "trailer1": "https://www.youtube.com/watch?v=KYz2wyBy3kc",
            "title2": "Avatar",
            "summary2": "A marine on an alien planet",
            "poster2": "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
            "trailer2": "https://www.youtube.com/watch?v=5PSNL1qE6VY",
            "title3": "Reservoir Dogs",
            "summary3": "A heist gone wrong",
            "poster3": "https://upload.wikimedia.org/wikipedia/en/f/f6/Reservoir_dogs_ver1.jpg",
            "trailer3": "https://www.youtube.com/watch?v=vayksn4Y93A",
            "title4": "Snatch",
            "summary4": "Two sides of the London unground collide",
            "poster4": "https://upload.wikimedia.org/wikipedia/en/a/a7/Snatch_ver4.jpg",
            "trailer4": "https://www.youtube.com/watch?v=Q8jbt0wBkMI",
            "title5": "Mallrats",
            "summary5": "Just another day at the mall",
            "poster5": "https://upload.wikimedia.org/wikipedia/en/9/96/Mallrats.jpg",
            "trailer5": "https://www.youtube.com/watch?v=_eVo7aBze1w",
            "title6": "In Bruges",
            "summary6": "Two hit men hide out in a small town in Belgium",
            "poster6": "https://upload.wikimedia.org/wikipedia/en/6/63/In_Bruges_Poster.jpg",
            "trailer6": "https://www.youtube.com/watch?v=KoE9edjEDCI"
          });
        });

module.exports = router;
