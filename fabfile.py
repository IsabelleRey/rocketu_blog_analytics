from fabric.colors import green, yellow
from fabric.contrib.files import upload_template
from fabric.decorators import task
from fabric.operations import local
from fabric.api import *


env.hosts = ['54.69.252.27']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/blog_analytics.pem'
env.shell = "/bin/bash -l -i -c"
project_name = "rocketu_blog_analytics"


@task
def hello():
    print(green("I'm alive!"))


@task
def create_file(file_name):
    local("touch ~/Desktop/{}.txt".format(file_name))


@task
def create_dir(my_directory):
    local("mkdir ~/Desktop/{}".format(my_directory))


@task
def create_directory(path, directory):
    local("mkdir ~/{}/{}".format(path, directory))

@task
def ubuntu_hello():
    with hide("stdout"):
        output = run("lsb_release -a")
        print(yellow(output))


def restart_app():
    """

    :rtype : object
    """
    sudo("service supervisor restart")
    sudo("service nginx restart")


@task
def deploy():
    with prefix("workon blog_analytics"):
        with cd("/home/ubuntu/rocketu_blog_analytics"):
            run("git pull origin master")
            run("pip install -r requirements.txt")
            run("python manage.py migrate")
            run("python manage.py collectstatic --noinput")

    restart_app()


@task
def setup_nginx(project_name, server_name):
    upload_template("../deploy/nginx.conf",
                    "/etc/nginx/sites-enabled/{}.conf".format(project_name),
                    {'server_name': server_name},
                    use_sudo=True,
                    backup=False)

    restart_app()

@task
def setup_gunicorn():
    with prefix("workon blog_analytics"):
        with cd("/home/ubuntu/rocketu_blog_analytics"):
                    run("pip install gunicorn")
                    upload_template("../deploy/gunicorn.conf",
                    "rocketu_blog_analytics/gunicorn.conf.py",
                    {'project_name': project_name},
                    use_sudo=True,
                    backup=False)

    restart_app()

# @task
# def setup_supervisor(project_name, virtual_env):
#     upload_template("../deploy/supervisor.conf",
# #                     "/etc/nginx/sites-enabled/{}.conf".format(project_name),
# #                     {'program': server_name},
#                     use_sudo=True,
#                     backup=False)
#
#     restart_app()
