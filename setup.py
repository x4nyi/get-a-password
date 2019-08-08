from setuptools import setup

setup(name='get-a-password',
      version='19.08.08',
      description='password manager',
      url='https://github.com/x4nyi/get-a-password',
      packages=['get_a_password'],
      scripts=['bin/get-a-password'],
      install_requires=[
        'click>=6.0'
      ],
      zip_safe=False)
