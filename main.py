from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import re

app = FastAPI(title="Sentiment Analysis API", version="1.0.0")

class SentimentRequest(BaseModel):
    sentences: List[str]

class SentimentResult(BaseModel):
    sentence: str
    sentiment: str

class SentimentResponse(BaseModel):
    results: List[SentimentResult]

# Sentiment dictionaries
HAPPY_WORDS = {
    'love', 'like', 'great', 'good', 'awesome', 'amazing', 'fantastic', 'wonderful',
    'excellent', 'perfect', 'happy', 'joy', 'pleased', 'delighted', 'brilliant',
    'outstanding', 'superb', 'marvelous', 'terrific', 'fabulous', 'smile', 'laugh',
    'enjoy', 'adore', 'wonderful', 'bliss', 'ecstatic', 'thrilled', 'positive'
}

SAD_WORDS = {
    'hate', 'terrible', 'awful', 'bad', 'horrible', 'sad', 'angry', 'mad', 'upset',
    'disappointed', 'frustrated', 'annoyed', 'depressed', 'miserable', 'unhappy',
    'dislike', 'despise', 'loathe', 'regret', 'sorry', 'cry', 'tears', 'grief',
    'sorrow', 'pain', 'suffering', 'negative', 'worst', 'hateful', 'awful'
}

POSITIVE_EMOJIS = {':)', ':-)', '😊', '😄', '😍', '🤗', '👍', '🥰', '😁', '🙂'}
NEGATIVE_EMOJIS = {':(', ':-(', '😢', '😭', '😠', '👎', '😞', '💔', '😤', '😔'}

def analyze_sentiment(sentence: str) -> str:
    """
    Analyze sentiment using rule-based approach with word matching and patterns
    """
    sentence_lower = sentence.lower().strip()
    
    # Check for emojis first
    for emoji in POSITIVE_EMOJIS:
        if emoji in sentence:
            return "happy"
    for emoji in NEGATIVE_EMOJIS:
        if emoji in sentence:
            return "sad"
    
    # Count positive and negative words
    positive_count = 0
    negative_count = 0
    
    words = re.findall(r'\b\w+\b', sentence_lower)
    
    for word in words:
        if word in HAPPY_WORDS:
            positive_count += 1
        if word in SAD_WORDS:
            negative_count += 1
    
    # Check for intensifiers and negations
    if any(word in sentence_lower for word in ['not', "n't", 'no', 'never']):
        # Simple negation handling - swap counts if negation is present
        positive_count, negative_count = negative_count, positive_count
    
    # Check for exclamation marks and question marks
    if '!' in sentence and positive_count > 0:
        positive_count += 1
    if '?' in sentence and negative_count > 0:
        negative_count += 1
    
    # Determine sentiment based on counts
    if positive_count > negative_count:
        return "happy"
    elif negative_count > positive_count:
        return "sad"
    else:
        return "neutral"

@app.post("/sentiment", response_model=SentimentResponse)
async def analyze_batch_sentiment(request: SentimentRequest):
    """
    Analyze sentiment for multiple sentences in batch
    """
    try:
        results = []
        
        for sentence in request.sentences:
            if not sentence or not sentence.strip():
                # Handle empty sentences as neutral
                sentiment = "neutral"
            else:
                sentiment = analyze_sentiment(sentence)
            
            results.append({
                "sentence": sentence,
                "sentiment": sentiment
            })
        
        return {"results": results}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

@app.get("/")
async def root():
    return {"message": "Sentiment Analysis API is running", "version": "1.0.0"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
