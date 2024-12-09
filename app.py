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
line_bot_api = LineBotApi('7EgMow7uxowokDODkkKPAlCpBTHDiEonMBF3aRWVvDyWUe327qvsC9wiIJQpV7+zcrhQ5yVDxNNLy9gdDjNbDD+ZKudiHBVn0GXJfe0ic8jkLKVxCFW2/RHPVIjhlBWaSckrCxYafTe0rnBzl1p0fQdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('4c3e800f2b2dd2c49b87326fc94a5357')

line_bot_api.push_message('Ud18701c20f39da291eeaba864d796ead', TextSendMessage(text='您好,目前時間是 2024/10/10 14:00 ，請問需要什麼服務呢?'))

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
            package_id='446',
            sticker_id='1991'  # 開心的貼圖
        )
            line_bot_api.reply_message(event.reply_token, sticker_message)

    elif message == '心情不好':
            sticker_message = StickerSendMessage(
            package_id='11539',
            sticker_id='52114138'  # 傷心的貼圖
        )
            line_bot_api.reply_message(event.reply_token, sticker_message)

    elif message == '找美食':
            location_message = LocationSendMessage(
            title='著名餐廳',
            address='Hog Island Oyster Co.',
            latitude=37.79726181895184,
            longitude=-122.39362601431256
        )
            line_bot_api.reply_message(event.reply_token, location_message)

    elif message == '找景點':
            location_message = LocationSendMessage(
            title='熱門景點',
            address='Skarðsáfossur',
            latitude=62.09834026797917,
            longitude=-7.406501774391917
        )
            line_bot_api.reply_message(event.reply_token, location_message)

    elif message == '熱門音樂':
            audio_message = AudioSendMessage(
            original_content_url='https://youtu.be/sJ-2X3rHtXw?si=Ow7QJEA94g_oSzjo',  # 替換為實際的音樂檔案網址
            duration=240000  # 音樂長度（毫秒）
        )
            line_bot_api.reply_message(event.reply_token, audio_message)

    elif message == '放鬆音樂':
            audio_message = AudioSendMessage(
            original_content_url='https://youtu.be/b5d5OmmUlPc?si=KjqoCFqC-zMPUbBU',  # 替換為實際的音樂檔案網址
            duration=300000  # 音樂長度（毫秒）
        )
            line_bot_api.reply_message(event.reply_token, audio_message)

    elif message == '今天是我的生日':
            image_message = ImageSendMessage(
            original_content_url='https://instagram.frmq1-1.fna.fbcdn.net/v/t51.29350-15/445982392_1168493424581932_2823979820016375869_n.jpg?stp=dst-jpg_e35_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi44MDB4NTk5LnNkci5mMjkzNTAuZGVmYXVsdF9pbWFnZSJ9&_nc_ht=instagram.frmq1-1.fna.fbcdn.net&_nc_cat=104&_nc_ohc=sB_C31Fv8iEQ7kNvgHhyc2m&_nc_gid=e634efac047d43908457cd99e591ae05&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=MzM3MzY4MDM2NzUyMDk1MzkwMw%3D%3D.3-ccb7-5&oh=00_AYBT_hpWmBXVyHjuu3wIyJ9sU2H78qC0k1msekBCMXYG0w&oe=675A9D7C&_nc_sid=10d13b',  # 替換為實際的圖片網址
            preview_image_url='https://instagram.frmq1-1.fna.fbcdn.net/v/t51.29350-15/445982392_1168493424581932_2823979820016375869_n.jpg?stp=dst-jpg_e35_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi44MDB4NTk5LnNkci5mMjkzNTAuZGVmYXVsdF9pbWFnZSJ9&_nc_ht=instagram.frmq1-1.fna.fbcdn.net&_nc_cat=104&_nc_ohc=sB_C31Fv8iEQ7kNvgHhyc2m&_nc_gid=e634efac047d43908457cd99e591ae05&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=MzM3MzY4MDM2NzUyMDk1MzkwMw%3D%3D.3-ccb7-5&oh=00_AYBT_hpWmBXVyHjuu3wIyJ9sU2H78qC0k1msekBCMXYG0w&oe=675A9D7C&_nc_sid=10d13b'  # 替換為實際的預覽圖片網址
        )
            text_message = TextSendMessage(text='生日快樂！')
            line_bot_api.reply_message(event.reply_token, [image_message, text_message])

    elif message in ['動作片', '動畫', '紀錄片']:
        # 根據類型傳送影片
        video_urls = {
            '動作片': 'https://youtu.be/6PP7QzMowp4?si=JsEKHmvDJugizqzH',
            '動畫': 'https://youtu.be/tfHhtCSGzn0?si=vjxdRSGM8ewilx0_',
            '紀錄片': 'https://youtu.be/vmnuj5SoG-o?si=9uGkb1E_ZPb0Fxre'
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
