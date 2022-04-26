from requests import get

def index(req): 
   headers = ({'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
      
   url = "https://api.themoviedb.org/3/movie/popular?api_key=eb99585a48f54fd6037b27da8567d4f4&language=en-GB&page=1"

   response = get(url , headers=headers)
   data = response.json()
   return [ f for f in data["results"]], 200
