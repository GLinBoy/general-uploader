from setuptools import setup

setup(
    name='EasyShare',
    version='0.1',
    py_modules=['yourscript'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        app=app:cli
    ''',
)