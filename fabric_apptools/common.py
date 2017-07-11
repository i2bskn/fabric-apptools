import os
import jinja2

def deploy_path():
    return os.getenv('DEPLOY_PATH', os.getcwd(), 'deploy')

def appenv_file():
    return os.getenv('APPENV_FILE', os.path.join(deploy_path(), 'appenv.yml'))

def template_path():
    return os.getenv('DEPLOY_TEMPLATE_PATH', os.path.join(os.getcwd(), 'deploy', 'templates'))

def template_env():
    return jinja2.Environment(loader=jinja2.FileSystemLoader(template_path()))
