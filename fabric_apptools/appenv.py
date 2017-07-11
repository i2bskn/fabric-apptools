import os
import yaml
from fabric.api import env
from fabric_apptools.common import *

def set_appenv(name='development'):
    with open(appenv_file()) as f:
        all_envs = yaml.load(f)
        env.stage = name
        env.appenv = all_envs[name]
