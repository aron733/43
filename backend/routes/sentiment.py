from fastapi import APIRouter, HTTPException
from datetime import datetime
from typing import Dict

router = APIRouter()

@router.get('/market')
async def get_market_sentiment() -> Dict:
    """Get market sentiment in real-time"""
    try:
        return {
            'timestamp': datetime.utcnow(),
            'overall_sentiment': 'Bullish',
            'sentiment_score': 0.75,
            'currency_pairs': {
                'EUR/USD': {'sentiment': 'Bullish', 'score': 0.80},
                'GBP/USD': {'sentiment': 'Neutral', 'score': 0.50},
                'USD/JPY': {'sentiment': 'Bearish', 'score': 0.30}
            },
            'news_count': 42,
            'social_sentiment': 0.65
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get('/crypto')
async def get_crypto_sentiment() -> Dict:
    """Get crypto sentiment"""
    try:
        return {
            'Bitcoin': {'sentiment': 'Bullish', 'score': 0.72},
            'Ethereum': {'sentiment': 'Bullish', 'score': 0.68},
            'overall': 'Positive'
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))