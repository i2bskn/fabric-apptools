import os
import yaml
from fabric.api import env

def _appenv_file():
    return os.getenv('APPENV_FILE', os.path.join(os.getcwd(), 'deploy', 'appenv.yml'))

def set_environment(name='development'):
    with open(_appenv_file()) as f:
        all_envs = yaml.load(f)
        env.stage = name
        env.appenv = all_envs[name]
