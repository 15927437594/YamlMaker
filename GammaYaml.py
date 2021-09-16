# -*- coding: utf-8 -*-
"""
user:Created by jid on 2021/8/31 9:20
email:jid@hwtc.com.cn
description:
"""
import os

import yaml


def create_rgb_config(rgb_config, src_list):
    config = {
        'delay_time': 0.3,
        'brightness': src_list
    }

    with open(rgb_config, 'w', encoding='utf-8') as f:
        yaml.dump(config, f, default_flow_style=False, allow_unicode=True)


if __name__ == '__main__':
    rgb_config = os.path.join(os.getcwd(), 'Gamma.yaml')
    src_list = []
    for rgb in range(256):
        rgb_dict = {}
        rgb_dict.update({'R': rgb})
        rgb_dict.update({'G': rgb})
        rgb_dict.update({'B': rgb})
        src_list.append(rgb_dict)
    src_list.reverse()
    create_rgb_config(rgb_config, src_list)
