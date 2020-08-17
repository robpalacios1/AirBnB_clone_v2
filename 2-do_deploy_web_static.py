#!/usr/bin/python3
"""
deploys archive to web servers
"""
from fabric.operations import put, run, env
import os

env.hosts = ['35.231.232.13', '3.92.138.255']


def do_deploy(archive_path):
    if os.path.exists(archive_path) is False:
        return False
    else:
        put(archive_path, "/tmp/")
        tgzfile = archive_path.split('/')[1]
        archivedir = tgzfile.split('.')[0]
        run("mkdir -p /data/web_static/releases/{}/"
            .format(archivedir))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(tgzfile, archivedir))
        run("rm /tmp/{}".format(tgzfile))
        run("mv /data/web_static/releases/{}/web_static/* \
        /data/web_static/releases/{}/"
            .format(archivedir, archivedir))
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(archivedir))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(archivedir))
        return True
