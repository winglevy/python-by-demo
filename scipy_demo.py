import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

# 生成一个简单的二维图像
image = np.zeros((100, 100))
image[20:80, 20:80] = 1

# 对图像进行高斯滤波
filtered_image = ndimage.gaussian_filter(image, sigma=5)

# 显示原始图像和滤波后的图像
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.subplot(1, 2, 2)
plt.imshow(filtered_image, cmap='gray')
plt.title('Filtered Image')
plt.show()