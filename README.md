# gold-trading-platform

## Login Page
<div>
     <img src="https://github.com/Ghannoum99/gold-trading-platform/blob/main/login-image.jpeg">
</div>

## Sign Up Page
<div>
     <img src="https://github.com/Ghannoum99/gold-trading-platform/blob/main/signup-image.jpeg">
</div>


## Setup

The first thing to do is to clone the repository:

```sh
$ git clonehttps://github.com/Ghannoum99/gold-trading-platform.git
$ cd gold-trading-platform
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd gold-trading-platform
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

