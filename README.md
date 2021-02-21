# Uploader

A simple uploader to help me upload my files from my phon to my PC/Laptop

## Summary

  - [Getting Started](#getting-started)
  - [Runing the tests](#running-the-tests)
  - [Deployment](#deployment)
  - [Built With](#built-with)
  - [Contributing](#contributing)
  - [Versioning](#versioning)
  - [Authors](#authors)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Uploader needs python 3.x to run;

#### Runing from the source

1. clone the project on your system:

    git clone https://github.com/GLinBoy/general-uploader.git

2. go to the Uploader directory

    cd general-uploader

3. Create a virual env:

    python3 -m venv .venv

3. install dependencies:

    pip install -r requirements.txt

4. Run application with this command:

    gunicorn -w 1 -b 0.0.0.0:5000 app:app --timeout=600

### Installing

Please, let me finish project and then give you installation instructions 😊

## Running the tests

I haven't any test yet.

### Break down into end to end tests

I didn't develop any test for project, YET, but I will add tests as soon as possible.

### And coding style tests

I didn't develop any test for project, YET, but I will add tests as soon as possible.

## Deployment

I added Gunicorn as a WSGI application, then you can use it anywhere (⛔️ DON'T USE IT ON CRITICAL ENV. ⛔️)

## Built With

  - [Python](https://python.orf/) - Main Development language, used version 3

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code
of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions
available, see the [tags on this
repository](https://github.com/PurpleBooth/a-good-readme-template/tags).

## Authors

  - **Hojjat Abedi** - [GLinBoy](https://github.com/GLinBoy)


## License

This project is licensed under the [MIT License](LICENSE.md) - see the [LICENSE.md](LICENSE.md) file for
details

## Acknowledgments

This section filled by your question 😊

