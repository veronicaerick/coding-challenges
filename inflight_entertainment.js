// given the length of a flight and a list of movie lengths, see if there is
// time to watch two without going over the time of the flight

var movies_flight_len = funciton(flight_len, movie_lens) {
    for (var i =0; i < movie_lens; i++ ) {
        for (var j =0; j < movie_lens) {
            if movie_lens[i] + movie_lens[j] == flight_len
                return true;
        }
    }
}