from setuptools import setup
from easy_credit import __version__

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='EasyPayClient',
    version=__version__,
    description='A easyCredit Python SDK',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/cgsmith/easycredit-api-sdk-python',
    license='MIT',
    author='Chris Smith',
    author_email='cgsmith105@gmail.com',
    packages=['easyCredit'],
    keywords=['easyCredit', 'Credit', 'Ratenkauf', 'Payments', 'Python', 'API', 'SDK'],
    install_requires=['requests >= 2.28.1'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)