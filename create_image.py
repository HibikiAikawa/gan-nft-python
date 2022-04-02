import cv2
import base64

import torch
import numpy as np

from model import imageNet


def create_image():
    model = imageNet().cuda()

    input = torch.rand(1,1).cuda()    
    output = model(input)
    output = output.reshape(64, 64, 3).cpu().detach().numpy()*255
    # TODO 保存しなくてもいい？
    cv2.imwrite('/work/tmp.png', output)
    with open('/work/tmp.png', "rb") as image_file:
        data = base64.b64encode(image_file.read())
        return data


