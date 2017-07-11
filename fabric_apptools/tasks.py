from fabric.api import task
from fabric_apptools.appenv import set_appenv

@task
def appenv(name='development'):
    set_appenv(name)
