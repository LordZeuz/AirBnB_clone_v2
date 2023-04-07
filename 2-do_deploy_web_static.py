#!/usr/bin/python3
# deploying archive with fabric

from fabric.api import env, run, put
import os


env.hosts = ['107.21.16.201', '100.25.169.239']
env.user = 'ubuntu'


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
