import json, hmac, requests, hashlib

def bitkub(reqType, reqPath, reqBody, reqCredentials):
    def gen_sign(api_secret, payload_string=None):
        return hmac.new(api_secret.encode('utf-8'), payload_string.encode('utf-8'), hashlib.sha256).hexdigest()
    host = 'https://api.bitkub.com'
    ts = requests.get(host + '/api/v3/servertime').text
    url = host + reqPath
    payload = []
    payload.append(ts)
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'X-BTK-TIMESTAMP': ts,
        'X-BTK-APIKEY': reqCredentials['apiKey']
    }
    if reqType == 'GET':
        def gen_query_param(url, query_param):
            req = requests.PreparedRequest()
            req.prepare_url(url, query_param)
            return req.url.replace(url, '')
        query_param = gen_query_param(host+reqPath, reqBody)
        payload.append('GET')
        payload.append(reqPath)
        payload.append(query_param)
        sig = gen_sign(reqCredentials['secretKey'], ''.join(payload))
        headers['X-BTK-SIGN'] = sig
        response = requests.request('GET', f'{host}{reqPath}{query_param}', headers=headers, data={}, verify=True)
        return response.json()
    if reqType == 'POST':
        payload.append('POST')
        payload.append(reqPath)
        payload.append(json.dumps(reqBody))
        sig = gen_sign(reqCredentials['secretKey'], ''.join(payload))
        headers['X-BTK-SIGN'] = sig
        response = requests.request('POST', url, headers=headers, data=json.dumps(reqBody), verify=True)
        return response.json()
