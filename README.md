# Bitkub Middleman

**Python module อำนวยความสะดวกในการเชื่อมต่อกับ Bitkub ผ่าน RESTful API V3**
https://github.com/bitkub/bitkub-official-api-docs/blob/master/restful-api.md

clone :

    git clone https://github.com/tidLord/bitkub-Middleman.git

ติดตั้ง requirements :

    pip install -r requirements.txt

## การใช้งาน

    from bitkub_v3 import bitkub

เรียกใช้ผ่านฟังก์ชั่น bitkub() โดยตัวฟังก์ชั่นจะ require
 - request type ("POST" และ "GET")
 - request path ([ตาม official doc ของ Bitkub](https://github.com/bitkub/bitkub-official-api-docs/blob/master/restful-api.md))
 - request body ([ตาม official doc ของ Bitkub](https://github.com/bitkub/bitkub-official-api-docs/blob/master/restful-api.md))
 - credentials ( api key และ secret key )
 
 นี่คือตัวอย่างการใช้งาน สำหรับ Secure endpoints

    credentials = {
        'apiKey': 'xxx',
        'secretKey': 'xxx'
    }
    reqBody = {
        'sym': 'btc_thb',
        'amt': 999,
        'rat': 999999,
        'typ': 'limit'
    }      
    bitkub("POST", '/api/v3/market/place-bid', reqBody, credentials)

หากกรณีที่ไม่ได้ต้องการจะใช้ Secure endpoints หรือต้องการ request path ที่ Bitkub ไม่ได้ต้องการ Body ก็แค่เว้นว่างไว้ เช่น

    credentials = {
        'apiKey': '',
        'secretKey': ''
    }
    reqBody = {
    }      
    bitkub("GET", '/api/status', reqBody, credentials)

โดยฟังก์ชั่นจะ return ข้อมูลจาก exchange กลับมาเป็น json ที่เราสามารถนำไปใช้งานได้เลยตามอัธยาศัย
   
   ## 
<a href="https://www.buymeacoffee.com/tar888" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
