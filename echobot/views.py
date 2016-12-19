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
        a = 60
        b = "123"
        try:
            url_str = 'http://opendata.cwb.gov.tw/opendataapi?dataid=F-C0032-001&authorizationkey=CWB-9C36ED08-5B28-4D07-8B91-2664777A075D'
            xml_str = urlopen(url_str).read()
            xmldoc = minidom.parseString(xml_str)
            obs_values2 = xmldoc.getElementsByTagName('parameterName')
            b = "456"
        except:
            pass
        for event in events:
            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage):
                    if "天氣" in event.message.text:
                        if "臺北" in event.message.text or "台北" in event.message.text:
                            a = 0
                        elif "新北" in event.message.text:
                            a = 15
                        elif "桃園" in event.message.text:
                            a = 30
                        elif "台中" in event.message.text or "臺中" in event.message.text:
                            a = 45
                        elif "台南" in event.message.text or "臺南" in event.message.text:
                            a = 60
                        elif "高雄" in event.message.text:
                            a = 75
                        elif "基隆" in event.message.text:
                            a = 90
                        elif "新竹縣" in event.message.text:
                            a = 105
                        elif "新竹市" in event.message.text:
                            a = 120
                        elif "苗栗" in event.message.text:
                            a = 135
                        elif "彰化" in event.message.text:
                            a = 150
                        elif "南投" in event.message.text:
                            a = 165
                        elif "雲林" in event.message.text:
                            a = 180
                        elif "嘉義縣" in event.message.text:
                            a = 195
                        elif "嘉義市" in event.message.text:
                            a = 210
                        elif "屏東" in event.message.text:
                            a = 225
                        elif "宜蘭" in event.message.text:
                            a = 240
                        elif "花蓮" in event.message.text:
                            a = 255
                        elif "台東" in event.message.text or "臺東" in event.message.text:
                            a = 270
                        elif "澎湖" in event.message.text:
                            a = 285
                        elif "金門" in event.message.text:
                            a = 300
                        elif "連江" in event.message.text or "馬祖" in event.message.text:
                            a = 315
                        b = obs_values2[a].firstChild.nodeValue

                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=b)#event.message.text)
                    )

        return HttpResponse()
    else:
        return HttpResponseBadRequest()
