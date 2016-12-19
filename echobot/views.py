from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from xml.dom import minidom
import urllib
from urllib.request import urlopen
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
        count = 60  #此宣告並處初始化，將各參數初始為"臺南市"的參數
        reply = ""
        city = "臺南市"
        try:
            url_str = 'http://opendata.cwb.gov.tw/opendataapi?dataid=F-C0032-001&authorizationkey=CWB-9C36ED08-5B28-4D07-8B91-2664777A075D'
            xml_str = urlopen(url_str).read()  #讀出
            xmldocity = minidom.parseString(xml_str)
            w_values = xmldoc.getElementsByTagName('parameterName')
        except:
            pass
        for event in events:
            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage):
                    if "天氣" in event.message.text:
                        if "臺北" in event.message.text or "台北" in event.message.text:
                            count = 0
                            city = "臺北市"
                        elif "新北" in event.message.text:
                            count = 15
                            city = "新北市"
                        elif "桃園" in event.message.text:
                            count = 30
                            city = "桃園市"
                        elif "台中" in event.message.text or "臺中" in event.message.text:
                            count = 45
                            city = "臺中市"
                        elif "台南" in event.message.text or "臺南" in event.message.text:
                            count = 60
                            city = "臺南市"
                        elif "高雄" in event.message.text:
                            count = 75
                            city = "高雄市"
                        elif "基隆" in event.message.text:
                            count = 90
                            city = "基隆市"
                        elif "新竹縣" in event.message.text:
                            count = 105
                            city = "新竹縣"
                        elif "新竹市" in event.message.text:
                            count = 120
                            city = "新竹市市"
                        elif "苗栗" in event.message.text:
                            count = 135
                            city = "苗栗縣"
                        elif "彰化" in event.message.text:
                            count = 150
                            city = "彰化縣"
                        elif "南投" in event.message.text:
                            count = 165
                            city = "南投縣"
                        elif "雲林" in event.message.text:
                            count = 180
                            city = "雲林縣"
                        elif "嘉義縣" in event.message.text:
                            count = 195
                            city = "嘉義縣"
                        elif "嘉義市" in event.message.text:
                            count = 210
                            city = "嘉義市"
                        elif "屏東" in event.message.text:
                            count = 225
                            city = "屏東縣"
                        elif "宜蘭" in event.message.text:
                            count = 240
                            city = "宜蘭縣"
                        elif "花蓮" in event.message.text:
                            count = 255
                            city = "花蓮縣"
                        elif "台東" in event.message.text or "臺東" in event.message.text:
                            count = 270
                            city = "臺東縣"
                        elif "澎湖" in event.message.text:
                            count = 285
                            city = "澎湖縣"
                        elif "金門" in event.message.text:
                            count = 300
                            city = "金門縣"
                        elif "連江" in event.message.text or "馬祖" in event.message.text:
                            count = 315
                            city = "連江縣"
                        reply = city + "的天氣是" + w_values[count].firstChild.nodeValue
                    else:
                        reply = event.message.text
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=reply)#event.message.text)
                    )

        return HttpResponse()
    else:
        return HttpResponseBadRequest()
