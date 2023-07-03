# Abra e mostre uma imagem na tela e seus histogramas em escala de
# cinza e em RGB. Após isso, aplique uma alteração de brilho
# (aumentando ou diminuindo), e mostre agora a imagem alterada e os
# histogramas em escala de cinza e em RGB para a nova imagem.

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Função para exibir a imagem e os histogramas
def show_image_with_histograms(image, title):
    # Converter a imagem para escala de cinza
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calcular o histograma em escala de cinza
    gray_hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

    # Calcular os histogramas em RGB
    b, g, r = cv2.split(image)
    b_hist = cv2.calcHist([b], [0], None, [256], [0, 256])
    g_hist = cv2.calcHist([g], [0], None, [256], [0, 256])
    r_hist = cv2.calcHist([r], [0], None, [256], [0, 256])

    # Criar a figura e os eixos para exibir a imagem e os histogramas
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))

    # Exibir a imagem
    axs[0, 0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    axs[0, 0].set_title('Imagem')
    axs[0, 0].axis('off')

    # Exibir o histograma em escala de cinza
    axs[0, 1].plot(gray_hist, color='black')
    axs[0, 1].set_title('Histograma (Escala de Cinza)')
    axs[0, 1].set_xlim([0, 256])
    axs[0, 1].set_xlabel('Intensidade')
    axs[0, 1].set_ylabel('Frequência')

    # Exibir os histogramas em RGB
    axs[1, 0].plot(r_hist, color='red')
    axs[1, 0].set_title('Histograma (Red)')
    axs[1, 0].set_xlim([0, 256])
    axs[1, 0].set_xlabel('Intensidade')
    axs[1, 0].set_ylabel('Frequência')

    axs[1, 1].plot(g_hist, color='green')
    axs[1, 1].set_title('Histograma (Green)')
    axs[1, 1].set_xlim([0, 256])
    axs[1, 1].set_xlabel('Intensidade')
    axs[1, 1].set_ylabel('Frequência')

    fig.tight_layout()

    # Exibir a figura
    plt.suptitle(title)
    plt.show()

# Carregar a imagem
image = cv2.imread('imagem.jpg')

# Exibir a imagem original e seus histogramas
show_image_with_histograms(image, 'Imagem Original')

# Aplicar uma alteração de brilho
brightness_change = 50  # Alteração de brilho (aumentar ou diminuir)
image_changed = cv2.convertScaleAbs(image, alpha=1, beta=brightness_change)

# Exibir a imagem alterada e os histogramas atualizados
show_image_with_histograms(image_changed, 'Imagem Alterada')
