# -*- coding: cp1252 -*-
import numpy as np
import cv2

fileName='video.flv'  # Nome do arquivo a ser lido

cap = cv2.VideoCapture(fileName)          # Carrega o vídeo 
while(cap.isOpened()):                    # Continua lendo cada frame enquanto o vídeo está aberto
    ret, frame = cap.read()
    if ret==True:
    
        cv2.imshow('frame',frame)              # Exibe os frames na tela
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
