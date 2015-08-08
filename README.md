# A simple TODO web app

This was my hand at creating the web app demoed [here](http://www.vertabelo.com/blog/technical-articles/web-app-development-with-flask-sqlalchemy-bootstrap-introduction).

It will soon be deployed on Heroku as well

## Getting started

Honestly, you should start with the blog posts -- they will walk you through it. It's done well enough, though I do have some caveats:

1. Midway through you will be prompted to register for the blog hoster's service, Vertabelo. It's their project so kudos to them for the self promotion, but I don't know what that will give you in addition to writing your `models.py` file for you. I did the entire project without it.
2. The python side of the world is totally fleshed out, with only a few minor differences between the web tutorial and the final [repo out on github](https://github.com/pdybka-ep/flask-todoapp) (*e.g.* several views not yet defined in the web tutorial). The HTML side, however, is not really discussed concretely in the tutorial at all. I found myself just copying the files over from the github repo, and working through what was going on there on my own.

If you want to work with the files I have, that should be easy enough too! In a *nix terminal, the following should work (in concept!). If your run into any errors, again, go to [the web tutorial](https://github.com/pdybka-ep/flask-todoapp), where the steps are explained in depth.

### preparing your local python environment
```bash
git clone https://github.com/RZachLamberty/test_webapp.git
cd ./test_webapp
virtualenv /path/to/venv
. /path/to/venv/bin/activate
pip install -r ./requirements.txt
```

### preparing your psql environment
```bash
sudo su - postgres
psql -f /path/to/github/repo/test_webapp/create_tablse.sql
exit
```

### starting the application
```bash
cd /path/to/github/repo/test_webapp
python todoapp.py
```
