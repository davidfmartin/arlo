from setuptools import setup, find_packages

setup(
    name='arlo',
    version='1.0.0',
    description='arlo application framework',
    author='David Martin',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='arlo api',

    packages=find_packages(),

    install_requires=['arlo' ],

    scripts=['/opt/arlo/arlo.py'],
)
