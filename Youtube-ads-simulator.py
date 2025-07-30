#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
YouTube Ads Simulator API
Simulates which ad categories would be shown on videos from any YouTube channel.

Tech Stack:
- Python
- YouTube Data API v3
- Simulated keyword matching
- Output: Keywords matched per video (top 10)

Author: [Your Name]
"""

from googleapiclient.discovery import build
import pandas as pd

# ----------------------------
# 🔒 Enter your credentials here
# ----------------------------

API_KEY = "YOUR_YOUTUBE_API_KEY"  # <-- Replace with your own Google API key
CHANNEL_ID = "YOUR_YOUTUBE_CHANNEL_ID"  # <-- Replace with a valid YouTube channel ID

# ----------------------------
# Step 1: Fetch 10 latest video titles from channel
# ----------------------------

def get_video_titles(api_key, channel_id, max_results=10):
    youtube = build('youtube', 'v3', developerKey=api_key)

    response = youtube.channels().list(
        part='contentDetails',
        id=channel_id
    ).execute()

    items = response.get('items', [])
    if not items:
        raise ValueError("No items found. Check if the channel ID is correct or public.")

    uploads_playlist = items[0]['contentDetails']['relatedPlaylists']['uploads']

    playlist_items = youtube.playlistItems().list(
        part='snippet',
        playlistId=uploads_playlist,
        maxResults=max_results
    ).execute()

    videos = []
    for item in playlist_items['items']:
        title = item['snippet']['title']
        description = item['snippet']['description']
        videos.append((title, description))

    return videos

# ----------------------------
# Step 2: Simulate ad keywords based on video metadata
# ----------------------------

def simulate_ads(video_metadata):
    ad_keywords = {
        "gaming": ["game", "play", "stream", "fps", "rank"],
        "horror": ["ghost", "horror", "jump", "dead", "scare"],
        "funny": ["funny", "meme", "laugh", "joke", "comedy"]
    }

    ads_output = []
    for title, desc in video_metadata:
        combined_text = (title + " " + desc).lower()
        matched = set()
        for category, keywords in ad_keywords.items():
            if any(word in combined_text for word in keywords):
                matched.update(ad_keywords[category])
        if not matched:
            matched.update(["generic", "youtube", "ads"])
        ads_output.append({
            "Video Title": title,
            "Keywords Detected": ", ".join(list(matched)[:10])  # Limit to 10
        })

    return pd.DataFrame(ads_output)

# ----------------------------
# Run the Simulation
# ----------------------------

if __name__ == "__main__":
    video_data = get_video_titles(API_KEY, CHANNEL_ID)
    df_ads = simulate_ads(video_data)
    print(df_ads)

