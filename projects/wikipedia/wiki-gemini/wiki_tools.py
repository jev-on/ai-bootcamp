import requests

def get_wikipedia_summary(topic: str) -> str:
    """Fetches a summary of a topic from Wikipedia.
    
    Args:
        topic: The subject to look up on Wikipedia.
    """
    print(f"--- [TOOL] Searching Wikipedia for: {topic}...")
    
    formatted_topic = topic.replace(" ", "_")
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{formatted_topic}"
    
    headers = {
        "User-Agent": "AIBootcampAgent/1.0 (https://github.com/jev-on/ai-bootcamp)"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data.get("extract", "No summary found for this topic.")
    elif response.status_code == 404:
        return "Topic not found on Wikipedia. Try a different search term."
    else:
        return f"Error connecting to Wikipedia: Status {response.status_code}"

def search_wikipedia(query: str, limit: int = 5) -> list[str]:
    """
    Search Wikipedia for a topic and return a list of page titles.
    
    Args:
        query: The search term (e.g., "Artificial Intelligence").
        limit: The number of results to return (max 50).
    """
    print(f"--- [TOOL] Searching Wikipedia articles for: {query}...")
    url = "https://en.wikipedia.org/w/api.php"
    
    params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "utf8": "1",
        "format": "json",
        "srlimit": limit
    }
    
    headers = {
        "User-Agent": "AIBootcampAgent/1.0 (https://github.com/jev-on/ai-bootcamp)"
    }
    
    response = requests.get(url, params=params, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        search_results = data.get("query", {}).get("search", [])
        return [result["title"] for result in search_results]
    else:
        return []
