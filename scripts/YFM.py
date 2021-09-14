
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


def timestamp_to_iso(time_stamp):
    time_struct_local = time.localtime(int(time_stamp))
    time_iso = time.strftime('%Y-%m-%d %H:%M:%S +0800', time_struct_local)
    return time_iso


def update_mtime_from_commit(dir='_posts'):
    """ 读取所有post的最后提交日期，并写入（覆盖）YFM """

    for file in get_files_name(dir):
        post = frontmatter.load(file)  # 读取front matter

        # some modify...
        with os.popen(cmd=f'git log -1 --format="%ct" "{file}"') as fd:
            time_stamp = fd.read()
            if time_stamp == '': raise ValueError('time_stamp is empty')
            last_committed_date = timestamp_to_iso(time_stamp)
            post['last-updated-date'] = last_committed_date

        with open(file, 'wb') as fd:
            frontmatter.dump(post, fd)  # dump到原文件中


if __name__ == "__main__":

    # 读取当前修改了（还未add到暂存区）的post的"mtime"，并写入（覆盖）YFM
    with os.popen(cmd='git ls-files -m') as fd:
        for file in fd.read().splitlines():  # splitlines() 去掉'\n'
            if not file.endswith('.md'): continue
            mtime = os.path.getmtime(file)
            last_committed_date = timestamp_to_iso(mtime)
            post = frontmatter.load(file)
            post['last-updated-date'] = last_committed_date

            option = input(f'是否修改{file}的mtime？[Y/n]')
            if option in ['Y', 'y', '']:
                with open(file, 'wb') as fd_file:
                    frontmatter.dump(post, fd_file)
                print(f'已更改{file}')
            else:
                print(f'没有改动{file}')

        # post.metadata.pop('title')