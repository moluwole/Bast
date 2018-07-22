from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='bast',
      version='0.1',
      description='Simple yet Elegant Web Framework with MVC Patterns',
      long_description=readme(),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Web Framework',
          'Framework :: Bast',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.*',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
          'Topic :: Software Development :: Libraries :: Application Frameworks',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      keywords='funniest joke comedy flying circus',
      url='https://github.com/moluwole/Bast',
      author='Majiyagbe Oluwole',
      contributors=['Majiyagbe Oluwole', 'Azeez Abiodun Solomon'],
      author_email='oluwole564@gmail.com',
      license='MIT',
      packages=['bast'],
      platforms='any',
      python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',
      install_requires=[
          'tornado',
          'argparse',
          'bcrypt',
          'jinja2'
      ],
      entry_points={
          'console_scripts': ['bast=bast.cli:main'],
      },
      include_package_data=True,
      zip_safe=False)
