# django-shop

[![Language](https://img.shields.io/badge/language-python-brightgreen?style=flat-square)](https://www.python.org/)

Hello everyone! This is the repository of shop application on Django framework.

## Table of contents

- [Table of contents](#table-of-contents)
- [Motivation](#motivation)
- [Build status](#build-status)
- [Badges](#badges)
- [Screenshots](#screenshots)
- [Tech/framework used](#techframework-used)
- [Features](#features)
- [Installation](#installation)
- [Fast usage](#fast-usage)
- [Tests](#tests)
- [Contribute](#contribute)
- [Credits](#credits)
- [License](#license)

## Motivation

I have wanted to make my own shop website. I've done this before with [WordPress](https://uk.wordpress.org/) and [WooCommerce](https://woocommerce.com/). Then I found the **best** [tutorials](https://www.youtube.com/channel/UCTZRcDjjkVajGL6wd76UnGg) for Django on YouTube and make shop with **it**. So it is very good practice and also the template.:blush:

## Build status

Here you can see build status of [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration):

![Django CI](https://github.com/mezgoodle/django-shop/workflows/Django%20CI/badge.svg)
![Lint Code Base](https://github.com/mezgoodle/django-shop/workflows/Lint%20Code%20Base/badge.svg)

## Badges

[![Theme](https://img.shields.io/badge/Theme-Shop-brightgreen?style=flat-square)](https://www.google.com/search?q=django+shop&rlz=1C1CHZO_ukUA900UA900&oq=django+shop&aqs=chrome..69i57j0l5j69i60l2.2903j1j7&sourceid=chrome&ie=UTF-8)
[![Platform](https://img.shields.io/badge/Platform-Django-brightgreen?style=flat-square)](https://www.djangoproject.com/)
 
## Screenshots

- Main page

![Screenshot 1](https://raw.githubusercontent.com/mezgoodle/images/master/django-shop1.png)

- Product page

![Screenshot 2](https://raw.githubusercontent.com/mezgoodle/images/master/django-shop2.png)

- Share page

![Screenshot 3](https://raw.githubusercontent.com/mezgoodle/images/master/django-shop3.png)

- Cart page

![Screenshot 4](https://raw.githubusercontent.com/mezgoodle/images/master/django-shop4.png)

- Checkout page

![Screenshot 5](https://raw.githubusercontent.com/mezgoodle/images/master/django-shop5.png)

## Tech/framework used

**Built with**

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Pillow](https://pillow.readthedocs.io/en/stable/)

## Features

On the website you can add customers, products, share them, make orders for authenticated and non users.

> Also you can add payment system, such as [PayPal](https://developer.paypal.com/demo/checkout/#/pattern/client)

## Installation

1. Clone this repository:

```bash
git clone https://github.com/mezgoodle/django-shop.git
```

2. Install all dependencies with [pip](https://pip.pypa.io/en/stable/):

```bash
pip install -r requirements.txt
```

## Fast usage

1. Rename .env_sample to .env and fill the variables like:

```bash
EMAIL_HOST_PASSWORD="<YOUR_EMAIL_PASSWORD>"
```

2. Move to _ecommerce_ directory, make migrations and create super-user:

```bash
cd ecommerce
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
```

3. Start the development server:

```bash
python3 manage.py runserver
```

## Tests

You can see all tests in [**tests.py**](https://github.com/mezgoodle/django-shop/blob/master/ecommerce/store/tests.py). And there results [here](https://github.com/mezgoodle/django-shop/actions?query=workflow%3A%22Django+CI%22).

## Contribute

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Credits

Credit to **Dennis Ivy** tutorial:

- [Playlist on YouTube](https://www.youtube.com/watch?v=QSyrThcaghg&list=PL-51WBLyFTg0omnamUjL1TCVov7yDTRng)

## License

MIT © [mezgoodle](https://github.com/mezgoodle)
