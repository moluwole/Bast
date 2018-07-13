from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='bast',
      version='0.1',
      description='Simple Web Framework yet Elegant with MVC Patterns',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='funniest joke comedy flying circus',
      url='http://github.com/storborg/funniest',
      author='Azeez Abiodun S. | Majiyagbe Oluwole',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['bast'],
      install_requires=[
          'tornado',
          'argparse'
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      entry_points={
          'console_scripts': ['bast=bast.command_line:main'],
      },
      include_package_data=True,
      zip_safe=False)