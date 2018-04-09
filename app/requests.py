import urllib.request,json
from .models import Source, Article

#getting api key
api_key = None

def configure_request(app):
    global api_key
    api_key = app.config['NEWS_API_KEY']

def get_sources():
    get_sources_url = 'https://newsapi.org/v1/sources'

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)
    return sources_results

def process_sources(source_list):

	'''
	Function  that processes the sources result and transform them to a list of Objects
	Args:
	sources_results: A list of dictionaries that contain sources details
	Returns :
	sources_list: A list of sources objects
	'''
    source_results = []

    for source_item in source_list:
        id = source_item.get('id')
        name = sourrce_item.get('name')
        description = source_item.get('description')

        source_object = Source(id,name,description)

        source_results.append(source_object)

    return source_results
