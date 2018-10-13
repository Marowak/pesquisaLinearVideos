# -*- coding: cp1252 -*-
import numpy as np
import cv2

def main():  
    fileName='video.flv'  # Nome do arquivo a ser lido
    img1 = cv2.imread('frame.jpg') # Imagem a ser comparada
    video = cv2.VideoCapture(fileName)          # Carrega o vídeo

    framesPassados = 0
    diffSalvo = 50000   
    frameDesejado = 0
    totalFrames = 0   
    
    while(video.isOpened()):                    # Continua lendo cada frame enquanto o vídeo está aberto
        ret, frame = video.read()
        if ret:
            cv2.imshow('frame',frame)              # Exibe os frames na tela
            totalFrames +=1
            
            diff = mse(img1,frame)
            
            if ((diff < 3000) and (diff < diffSalvo)):   
                diffSalvo = diff
                frameDesejado = totalFrames
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    tempoTotal = frameDesejado / 25.0
    minutos = str(np.floor(tempoTotal / 60))
    segundos = str(tempoTotal % 60)
    
    print("Minutos: " + minutos + " Segundos: " + segundos)
    
    video.release()
    cv2.destroyAllWindows()

def mse(imagem1,imagem2):
    err = np.sum((imagem1.astype("float") - imagem2.astype("float")) ** 2)
    err /= float(imagem1.shape[0] * imagem2.shape[1])

    return err


main()
