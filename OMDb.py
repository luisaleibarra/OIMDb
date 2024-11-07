import requests

# Your OMDb API key
api_key = 'd0df735a'  # Replace with your actual API key

# Base URL for OMDb API
base_url = 'http://www.omdbapi.com/'

# Parameters for the API request
params = {
    'apikey': api_key,
    't': 'Top Gun: Maverick'
}

# Make the API request
response = requests.get(base_url, params=params)
data = response.json()

# Check if the response was successful
if data.get('Response') == 'True':
    # Display movie details
    print(f"Title: {data.get('Title')}")
    print(f"Year: {data.get('Year')}")
    print(f"Rated: {data.get('Rated')}")
    print(f"Released: {data.get('Released')}")
    print(f"Runtime: {data.get('Runtime')}")
    print(f"Genre: {data.get('Genre')}")
    print(f"Director: {data.get('Director')}")
    print(f"Writer: {data.get('Writer')}")
    print(f"Actors: {data.get('Actors')}")
    print(f"Plot: {data.get('Plot')}")
    print(f"Language: {data.get('Language')}")
    print(f"Country: {data.get('Country')}")
    print(f"Awards: {data.get('Awards')}")
    print(f"Poster: {data.get('Poster')}")
    print(f"Metascore: {data.get('Metascore')}")
    print(f"imdbRating: {data.get('imdbRating')}")
    print(f"imdbVotes: {data.get('imdbVotes')}")
    print(f"imdbID: {data.get('imdbID')}")
    print(f"Type: {data.get('Type')}")
    print(f"DVD: {data.get('DVD')}")
    print(f"BoxOffice: {data.get('BoxOffice')}")
    print(f"Production: {data.get('Production')}")
    print(f"Website: {data.get('Website')}")
else:
    print("Movie not found or an error occurred.")
