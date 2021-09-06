import setuptools

with open('README.md', 'r', encoding='utf-8') as file:
    long_description = file.read()

setuptools.setup(
    name='pytoimage',
    version='0.0.1',
    description='Transform your Python code in an image.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/gabrielstork/pytoimage',
    author='Gabriel Stork',
    author_email='storkdeveloper@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    keywords='image code custom theme color palette',
    packages=setuptools.find_packages(),
    include_package_data = True,
    install_requires=['pillow'],
    python_requires='>=3',
)
