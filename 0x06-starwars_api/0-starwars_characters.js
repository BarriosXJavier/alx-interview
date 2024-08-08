#!/usr/bin/node

import request from 'request';

// Check if a movie ID is provided as a command-line argument
if (process.argv.length < 3) {
    console.error('Usage: ./<script> <movie_id>');
    process.exit(1);
}

// get movie id from the command-line
const movieId = process.argv[2];

// Define the API endpoint for the specified movie
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Send a GET request to the Star Wars API
request(url, (error, response, body) => {
    if (error) {
        console.error(error);
        return;
    }

    // Parse the response body as JSON
    const data = JSON.parse(body);

    // Iterate over each character URL in the movie's character list
    data.characters.forEach((characterUrl) => {
        // Send a GET request to each character URL
        request(characterUrl, (error, response, body) => {
            if (error) {
                console.error(error);
                return;
            }

            // Parse the character data and print the character name
            const character = JSON.parse(body);
            console.log(character.name);
        });
    });
});
