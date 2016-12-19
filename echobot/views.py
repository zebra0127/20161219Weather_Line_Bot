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
        a = "123"
        try:
            url_str = 'http://opendata.cwb.gov.tw/opendataapi?dataid=F-C0032-001&authorizationkey=CWB-9C36ED08-5B28-4D07-8B91-2664777A075D'
            xml_str = urlopen(url_str).read()
            a = "456"
            xmldoc = minidom.parseString(xml_str)
            a = "789"
            obs_values1 = xmldoc.getElementsByTagName('locationName')
            a = "012"
            obs_values2 = xmldoc.getElementsByTagName('parameterName')
            a = obs_values2[0].firstChild.nodeValue
        except:
            pass
        for event in events:
            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage):
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=a)#event.message.text)
                    )

        return HttpResponse()
    else:
        return HttpResponseBadRequest()
