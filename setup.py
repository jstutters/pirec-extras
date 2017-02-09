from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='plumbium-extras',
    version='0.0.4',
    packages=['plumbium_extras'],
    zip_safe=True,
    author='Jon Stutters',
    author_email='j.stutters@ucl.ac.uk',
    description='Tools for working with plumbium',
    long_description=readme(),
    url='https://github.com/jstutters/plumbium-extras',
    install_requires=['click'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pbtool=plumbium_extras.cli:cli'
        ]
    },
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Topic :: System :: Logging'
    ]
)
