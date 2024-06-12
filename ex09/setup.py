from setuptools import setup, find_packages


setup(
    name='ft_package',
    version='0.0.1',
    author='Plaetorius',
    author_email='plaetorius@example.com',
    description='A simple example Python library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Plaetorius/Piscine-Python',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)