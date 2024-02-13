from bitkub_v3 import bitkub

### สำหรับ Non-secure endpoints
credentials = {
    'apiKey': '',
    'secretKey': ''
}

# GET แบบที่ไม่ต้องการ Body
reqBody = {
}      
print(bitkub('GET', '/api/status', reqBody, credentials))

# GET แบบที่ต้องการ Body
reqBody = {
    'symbol': 'BTC_THB',
    'resolution': '1',
    'from': 1633424427,
    'to' : 1633427427
}      
print(bitkub('GET', '/tradingview/history', reqBody, credentials))


### สำหรับ Secure endpoints ###
credentials = {
    'apiKey': 'xxx',
    'secretKey': 'xxx'
}

# GET แบบ Secure endpoints ที่ต้องการ Body
reqBody = {
    'hash': 'fwQ6dnQYKnqFPYSn2u25cNDfRsN'
}      
print(bitkub('GET', '/api/v3/market/order-info', reqBody, credentials))

# POST แบบที่ไม่ต้องการ Body
reqBody = {
}      
print(bitkub('POST', '/api/v3/user/trading-credits', reqBody, credentials))

# POST แบบที่ต้องการ Body
reqBody = {
    'sym': 'btc_thb',
    'amt': 999,
    'rat': 999999,
    'typ': 'limit'
}      
print(bitkub('POST', '/api/v3/market/place-bid', reqBody, credentials))
