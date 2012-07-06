# -*- coding: cp1251 -*-
'''
Скрипт замены ссылок на кодированные значения данных изображений
в html-фалйах. Для Винды.

@author: pixel, piksel@mail.ru

Использование:
1. Нужно подставить в переменные имя файла HTML на диске,
   регулярку урла изображений, их префикс и суффикс.
2. Выставить IS_EXEC в True, если необходима замена
   или оставить в False для тестов.
3. Файлы изображений должны называться единообразно
   с порядковым номером-цифрой и находиться
   в папке скрипта (или выставить путь в префиксе).

'''
import base64, re

HTML_FILENAME = 'test-file.html'
IMG_TAG_URL_REGEXP = r' src="(/img/test-file-(?P<num>\d+).png)"'
IMG_FILES_PREFIX = 'test-file-'
IMG_FILES_SUFFIX = '.png'
IS_EXEC = True
IS_VERBOSE = True

f = open(HTML_FILENAME, 'r+')
html = f.read()

img_re = re.compile(IMG_TAG_URL_REGEXP)

for m, num in img_re.findall(html):
    if IS_VERBOSE: print 'Finded:', m, ' | num =', num
    try:
        img_filename = IMG_FILES_PREFIX + num + IMG_FILES_SUFFIX
        img = open(img_filename, 'rb')
        if IS_VERBOSE: print 'Opened image:', img_filename
        data = base64.b64encode(img.read())
        if IS_VERBOSE: print 'Decoded image:', img_filename
    finally:
        if IS_VERBOSE: print 'Closed image:', img_filename
        img.close()
    if data:
        html = html.replace(m, 'data:image/jpeg;base64,' + data)
        if IS_VERBOSE: print 'HTML-data was replaced...'

f.seek(0)
if IS_EXEC:
    f.write(html)
    if IS_VERBOSE: print 'HTML-data was processed!'

f.close()
