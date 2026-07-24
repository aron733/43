# Trading Platform 43 - API Documentation

## Base URL
```
http://localhost:5000/api
```

## Authentication
All endpoints (except /health) require JWT token:
```
Authorization: Bearer <token>
```

## Endpoints

### Trading

#### GET /trading/positions
Get all open positions
```bash
curl -X GET http://localhost:5000/api/trading/positions
```

#### GET /trading/trades
List all active trades

#### POST /trading/order
Create new order
```json
{
  "instrument": "EUR_USD",
  "units": 10000,
  "side": "BUY"
}
```

### Market Data

#### GET /market/quote/{symbol}
Get real-time quote

#### GET /market/intraday/{symbol}
Get intraday data

### Sentiment

#### GET /sentiment/market
Get market sentiment

#### GET /sentiment/crypto
Get crypto sentiment

### MyFXBook

#### GET /myfxbook/accounts
Get MyFXBook accounts

#### GET /myfxbook/account/{id}/stats
Get account statistics

## WebSocket

### Connection
```javascript
const socket = io('http://localhost:5000');

socket.on('market_update', (data) => {
  console.log('Market update:', data);
});
```

## Error Responses

All errors return:
```json
{
  "detail": "Error message"
}
```

Status codes:
- 200: Success
- 400: Bad Request
- 401: Unauthorized
- 404: Not Found
- 500: Server Error
