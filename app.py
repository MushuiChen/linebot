# -*- coding: utf-8 -*-

#載入LineBot所需要的套件
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import re
import random
app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('wvdgugGq+zaBg3f3hJL+Tsjg/TxkBxYnrfm0w/cEXS7LEUK0uNH+eeNwOx8mC55udDDDBp6Iy+6PA3CUILWH4D6O8DhmMDe/cdio/MSvcBp6Iy+6PA3CUILWH4D6O8DhmMDe/cC/MSvcBp6Iy+6PA3CUILWH4D6O8DhmMDe/cC/MSvcBp6Iy+LnnvL0FFFyg700FpFm/MS B04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('97a38974ee2dad9c5f575f82ce28a7c0')

line_bot_api.push_message('U759b49ce9ec6234e18cf8d43c19cb7ea', TextSendMessage(text='您好,目前時間是 2024/10/10 14:00 ，請問需要什麼服務呢?'))

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = text=event.message.text
    if message == '天氣':
            reply_text = '請稍等，我幫您查詢天氣資訊！'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(reply_text))

    elif message == '心情好':
            sticker_message = StickerSendMessage(
            package_id='8515',
            sticker_id='16581242'  # 開心的貼圖
        )
            line_bot_api.reply_message(event.reply_token, sticker_message)

    elif message == '心情不好':
            sticker_message = StickerSendMessage(
            package_id='8515',
            sticker_id='16581262'  # 傷心的貼圖
        )
            line_bot_api.reply_message(event.reply_token, sticker_message)

    elif message == '找美食':
            location_message = LocationSendMessage(
            title='吃光食堂',
            address='公民里 台中市西區',
            latitude=24.142004059652407,
            longitude=120.6708091028049
        )
            line_bot_api.reply_message(event.reply_token, location_message)

    elif message == '找景點':
            location_message = LocationSendMessage(
             title='湖心亭（市定古蹟）',
            address='新興里 台中市北區',
            latitude=24.144433941595807,
            longitude=120.68420319880194  
        )
            line_bot_api.reply_message(event.reply_token, location_message)

    elif message == '熱門音樂':
            audio_message = AudioSendMessage(
            original_content_url='https://www.youtube.com/watch?v=Vk5-c_v4gMU&list=RDCLAK5uy_kWmaONW-ni4bGVHI-DnXi2wEv9fICbgEc&index=4',
            duration=188000
        )
            line_bot_api.reply_message(event.reply_token, audio_message)

    elif message == '放鬆音樂':
            audio_message = AudioSendMessage(
            original_content_url='https://www.youtube.com/watch?v=MZ8Ri-_Uusk&list=PLE31UdyigZQ9ZQ3cIbMvffJrkZU_Zab57&index=3',
            duration=942000
        )
            line_bot_api.reply_message(event.reply_token, audio_message)

    elif message == '今天是我的生日':
            image_message = ImageSendMessage(
            original_content_url='https://drive.google.com/file/d/1gvVZB4XsSYK8pgAZhu9_hWzARZVbvn8B/view?usp=sharing',
        )
            text_message = TextSendMessage(text='祝你事事順利，生日快樂')
            line_bot_api.reply_message(event.reply_token, [image_message, text_message])

    elif message in ['動畫']:
        video_urls = {
            '動畫': 'https://www.youtube.com/watch?v=1-hNreqVpfA',    
        }
        video_url = video_urls.get(message)
        if video_url:
            reply_text = f'這是您要的{message}：\n{video_url}'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(reply_text))
        else:
            reply_text = '抱歉，沒有這類型的影片'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(reply_text))

    elif message in ['科幻']:
            reply_text = '抱歉，沒有這類型的影片'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(reply_text))

    else:
            reply_text = '很抱歉，我目前無法理解這個內容。'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(reply_text))
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)