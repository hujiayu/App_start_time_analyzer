#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import os
import shutil

import cv2

from settings import PROJECT_DIR

logger = logging.getLogger(__name__)


def prase_video(video, dest):
    if not os.path.isdir(PROJECT_DIR + dest):
        os.mkdir(PROJECT_DIR + dest)
    # pre delete images in folder
    shutil.rmtree(PROJECT_DIR + dest)
    os.mkdir(PROJECT_DIR + dest)

    vc = cv2.VideoCapture(video)
    c = 1
    fps = vc.get(cv2.CAP_PROP_FPS)
    logger.info(u"当前帧率:{}".format(fps))

    if vc.isOpened():
        print "opened"
        rval, frame = vc.read()
    else:
        rval = False

    while rval:
        rval, frame = vc.read()
        cv2.imwrite(PROJECT_DIR + dest + '/' + str(c) + '.jpg', frame)
        c = c + 1
        cv2.waitKey(100)
    logger.info(u"总帧数:{}".format(c))
    vc.release()
    return fps


if __name__=='__main__':
    print prase_video("/Users/hujiayu/Desktop/meituan.mp4", '/image/meituan')