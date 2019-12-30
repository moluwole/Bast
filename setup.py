from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='Bast',
      version='1.0.1',
      description='Simple yet Elegant Web Framework with MVC Patterns',
      long_description=readme(),
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
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
          'bcrypt',
          'jinja2',
          'gitpython',
          'click',
          'orator',
          'python-env',
          'colorama',
          'nose',
          'twine'
      ],
      entry_points={
          'console_scripts': ['panther=bast.cli:main'],
      },
      include_package_data=True,
      zip_safe=False)
