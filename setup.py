from setuptools import setup, find_packages

setup(name='muZic',
    version='1.0',
    description='Download music from youtube and store it in a device',
    classifiers=[
        'License :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    author='xzebra',
    license='MIT',
    packages=find_packages(include=[
        'src', 'src.*'
    ]),
    install_requires=[
        'tabulate',
        'pexpect',
        'pysqlite',
      ],
    entry_points = {
        'console_scripts': ['muZic=src.muZic:main',],
    },
    include_package_data=True,
    zip_safe=False)
