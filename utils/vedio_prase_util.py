#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import shutil

import cv2

shutil.rmtree('/Users/hujiayu/github/ocr/image')
os.mkdir('/Users/hujiayu/github/ocr/image')

videoUrl = "/Users/hujiayu/Desktop/WeChatSight15.mp4"
vc = cv2.VideoCapture(videoUrl)
c = 1

print "当前帧率:{}".format(vc.get(cv2.CAP_PROP_FPS))

if vc.isOpened():
    print "opened"
    rval, frame = vc.read()
else:
    rval = False

timeF = 100

while rval:
    rval, frame = vc.read()
    cv2.imwrite('/Users/hujiayu/github/ocr/image/' + str(c) + '.jpg', frame)
    c = c + 1
    cv2.waitKey(1)
print "total count:{}".format(c)
vc.release()