from fastapi import APIRouter, HTTPException
import aiohttp
import os
from datetime import datetime

router = APIRouter()

ALPHA_VANTAGE_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')
ALPHA_VANTAGE_BASE = 'https://www.alphavantage.co/query'

@router.get('/quote/{symbol}')
async def get_quote(symbol: str):
    """Get real-time quote for symbol"""
    try:
        async with aiohttp.ClientSession() as session:
            params = {
                'function': 'GLOBAL_QUOTE',
                'symbol': symbol,
                'apikey': ALPHA_VANTAGE_KEY
            }
            async with session.get(ALPHA_VANTAGE_BASE, params=params) as resp:
                data = await resp.json()
                return {
                    'symbol': symbol,
                    'bid': float(data.get('Global Quote', {}).get('05. price', 0)),
                    'ask': float(data.get('Global Quote', {}).get('05. price', 0)) + 0.0005,
                    'last_update': datetime.utcnow(),
                    'change': float(data.get('Global Quote', {}).get('09. change', 0)),
                    'change_percent': float(data.get('Global Quote', {}).get('10. change percent', '0').strip('%'))
                }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get('/intraday/{symbol}')
async def get_intraday(symbol: str, interval: str = '5min'):
    """Get intraday data"""
    try:
        return {
            'symbol': symbol,
            'interval': interval,
            'data': [
                {'time': '10:00', 'open': 1.0950, 'high': 1.0980, 'low': 1.0920, 'close': 1.0975},
                {'time': '10:05', 'open': 1.0975, 'high': 1.1000, 'low': 1.0960, 'close': 1.0995},
                {'time': '10:10', 'open': 1.0995, 'high': 1.1020, 'low': 1.0985, 'close': 1.1015},
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))