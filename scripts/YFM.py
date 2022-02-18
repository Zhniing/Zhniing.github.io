# -*- coding: utf-8 -*-

# Script for YFM(YAML front matter) operation

import os
import frontmatter
import time
import datetime


tz = datetime.timezone(datetime.timedelta(seconds=28800))  # UTC+08:00


def get_files_name(dir='_posts'):
    content = os.walk(dir)
    for path, dir_list, file_list in content:
        for file_name in file_list:
            yield(os.path.join(path, file_name))


def timestamp_to_iso(time_stamp):
    """ Example: 2021-09-01T20:27:53+08:00 """

    time_struct_local = time.localtime(int(time_stamp))
    time_iso = time.strftime('%Y-%m-%dT%H:%M:%S+08:00', time_struct_local)

    return time_iso


def iso_to_timestamp(time_iso):
    """ Example: 2021-09-01T20:27:53+08:00 """

    dt = datetime.datetime.strptime(time_iso, "%Y-%m-%dT%H:%M:%S%z")
    timestamp = dt.timestamp()

    return timestamp


def update_yfm_from_commit(dir='_posts'):
    """ 读取所有post的最后提交日期，并写入（覆盖）YFM """

    for file in get_files_name(dir):
        post = frontmatter.load(file)  # 读取front matter

        # some modify...
        with os.popen(cmd=f'git log -1 --format="%ct" "{file}"') as fd:
            time_stamp = fd.read()
            if time_stamp == '':
                print(f'[Warning] time stamp is empty: {file}')
                continue
            last_committed_date = timestamp_to_iso(time_stamp)
            post['last-updated-date'] = last_committed_date

        with open(file, 'wb') as fd:
            frontmatter.dump(post, fd)  # dump到原文件中


def update_mtime_from_yfm(dir='_posts'):
    """ 读取所有post的YFM，并更新文件的mtime """

    for file in get_files_name(dir):
        post = frontmatter.load(file)
        if 'last-updated-date' in post.keys():
            yfm_lud = post['last-updated-date']
            if type(yfm_lud) == str:
                yfm_lud = datetime.datetime.fromisoformat(yfm_lud)
            if type(yfm_lud) != datetime.datetime:
                raise ValueError("[Error] Invalid last-updated-date format")
            yfm_ts = yfm_lud.timestamp()
            os.utime(file, (yfm_ts, yfm_ts))  # 更新mtime
            print(f'已更新mtime: {file}')


if __name__ == "__main__":
    """
    读取当前修改了（还未add到暂存区）的post的"mtime"，并写入（覆盖）YFM
    注意: `git ls-files -m`只显示工作区(working tree)的修改文件，不会显示暂存区(index)的修改文件
    """

    num_git_modified = 0  # git working tree里面的已修改文件
    num_ne_yfm_mtime = 0  # (ne: Not Equal) YFM和mtime不一致的md文件数量
    num_changed = 0  # 更改了的md文件数量

    with os.popen(cmd='git ls-files -m') as fd_cmd:  # 将命令的输出当作一个文件
        file_list = fd_cmd.read().splitlines()  # 获取文件名list
        for file in file_list:  # splitlines() 去掉'\n'
            if not os.path.isfile(file): continue  # 跳过已删除的文件
            if not file.endswith('.md'): continue  # 只处理md文件
            if not file.startswith('_posts/'): continue  # 只处理_posts文件夹中的文件
            num_git_modified += 1
            mtime = os.path.getmtime(file)  # 获取文件的修改时间
            # mtime_iso = timestamp_to_iso(mtime)
            mtime_dt = datetime.datetime.fromtimestamp(mtime, tz)
            post = frontmatter.load(file)  # 获取md文件的YFM

            if 'last-updated-date' in post.keys():
                yfm_lud = post['last-updated-date']  # 获取YFM中的更新日期 (lud: last-updated-date)
                if type(yfm_lud) != datetime.datetime and type(yfm_lud) == str:
                    yfm_lud = datetime.datetime.fromisoformat(yfm_lud)  # 格式转换：字符串 -> datetime对象

                if mtime_dt == yfm_lud: continue  # yfm与mtime一致就不做处理

            num_ne_yfm_mtime += 1

            post['last-updated-date'] = mtime_dt  # dt.__str__()返回iso格式的str

            option = input(f'[{file}] [YFM] {yfm_lud} -> {mtime_dt} ?[Y/n]')
            if option in ['Y', 'y', '']:
                with open(file, 'wb') as fd:
                    frontmatter.dump(post, fd)
                print(f'YFM changed')

                os.utime(file, (mtime, mtime))  # 设置文件的mtime，使其与YFM一致
                num_changed += 1
            else:
                print(f'YFM unchanged')
                # if yfm_lud:
                    # yfm_lud = iso_to_timestamp(yfm_lud)
                    # os.utime(file, (yfm_lud, yfm_lud))

        # Summary
        print(f'[git worktree] {num_git_modified}个md文件的内容有变动，其中：')
        if num_git_modified > 0:
            print(f'YFM与mtime不一致：{num_ne_yfm_mtime}个')
            print(f'本次调整了{num_changed}个')
