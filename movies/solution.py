import requests
from movies import constants


def get_ids(discover_api):
    """
    Get all movie or tv show ids given the movie db api
    Args:
        discover_api (str): the get request for requesting movies or tv shows

    Returns:
        ids (list[int]): list of ids

    """

    response = requests.get(discover_api)

    assert(response.status_code == requests.codes.ok), f'Failed to call {discover_api}'

    results = response.json()

    # extract total pages to traverse
    total_pages = results['total_pages']

    page_num = 1

    ids = list()

    # traverse all page results
    while page_num <= total_pages:
        response = requests.get(discover_api + f'&page={page_num}')
        assert(response.status_code == requests.codes.ok), f'Failed to get results for page {page_num}'

        page_num += 1

        curr_page_results = response.json()['results']

        for title in curr_page_results:
            ids.append(title['id'])

    return ids


def get_actors(titles, api_type):
    """
    Get all cast members who appeared in a list of titles
    Args:
        titles (list[int]): list of movie or tv show title ids
        api_type (str): movie or tv api to pull from

    Returns:
        actors (list[int]): list of actor ids

    """

    # store actor ids in set because we only care that actor has been in at least 1 movie/show
    actors = set()

    for title_id in titles:
        if api_type == 'movie':
            response = requests.get(f'https://api.themoviedb.org/3/movie/{title_id}/credits?api_key=606aaffd7ca10f0b80804a1f0674e4e1')
        elif api_type == 'tv':
            response = requests.get(f'https://api.themoviedb.org/3/tv/{title_id}/credits?api_key=606aaffd7ca10f0b80804a1f0674e4e1&language=en-US')
        else:
            raise TypeError('API type must be "movie" or "tv"')

        assert(response.status_code == requests.codes.ok), f'Failed to request credits for {title_id}'

        results = response.json()

        cast_list = results['cast']

        for actor in cast_list:
            actors.add(actor['id'])

    return actors


def get_num_reoccurring_actors():
    """
    Get number of actors and actresses who were in at least one movie and at least one tv episode in December 2018
    Returns:
        (int): number of actors and actresses
    """
    movie_titles = get_ids(constants.movie_api)
    movie_actors = get_actors(movie_titles, 'movie')

    tv_titles = get_ids(constants.tv_api)
    tv_actors = get_actors(tv_titles, 'tv')

    return len(movie_actors & tv_actors)


if __name__ == '__main__':
    get_num_reoccurring_actors()
