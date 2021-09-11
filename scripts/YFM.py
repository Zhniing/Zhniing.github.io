
# -*- coding: utf-8 -*-
# From: https://www.yixuju.cn/programming/python/change-meta-data/

# Script for YFM(YAML front matter) operation

import os
import chardet
import yaml
import warnings
import frontmatter
import time

def get_files_name(dir='_posts'):
    content = os.walk(dir)
    for path, dir_list, file_list in content:
        for file_name in file_list:
            yield(os.path.join(path, file_name))

def get_charset(dir):
    with open(dir, "rb") as f:
        data = f.read()
    return chardet.detect(data)

def get_meta_data(dir='_posts'):
    for file in get_files_name(dir=dir):
        post = frontmatter.load(file)
        yield file, post.metadata

if __name__ == "__main__":
    for file in get_files_name('_posts'):
        post = frontmatter.load(file)  # 读取front matter

        # some modify...
        with os.popen(cmd=f'git log -1 --format="%ct" "{file}"') as fd:
            time_stamp = fd.read()
            if time_stamp == '': raise ValueError('time_stamp is empty')
            last_committed_date = time.strftime('%Y-%m-%d %H:%M:%S +0800', time.localtime(int(time_stamp)))
            post['last-updated-date'] = last_committed_date

        with open(file, 'wb') as fd:
            frontmatter.dump(post, fd)  # dump到原文件中

        # post.metadata.pop('title')