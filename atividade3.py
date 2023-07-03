# Abra e mostre uma imagem na tela. Após isso, aplique as operações de
# mudança de escala, translação e rotação, nesta ordem, e mostre
# novamente a imagem com o resultado;

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem
image = cv2.imread('imagem.jpg')

# Operações de mudança de escala, translação e rotação
scale_factor = 0.5  # Fator de escala
resized_image = cv2.resize(image, None, fx=scale_factor, fy=scale_factor)

translation_matrix = np.float32([[1, 0, 10], [0, 1, 10]])  # Matriz de translação (50 pixels para a direita, 100 pixels para baixo)
translated_image = cv2.warpAffine(resized_image, translation_matrix, (resized_image.shape[1], resized_image.shape[0]))

angle = 45  # Ângulo de rotação (em graus)
rotation_matrix = cv2.getRotationMatrix2D((translated_image.shape[1] // 2, translated_image.shape[0] // 2), angle, 1)
rotated_image = cv2.warpAffine(translated_image, rotation_matrix, (translated_image.shape[1], translated_image.shape[0]))

# Criar a figura e os eixos para exibir as imagens
fig, axs = plt.subplots(1, 2)

# Exibir a imagem original no eixo esquerdo
axs[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axs[0].set_title('Imagem Original')
axs[0].axis('off')

# Exibir a imagem final no eixo direito
axs[1].imshow(cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB))
axs[1].set_title('Imagem Final')
axs[1].axis('off')

# Ajustar a largura da figura para evitar cortes
fig.tight_layout()

# Exibir a figura
plt.show()
