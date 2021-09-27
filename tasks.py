from invoke import task


@task
def run_local(ctx):
    ctx.run('python3 manage.py collectstatic')
    # download dump DB
    ctx.run("python3 ./manage.py makemigrations")
    ctx.run("python3 ./manage.py migrate")
    ctx.run("python3 ./manage.py runserver 0.0.0.0:8000")
