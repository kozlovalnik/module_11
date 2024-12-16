import requests

# Открываем запрос и определяем кодировку страницы
r = requests.get('https://api.github.com/events')
print(r.encoding)

import pandas as pd
import numpy as np

# Сформируем серию из 1000 случайных чисел и выведем первые 7 и последние 6
long_series = pd.Series(np.random.randn(1000))
print(long_series.head(7))
print(long_series.tail(6))

import matplotlib.pyplot as plt

# Нарисуем простой график
fig, ax = plt.subplots()
ax.plot([1,2,3,4],[2,4,1,3])
plt.show()

from PIL import Image

# Берем изображение BMP, поворачиваем его на 90 градусов и сохраняем в формате JPEG
with Image.open('IMG.bmp') as im:
    out = im.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    out.save('IMG1.jpg',"JPEG")
