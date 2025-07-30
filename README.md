This API-powered mini-project allows users to simulate which ad categories might appear on a YouTube channel based purely on video titles and descriptions. It mimics contextual ad targeting logic using basic NLP and keyword matching, giving a fun and educational look into how platforms like YouTube might infer advertising content from video metadata — without needing personal data or watch history.

Features
- Input any YouTube Channel ID
- Automatically fetch the latest 10 videos
- Use keyword-based logic to simulate likely ad categories (e.g., Gaming, Horror, Funny)
- Built with Python + YouTube Data API + Pandas
- Clean, customizable, and open for extension (e.g., real-time serving via FastAPI or Streamlit)

Use Cases
- Show off API integration skills in a portfolio project
- Practice lightweight NLP and keyword-based classification
- Build beginner-level recommender system prototypes
- Teach others how ad targeting works with no privacy risks

Tech Stack
- Python
- google-api-python-client
- pandas
- (Optional: FastAPI, Streamlit, Flask if you want to deploy)

How It Works
1. You provide a YouTube channel ID
2. The app calls the YouTube Data API to fetch recent video metadata
3. Keywords in video titles/descriptions are matched to simulated ad categories
4. Results are displayed as a DataFrame or returned via API

