#!/usr/bin/node

'use strict'

import { get } from 'https'

if (process.argv.length < 3) {
    console.error('Usage: node script.js <movie_id>')
    process.exit(1)
}

const movieId = parseInt(process.argv[2], 10)

const options = {
    hostname: 'swapi-api.alx-tools.com',
    path: `/api/films/${movieId}/`,
    method: 'GET'
}

get(options, (res) => {
    let data = ''

    res.on('data', (chunk) => {
        data += chunk
    })

    res.on('end', () => {
        const { characters } = JSON.parse(data)
        characters.forEach((characterUrl) => {
            get(characterUrl, (charRes) => {
                let charData = ''

                charRes.on('data', (chunk) => {
                    charData += chunk
                })

                charRes.on('end', () => {
                    const { name } = JSON.parse(charData)
                    console.log(name)
                })
            }).on('error', (err) => {
                console.error(`Error fetching character: ${err.message}`)
            })
        })
    })
}).on('error', (err) => {
    console.error(`Error fetching movie data: ${err.message}`)
})