#!/usr/bin/python3
# Fabric script that generates a .tgz from the contents of the web_static

import os
from datetime import datetime
from fabric.api import local


def do_pack():
    '''generates a .tgz file from webstatic'''
    try:
        local('mkdir -p versions')
        form = '%Y%m%d%H%M%S'
        tarfile = ('versions/web_static_{}.tgz'
                   .format(datetime.now().strftime(form)))
        local("tar -cvzf {} web_static/".format(tarfile))
        size = os.stat(output).st_size
        print("web_static packed: {} -> {} Bytes".format(tarfile, size))
        return tarfile
    except Exception:
        return None
