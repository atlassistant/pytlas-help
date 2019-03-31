pytlas-help ![License]( https://img.shields.io/badge/License-GPL%20v3-blue.svg)
===

Provides some help to the users such as what are the currently available skills and how to trigger them.

## Supported languages

- French
- English

## Typical sentences

- How can you help?
- Que sais-tu faire ?

## Launching tests

In order to launch tests, you will need to install required dependencies and then launch the test suite with:

```bash
$ pip install -r requirements_tests.txt
$ python -m nose --with-coverage --cover-package=help
```