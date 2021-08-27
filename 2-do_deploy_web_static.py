#!/usr/bin/python3
""" This script defines a function do_deploy """
from fabric.api import put, run, env, local
from os.path import isfile
from datetime import datetime


env.hosts = [
    '34.138.131.46',
    '34.228.168.55'
]

env.user = "ubuntu"


def do_pack():
    """ This function generates a .tgz archive from the
        contents of the web_static folder """
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    name = 'web_static_' + date + '.tgz'
    local('mkdir -p versions/')
    descompress = local('tar -zcvf versions/{} web_static'.format(name))
    if descompress.failed:
        return None
    return 'versions/' + name


def do_deploy(archive_path):
    """ This function distributes an archive to your web servers """
    name_file = archive_path.split('/')[1][:-4]
    if not isfile(archive_path):
        return False
    upload = put(archive_path, "/tmp/{}.tgz".format(name_file))
    if upload.failed:
        return False
    create = run('mkdir -p /data/web_static/releases/{}/'.format(name_file))
    if create.failed:
        return False
    descompress = run('tar xzf /tmp/{}.tgz -C /data/\
web_static/releases/{}/'.format(name_file, name_file))
    if descompress.failed:
        return False
    delete = run('rm /tmp/{}.tgz'.format(name_file))
    if delete.failed:
        return False
    move = run('mv /data/web_static/releases/{}/web_static/* \
/data/web_static/releases/{}/'.format(name_file, name_file))
    if move.failed:
        return False
    o_del = run('rm -rf /data/web_static/releases/{}/\
web_static'.format(name_file))
    if o_del.failed:
        return False
    sym_l_del = run('rm -rf /data/web_static/current')
    if sym_l_del.failed:
        return False
    symbolic = run('ln -s {} /data/web_static/current'.format(name_file))
    if symbolic.failed:
        return False
    return True
