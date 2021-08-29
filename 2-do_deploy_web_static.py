#!/usr/bin/python3
''' Fabric script that distributes an archive
to your web servers, using the function do_deploy'''

from os import path
from fabric.api import local, put, env, run
from datetime import datetime

env.hosts = ["34.138.40.16", "35.173.128.216"]
# env.user = 'ubuntu'


def do_pack():
    ''' Create a file .tgz base on folder web_satatic'''
    if not path.exists("./versions"):
        local("mkdir -p versions")

    date = datetime.now()
    time_name = date.strftime("%Y%m%d%H%M%S")
    name = 'versions/web_static_{}.tgz'.format(time_name)
    # compress files
    try:
        local("tar -cvzf {} web_static".format(name))
    except Exception as e:
        return(None)
    # set permisions
    # local('chmod 664 {}'.format(name))
    # get the size
    size = path.getsize(name)
    print('web_static packed: {} -> {}Bytes'.format(name, size))
    return(name)


def do_deploy(archive_path):
    '''function por unpacking files'''
    if not path.exists(archive_path):
        return (False)
    try:
        # set name file
        name_file = archive_path.split('/')[1].split(".")[0]
        put(archive_path, '/tmp/{}.tgz'.format(name_file))
        # create a new folder
        run('mkdir -p /data/web_static/releases/{}/'.format(name_file))
        # uncompress file
        run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/'
            .format(name_file, name_file))
        # delete temp file
        run('rm /tmp/{}.tgz'.format(name_file))
        # move the content from web_static to new folder
        run('mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}/'.format(name_file,
                                                  name_file))
        # delete folder web_static
        run('rm -rf /data/web_static/releases/{}/web_static'.format(name_file))
        # delete simbolic link
        run('rm -rf /data/web_static/current')
        # create a new simbolic link
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(name_file))
    except Exception as e:
        return(False)
