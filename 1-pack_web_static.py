#!/usr/bin/python3
'''Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo'''

from os import path
from fabric.api import local
from datetime import datetime


def do_pack():
    ''' Create a file .tgz base on web_satatic'''
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
