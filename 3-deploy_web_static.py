#!/usr/bin/python3
''' fabfile to run on remote server'''

from datetime import datetime
from fabric.api import env, run, put, local
import os


env.hosts = ['35.153.19.82', '52.91.202.212']
env.user = 'ubuntu'


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


def do_deploy(archive_path):
    '''distributes an archive to your web servers'''
    if not os.path.exists(archive_path):
        return False
    try:
        bname = os.path.basename(archive_path)
        put(archive_path, '/tmp/')
        run("mkdir -p  /data/web_static/releases/{}/".format(bname[:-4]))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(bname,
            bname[:-4]))
        run('rm /tmp/{}'.format(bname))
        run('mv /data/web_static/releases/{}/web_static/* /data/web_static/'
            'releases/{}/'.format(bname[:-4], bname[:-4]))
        run('rm -rf /data/web_static/releases/{}/web_static/'.format(
             bname[:-4]))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(bname[:-4]))
        print("New version deployed!")
        return True
    except Exception:
        return False


def deploy():
    """Create and distribute an archive to a web server."""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
