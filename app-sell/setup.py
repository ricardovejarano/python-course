from setuptools import setup


setup(
    name='sells',
    version='0.1',
    py_modules=['sells'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        sells=sells:cli
    ''',
)