#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the
contents of the web_static folder of your AirBnB Clone repo,
using the function do_pack
"""
import os
from collections.abc import Mapping
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    generates a .tgz archive from the contents of
    the web_static folder of your AirBnB Clone repo
    """
    try:
        local("mkdir -p versions")
        t = datetime.now()
        archive_name = 'web_static_{}{}{}{}{}{}.tgz'.format(
            t.year, t.month, t.day, t.hour, t.minute, t.second)
        local("tar -cvzf versions/{}.tgz web_static".format(archive_name))
        return f'versions/{archive_name}'
    except Exception as e:
        print(str(e))
