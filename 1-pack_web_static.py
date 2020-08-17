#!/usr/bin/python3
"""
uses fabric to pack web_static into file
"""
from fabric.operations import local
import os
from datetime import datetime


def do_pack():
    try:
        if os.path.exists("versions") is False:
            local("mkdir versions")
            created = datetime.now().strftime("%Y%m%d%H%M%S")
            tgzfile = "versions/web_static_{}.tgz".format(created)
            local("tar -cvzf {} web_static".format(tgzfile))
            return tgzfile
    except:
        return None
