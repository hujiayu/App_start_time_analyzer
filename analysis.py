#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

import utils.vedio_util as vedio_handler
import utils.template_match_util as template_match_handler
import utils.similarity_util as similarity_handler


logger = logging.getLogger(__name__)


def process(video, dest, start_template, end_pic):
    """ functions that return the cold start time of app 

        :video : video path 
               e.g.  "/Users/hujiayu/Desktop/WeChatSight15.mp4"

        :dest : folder that video frames saved in 
               e.g. "/image/eleme"
               
        :start_template : picture which marks user begin to start up app
        
        :end_pic : picture which marks app start up done

    """
    logger.info("start to prase vedio")
    fps = vedio_handler.prase_video(video, dest)
    print "帧率为:{}".format(fps)
    logger.info("start to match start loc")
    start = template_match_handler.readfolder(dest, start_template)[0]
    start_index = start.split("/")[-1].split('.')[0]
    print "启动开始帧为:{}".format(start_index)
    logger.info("start to match end loc")
    end = similarity_handler.readfolder(dest, end_pic, 2)
    end_index = end.split('.')[0]
    print "启动结束帧为:{}".format(end_index)
    cold_start_time = (float(end_index) - float(start_index)) / float(fps)
    return cold_start_time


if __name__=='__main__':
    # print process("/Users/hujiayu/Desktop/WeChatSight15.mp4",
    #               '/image/eleme',
    #               "/Users/hujiayu/Desktop/templateIcon.jpg",
    #               '/Users/hujiayu/Desktop/template2.jpeg')

    print process("/Users/hujiayu/Desktop/meituan.mp4",
                  '/image/meituan',
                  "/Users/hujiayu/Desktop/meituanIcon.jpg",
                  '/Users/hujiayu/Desktop/template3.PNG')
