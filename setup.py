from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='alltweets',
    version='0.2',
    description='A very simple Twitter crawler that can collect all friends, followers, and tweets of a specified user.',
    long_description='A very simple Twitter crawler that can collect all friends, followers, and tweets of a specified user.',
    classifiers=[
        'Development Status :: 3 - Alpha',
    ],
    keywords = 'Twitter crawl timeline',
    url='http://github.com/j1wan/alltweets',
    author='Jiwan Jeong',
    author_email='jiwanjeong@gmail.com',
    license='MIT',
    packages=['alltweets'],
    install_requires=['requests'],
    zip_safe=False
)
