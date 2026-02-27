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
