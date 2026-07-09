# Acuiring Reviews

1. Open the Yelp review page (https://www.yelp.com/biz/busch-gardens-tampa-bay-tampa-5?osq=Amusement+Parks)
2. Open the browser console, paste in the contents of `scraper.js`.
3. Run the script, advance to next page, repeat until at least 500 reviews acquired.
4. After 500 reviews acquired they will appear as raw JSON in the page, copy them to `reviews.json`.

# Setup

1. Create a virtual environment: `python3 -m venv venv`
2. Activate it:
   - macOS/Linux: `source venv/bin/activate`
   - Windows: `venv\Scripts\activate`
3. Install the requirements: `pip install -r requirements.txt`
4. Download the spaCy language model: `python -m spacy download en_core_web_sm`
5. Run the preprocessing script: `python prep-data.py`
