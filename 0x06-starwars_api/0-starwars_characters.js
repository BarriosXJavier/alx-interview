#!/usr/bin/node

const argv = process.argv;
const request = require('request');

// Check if a movie ID is provided
if (argv.length < 3) {
    console.error('Usage: ./<script> <movie_id>');
    process.exit(1);
}

const movieId = argv[2];
const urlFilm = 'https://swapi-api.alx-tools.com/api/films/';
const urlMovie = `${urlFilm}${movieId}/`;

request(urlMovie, function (error, response, body) {
    if (!error) {
        const fbody = JSON.parse(body);
        const characters = fbody.characters;

        if (characters && characters.length > 0) {
            const limit = characters.length;
            charRequest(0, characters, limit);
        }
    } else {
        console.error('Error:', error);
    }
});

function charRequest(idx, characters, limit) {
    if (idx === limit) {
        return;
    }
    request(characters[idx], function (error, response, body) {
        if (!error) {
            const rbody = JSON.parse(body);
            console.log(rbody.name);
            charRequest(idx + 1, characters, limit);
        } else {
            console.error('Error:', error);
        }
    });
}
