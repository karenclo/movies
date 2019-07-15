# movies

Approach:
1. get number of pages that contain movies released Dec 1 - Dec 31 2018
2. traverse pages and store all movie ids
3. pass in ids to /movies/{movie_id}/credits and create set extracting name from each object in cast list
4. get number of pages that contain TV shows aired Dec 1 - Dec 31 2018
5. traverse pages and store all tv show ids
6. pass in ids to /tv/{tv_id}/credits and create set extracting name from each object in cast list
7. return intersection between movie_set and tv_set

Corner Cases:
- API returns error/timeout
- Cast list is empty


