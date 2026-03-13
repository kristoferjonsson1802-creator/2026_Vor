const fs = require('fs');
const path = require('path');

const dataPath = path.join(__dirname, '..', 'data', 'artists.json');

const getAllArtists = () => {
    const rawData = fs.readFileSync(dataPath, 'utf-8');
    return JSON.parse(rawData);
};

const getArtistById = (id) => {
    const artists = getAllArtists();
    return artists.find(artist => artist.id === id);
};

module.exports = {
    getAllArtists,
    getArtistById
};