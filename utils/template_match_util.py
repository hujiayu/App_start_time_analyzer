# coding=utf-8
import os

import cv2
import numpy as np

from settings import PROJECT_DIR


def template_matching(image, template):
    try:
        result = cv2.matchTemplate(cv2.imread(image), cv2.imread(template), cv2.TM_CCOEFF_NORMED)
    except Exception as e:
        print "{} cannot load".format(image)
        return None, None
    threshold = 0.9
    locations = np.where(result >= threshold)

    average_x = 0
    average_y = 0
    matches_found = zip(*locations[::-1])
    for pt in matches_found:
        average_x += pt[0]
        average_y += pt[1]

    if len(matches_found):
        average_x /= len(matches_found)
        average_y /= len(matches_found)
        print locations
        return average_x, average_y

    return None, None


def readfolder(folder, pic):
    t = 0
    matched_pics = []
    for root, directors, files in os.walk(PROJECT_DIR + folder):
        for filename in files:
            filepath = os.path.join(root, filename)
            if filepath.endswith(".png") or filepath.endswith(".jpg"):
                x, y = template_matching(filepath, pic)
                if x is None or y is None:
                    continue
                # print x, y
                matched_pics.append(filepath)

    return matched_pics


if __name__ == '__main__':
    print readfolder("/image", "/Users/hujiayu/Desktop/templateIcon.jpg")
