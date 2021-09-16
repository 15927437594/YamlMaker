# -*- coding: utf-8 -*-
"""
user:Created by jid on 2021/8/31 9:20
email:jid@hwtc.com.cn
description:
"""
import os

import yaml


def create_rgb_config(rgb_config, src_list, gray_level):
    config = {
        'delay_time': 0.3,
        'brightness': src_list,
        'calibrate_x': 0.290,
        'calibrate_y': 0.315,
        'calibrate_lv': 800,
        'gray_level': gray_level
    }

    with open(rgb_config, 'w', encoding='utf-8') as f:
        yaml.dump(config, f, default_flow_style=False, allow_unicode=True)


if __name__ == '__main__':
    rgb_config = os.path.join(os.getcwd(), 'ACSCN02_WB.yaml')
    rgb_list = [[0, 0, 255], [0, 255, 0], [255, 0, 0], [255, 255, 255], [254, 254, 254], [248, 248, 248],
                [240, 240, 240], [233, 233, 233],
                [225, 225, 225], [218, 218, 218], [210, 210, 210], [203, 203, 203], [195, 195, 195], [188, 188, 188],
                [180, 180, 180], [173, 173, 173], [165, 165, 165], [158, 158, 158], [150, 150, 150], [143, 143, 143],
                [135, 135, 135], [128, 128, 128], [120, 120, 120], [113, 113, 113], [105, 105, 105], [98, 98, 98],
                [90, 90, 90], [83, 83, 83], [75, 75, 75], [68, 68, 68], [60, 60, 60], [53, 53, 53], [45, 45, 45],
                [38, 38, 38], [30, 30, 30], [23, 23, 23], [15, 15, 15], [8, 8, 8], [0, 0, 0]]
    gray_level = [1023, 1017, 993, 963, 933, 903, 873, 843, 813, 783, 753, 723, 693, 663, 633, 603, 573, 543, 513, 483, 453,
             423, 393, 363, 333, 303, 273, 243, 213, 183, 153, 123, 93, 63, 33, 0]

    src_list = []
    for rgb in rgb_list:
        rgb_dict = {}
        rgb_dict.update({'R': rgb[0]})
        rgb_dict.update({'G': rgb[1]})
        rgb_dict.update({'B': rgb[2]})
        src_list.append(rgb_dict)
    create_rgb_config(rgb_config, src_list, gray_level)
