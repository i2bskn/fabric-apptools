from fabric.api import env

def set_environment(stage='development'):
    env.appenv = {'stage': stage}
