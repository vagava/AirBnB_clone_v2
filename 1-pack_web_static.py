#!/usr/bin/python3


"""do_pack()"""


def do_pack():
    """Fabric script that generates a .tgz archive from the contents
    of the web_static folder
    """

    import tarfile
    import os.path
    from datetime import datetime
    from fabric.api import local

    folder_to_save = 'versions'
    time_format = datetime.now().strftime("%Y%m%d%H%M%S")
    tar_file = 'web_static_{}.tgz'.format(time_format)

    if not os.path.exists(folder_to_save):
        os.mkdir(folder_to_save)

    with tarfile.open(folder_to_save + '/' + tar_file, "w:gz") as tar:
        tar.add('web_static', arcname=os.path.basename('web_static'))

    if os.path.exists(folder_to_save + '/' + tar_file):
        return folder_to_save + '/' + tar_file
