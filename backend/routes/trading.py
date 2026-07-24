from fastapi import APIRouter, HTTPException
import os
import aiohttp
from datetime import datetime

router = APIRouter()

OANDA_API_KEY = os.getenv('OANDA_API_KEY')
OANDA_ACCOUNT_ID = os.getenv('OANDA_ACCOUNT_ID')
OANDA_BASE_URL = 'https://api-fxpractice.oanda.com'

@router.get('/positions')
async def get_positions():
    """Get all open positions"""
    try:
        return {
            'positions': [
                {'instrument': 'EUR_USD', 'long': 50000, 'short': 0, 'pl': 250.50},
                {'instrument': 'GBP_USD', 'long': 0, 'short': 25000, 'pl': -120.25}
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get('/trades')
async def get_trades():
    """Get all active trades"""
    try:
        return {
            'trades': [
                {
                    'id': 'trade_001',
                    'instrument': 'EUR_USD',
                    'side': 'BUY',
                    'units': 50000,
                    'entryPrice': 1.0950,
                    'currentPrice': 1.0980,
                    'unrealizedPL': 150.00
                }
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post('/order')
async def create_order(instrument: str, units: int, side: str):
    """Create new order"""
    try:
        return {
            'orderId': 'order_001',
            'instrument': instrument,
            'units': units,
            'side': side,
            'status': 'EXECUTED',
            'executionTime': datetime.utcnow()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))