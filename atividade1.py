# Faça um identificador de rosto humano que consiga identificar seu rosto diretamente da câmera do seu computador

import cv2

# Carregar o classificador de rosto pré-treinado
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Inicializar a captura de vídeo
video_capture = cv2.VideoCapture(0)

while True:
    # Ler o quadro atual da câmera
    ret, frame = video_capture.read()

    # Converter para escala de cinza para a detecção do rosto
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar os rostos na imagem
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Desenhar retângulos ao redor dos rostos detectados
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Mostrar o quadro resultante com as detecções de rosto
    cv2.imshow('Face Detection', frame)

    # Sair do loop quando a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar os recursos
video_capture.release()
cv2.destroyAllWindows()
