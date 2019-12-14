from setuptools import setup, find_packages


setup(
    name='thoughts',
    version='1.0.1',
    author='Orr Benyamini',
    description='Advanced system design project: A brain computer interface',
    packages=find_packages(),
    install_requires=['click', 'flask'],
    tests_require=['pytest', 'pytest-cov'],
)
