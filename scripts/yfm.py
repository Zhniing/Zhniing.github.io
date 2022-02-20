# -*- coding: utf-8 -*-

# Script for YFM(YAML front matter) operation

import os
import frontmatter
import datetime
from typing import Tuple
from glob import glob


# Time zone: UTC+08:00
tz = datetime.timezone(datetime.timedelta(seconds=28800))


def modified_md_files(dirs: Tuple[str, ...] = ['_posts']):
    """读取当前修改了（还未add到暂存区）的post的"mtime"，并写入（覆盖）YFM

    注意: `git ls-files -m`只显示工作区(working tree)的修改文件，不会显示暂存区(index)的修改文件

    Args:
        dirs (Tuple[str, ...], optional): Look up files in these directories. Defaults to ['_posts'].
    """

    with os.popen(cmd='git ls-files -m') as fd_cmd:  # 将命令的输出当作一个文件
        files = fd_cmd.read().splitlines()  # 获取文件名list
        for file in files:  # splitlines() 去掉'\n'
            if not os.path.isfile(file):
                continue  # 跳过已删除的文件
            if not file.endswith('.md'):
                continue  # 仅md文件
            for dir in dirs:
                if file.startswith(dir):
                    yield file
                    break  # 下一个文件


def are_equal_yfm_mtime(file: str, mtime: float) -> bool:
    """检查文件的yfm与mtime是否一致

    Args:
        file (str): File name
        mtime (float): Modification time of the file

    Returns:
        bool: yfm与mtime是否一致
    """

    mtime_dt = datetime.datetime.fromtimestamp(mtime, tz)
    post = frontmatter.load(file)  # 获取md文件的YFM

    if 'last-updated-date' in post.keys():
        # 获取YFM中的更新日期 (lud: last-updated-date)
        yfm_lud = post['last-updated-date']
        if type(yfm_lud) != datetime.datetime and type(yfm_lud) == str:
            yfm_lud = datetime.datetime.fromisoformat(yfm_lud)  # 格式转换：字符串 -> datetime对象

        if mtime_dt == yfm_lud:
            return True  # yfm与mtime一致
        else:
            return False


def update_yfm(file: str, mtime: float) -> bool:
    """更新单个文件的yfm

    Args:
        file (str): File name
        mtime (float): Modification time of the file

    Returns:
        bool: 是否更新了yfm
    """

    mtime_dt = datetime.datetime.fromtimestamp(mtime, tz)
    post = frontmatter.load(file)  # 获取md文件的YFM

    option = input(
        f'[{file}] [YFM] {post.get("last-updated-date")} -> {mtime_dt} ?[Y/n]'
    )
    if option in ['Y', 'y', '']:
        post['last-updated-date'] = mtime_dt  # dt.__str__()返回iso格式的str
        with open(file, 'wb') as fd:
            frontmatter.dump(post, fd)
        print(f'YFM changed')

        os.utime(file, (mtime, mtime))  # 设置文件的mtime，使其与YFM一致
        return True
    else:
        print(f'YFM unchanged')
        return False


def update_yfm_in_dirs(dirs: Tuple[str, ...] = ['_posts']) -> None:
    """更新指定文件夹中，内容变动过 (git) 的文件的yfm

    Args:
        dirs (Tuple[str, ...], optional): Look up files in these directories. Defaults to ['_posts'].
    """

    num_git_modified = 0  # git working tree里面的已修改文件
    num_neq_yfm_mtime = 0  # (ne: Not Equal) YFM和mtime不一致的md文件数量
    num_changed = 0  # 更改了的md文件数量

    for file in modified_md_files(dirs):
        mtime = os.path.getmtime(file)  # 获取文件的修改时间
        num_git_modified += 1
        num_neq_yfm_mtime += are_equal_yfm_mtime(file, mtime)
        num_changed += update_yfm(file, mtime)

    # Summary
    print(f'[git worktree] {num_git_modified}个md文件的内容有变动', end='')
    if num_git_modified > 0:
        print('，其中：')
        print(f'YFM与mtime不一致：{num_neq_yfm_mtime}个')
        print(f'本次调整了{num_changed}个')
    else:
        print()


if __name__ == "__main__":
    func_options = {
        '1': 'All the modified .md files',
        '2': 'Single file',
    }

    dir_options = {
        '1': '_posts',
        '2': '_drafts',
    }

    while True:
        # Print func_options
        for k, v in func_options.items():
            print(f'{k}. {v}')
        print('0. Exit (default)')

        resp_func = input('Choice function (only one): ')
        print()

        # Check the validity of resp_func
        if resp_func in ['0', '']:
            exit()
        if resp_func in func_options.keys():
            break
        else:
            print(f'Invalid input\n')

    while True:
        # Print dir_options
        for k, v in dir_options.items():
            print(f'{k}. {v}')
        print('0. Exit (default)')

        resp_dirs = input('Choice directories: ')
        print()

        # Check the validity of resp_dirs
        if resp_dirs in ['0', '']:
            exit()
        num_valid = 0
        for r in resp_dirs:
            if r in dir_options.keys():
                num_valid += 1
        if num_valid == len(resp_dirs):
            break
        else:
            print(f'Invalid input\n')

    # Solve
    dirs = [dir_options[k] for k in resp_dirs]
    if resp_func == '1':
        update_yfm_in_dirs(dirs)
    elif resp_func == '2':
        files = []
        i = 0
        for dir in dirs:
            pattern = os.path.join(dir, '*')
            files += glob(pattern)

        while True:
            for file in files:
                i += 1
                print(f'{i:2}. {file}')
            print('0. Exit (default)')

            resp_file = input('Choice file (only one): ')
            print()

            if resp_file in ['0', '']:
                exit()
            try:
                resp_file = int(resp_file) - 1
                if resp_file in range(len(files)):
                    break
                else:
                    raise ValueError
            except ValueError:
                print(f'Invalid input\n')
                i = 0

        file = files[resp_file]
        mtime = os.path.getmtime(file)
        update_yfm(file, mtime)
