def can_two_movies_fill_flight(movie_lengths, flight_length):
    movie_lengths = set()

    for first_movie_length in movie_lengths:
        matching_second_movie_length = flight_length - first_movie_length
        if matching_second_movie_length in movie_lengths:
            return True

        movie_lengths.add(first_movie_length)