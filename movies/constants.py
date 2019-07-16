# access key for https://www.themoviedb.org/
api_key = '606aaffd7ca10f0b80804a1f0674e4e1'

# time constraints
start_date = '2018-12-01'
end_date = '2018-12-31'

# api for accessing movies and tv shows
movie_api = f'https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language=en-US&sort_by=primary_release_date.asc&primary_release_date.gte={start_date}&primary_release_date.lte={end_date}'
tv_api = f'https://api.themoviedb.org/3/discover/tv?api_key={api_key}&language=en-US&sort_by=first_air_date.asc&first_air_date.gte={start_date}&first_air_date.lte={end_date}&timezone=America%2FNew_York&include_null_first_air_dates=false'
