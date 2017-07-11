import os
import tempfile
from fabric.api import env
from fabric_apptools.common import *
from fabric_apptools.appenv import set_appenv

def build_template(name, path=None, params=None, name='development'):
    tplenv = template_env()
    template = tplenv.get_template(name)

    if not path:
        path = os.path.join(tempfile.mkdtemp(), os.path.basename(name))
    if not params:
        if 'appenv' not in env:
            set_appenv(name)
        params = env.appenv

    with open(path, 'w') as f:
        f.write(template.render(params))

    return path
