from setuptools import setup, find_namespace_packages


setup(
    name='qtoggleserver-mppsolar',
    version='unknown-version',
    description='MPP Solar inverters support for qToggleServer',
    author='Calin Crisan',
    author_email='ccrisan@gmail.com',
    license='Apache 2.0',

    packages=find_namespace_packages(),

    install_requires=[
        'pyserial>=3.4',
        'pyserial-asyncio>=0.4',
    ]
)
