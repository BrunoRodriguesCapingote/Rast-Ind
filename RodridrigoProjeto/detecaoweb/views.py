from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from django.views.decorators import gzip
import cv2
from detecaoweb.Ras&Ind import Control


def index(request):
    return render(request, 'index.html')


def item_data(request):
    return render(request, 'item_data.html')


def indentificacao(request):
    return StreamingHttpResponse(gen_frames(), content_type="multipart/x-mixed-replace;boundary=frame")


def gen_frames():
    camera = cv2.VideoCapture(0)
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
