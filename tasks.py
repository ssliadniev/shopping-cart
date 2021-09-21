from invoke import task


@task
def run_local(c):
    c.run("python3 ./django_project/manage.py makemigrations")
    c.run("python3 ./django_project/manage.py migrate")
    c.run("python ./django_project/manage.py runserver 0.0.0.0:8000")
