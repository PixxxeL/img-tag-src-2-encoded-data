# -*- coding: cp1251 -*-
'''
������ ������ ������ �� ������������ �������� ������ �����������
� html-������. ��� �����.

@author: pixel, piksel@mail.ru

�������������:
1. ����� ���������� � ���������� ��� ����� HTML �� �����,
   ��������� ���� �����������, �� ������� � �������.
2. ��������� IS_EXEC � True, ���� ���������� ������
   ��� �������� � False ��� ������.
3. ����� ����������� ������ ���������� ������������
   � ���������� �������-������ � ����������
   � ����� ������� (��� ��������� ���� � ��������).

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
