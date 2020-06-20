from apiclient.discovery import build 
   
# Arguments that need to passed to the build function 
DEVELOPER_KEY = "" 
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
   
# creating Youtube Resource Object 
youtube_object = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, 
                                        developerKey = DEVELOPER_KEY) 
   
from flask import * 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def basic():
    if request.method == 'GET':
        videos = youtube_search_keyword('Indian Politics', 10)
        return render_template('index.html', videos=videos)
    return render_template('index.html')


def youtube_search_keyword(query, max_results): 
       
    # calling the search.list method to 
    # retrieve youtube search results 
    search_keyword = youtube_object.search().list(q = query, part = "id, snippet", 
                                               maxResults = max_results).execute()
    # extracting the results from search response 
    results = search_keyword.get("items", []) 
    print(results)
   
    # empty list to store video,  
    # channel, playlist metadata 
    videos = [] 
    playlists = [] 
    channels = [] 
       
    # extracting required info from each result object 
    for result in results: 
        # video result object 
        if result['id']['kind'] == "youtube#video": 
            videos.append("% s (% s) (% s) (% s)" % (result["snippet"]["title"], 
                            result["id"]["videoId"], result['snippet']['description'], 
                            result['snippet']['thumbnails']['default']['url'])) 
  
        # playlist result object
    return videos
if __name__ == "__main__": 
    app.run(debug=True)