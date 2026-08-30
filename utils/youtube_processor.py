import re
from youtube_transcript_api import YouTubeTranscriptApi

def extract_youtube_id(url):
    pattern = r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:watch\?v=|embed\/|v\/)|youtu\.be\/)([\w-]{11})'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None

def get_youtube_transcript(video_url):
    video_id = extract_youtube_id(video_url)
    if not video_id:
        raise ValueError("Invalid YouTube URL format.")
    
    if hasattr(YouTubeTranscriptApi, 'get_transcript'):
        try:
            data = YouTubeTranscriptApi.get_transcript(video_id, languages=['en', 'hi', 'en-IN'])
        except Exception:
            data = YouTubeTranscriptApi.get_transcript(video_id)
    else:
        api = YouTubeTranscriptApi()
        try:
            data = api.fetch(video_id, languages=['en', 'hi', 'en-IN'])
        except Exception:
            data = api.fetch(video_id)
    
    transcript_texts = []
    for item in data:
        if isinstance(item, dict):
            transcript_texts.append(item.get('text', ''))
        elif hasattr(item, 'text'):
            transcript_texts.append(item.text)
    
    return " ".join(transcript_texts)