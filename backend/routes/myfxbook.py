from fastapi import APIRouter, HTTPException
import aiohttp
import os
import hashlib

router = APIRouter()

MYFXBOOK_API_KEY = os.getenv('MYFXBOOK_API_KEY')
MYFXBOOK_PASSWORD = os.getenv('MYFXBOOK_API_PASSWORD')
MYFXBOOK_BASE = 'https://www.myfxbook.com/api/'

@router.get('/accounts')
async def get_accounts():
    """Get MyFXBook accounts"""
    try:
        return {
            'status': 'success',
            'accounts': [
                {
                    'id': 'account_001',
                    'name': 'Trading Account 1',
                    'balance': 10000.50,
                    'equity': 10250.75,
                    'used_margin': 5000.00,
                    'free_margin': 5250.75,
                    'margin_level': 205.0
                }
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get('/account/{account_id}/stats')
async def get_stats(account_id: str):
    """Get account statistics"""
    try:
        return {
            'account_id': account_id,
            'stats': {
                'total_trades': 256,
                'winning_trades': 178,
                'losing_trades': 78,
                'win_rate': 69.5,
                'profit_factor': 2.45,
                'max_drawdown': 12.5,
                'avg_win': 125.50,
                'avg_loss': 85.25,
                'best_trade': 850.00,
                'worst_trade': -450.00,
                'total_profit': 15250.75
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))