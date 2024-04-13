from django.shortcuts import render,redirect
from django.http import HttpResponse, StreamingHttpResponse
from django.views.decorators import gzip
import cv2
from Rast_Ind import Control


def index(request):
    return render(request, 'index.html')


def item_data(request):
    return render(request, 'item_data.html')


def indentificacao(request):
    return StreamingHttpResponse(capturador_de_frames(), content_type="multipart/x-mixed-replace;boundary=frame")


def capturador_de_frames():
    data_pack: list = list()
    camera = cv2.VideoCapture(0)
    while True:
        success, frame = camera.read()
        if not success:
            break
        elif data_pack.__len__() <= 13:
            rast_ind_control = Control()
            rast_ind_control.ativar_rastreamento(operacao=1)
            rast_ind_control.set_image_pack(image_pack=data_pack)
            rast_ind_control.iniciar_operacao()
            return redirect('item_data')

        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            data_pack.append(frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
