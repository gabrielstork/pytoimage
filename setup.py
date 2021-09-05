import setuptools

with open('README.md', 'r', encoding='utf-8') as file:
    long_description = file.read()

setuptools.setup(
    name='pytoimage',
    version='0.0.1',
    author='Gabriel Stork',
    author_email='storkdeveloper@gmail.com',
    license='MIT',
    description='Transform your Python code in a image.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/gabrielstork/directory-structure',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    package_dir={'': '.'},
    packages=setuptools.find_packages(where='.'),
    python_requires='>=3',
    install_requires=['pillow'],
)
