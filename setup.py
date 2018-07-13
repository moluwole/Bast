from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='bast',
    version='0.1',
    py_modules=['bast'],
    install_requires=[
        'argparse',
        'Flask-Migrate'
    ],
    entry_points='''
        [console_scripts]
        bast_cli=bast_cli:cli
    ''',
)
