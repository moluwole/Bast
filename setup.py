from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='Bast',
      version='0.0.1.0.2',
      description='Simple yet Elegant Web Framework with MVC Patterns',
      long_description=readme(),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
          'Topic :: Software Development :: Libraries :: Application Frameworks',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      keywords='web framework tornado ORM MVC',
      url='https://github.com/moluwole/Bast',
      author='Majiyagbe Oluwole',
      author_email='oluwole564@gmail.com',
      maintainer='Majiyagbe Oluwole | Azeez Abiodun Solomon',
      license='MIT',
      packages=['bast'],
      platforms='any',
      install_requires=[
          'tornado',
          'argparse',
          'bcrypt',
          'jinja2',
          'gitpython',
          'click'
      ],
      entry_points={
          'console_scripts': ['panther=bast.cli:main'],
      },
      include_package_data=True,
      zip_safe=False)
