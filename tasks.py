from invoke import task
import time


def wait_port_is_open(host, port):
    import socket
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((host, port))
        sock.close()
        if result == 0:
            return
        time.sleep(1)


@task
def run_local(ctx):
    wait_port_is_open('db', 5432)
    ctx.run('python manage.py collectstatic --noinput')
    # download dump DB
    ctx.run("python ./manage.py makemigrations")
    ctx.run("python ./manage.py migrate")
    ctx.run("python ./manage.py runserver 0.0.0.0:8000")
