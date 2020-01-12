from setuptools import setup

setup(
    name="autoclicker",
    version="1.0",
    description="Python program that clicks for you",
    author="Harry Ceong",
    packages=['autoclicker','autoclicker.commons'],
    install_requires=['pynput==1.4'],
    classifiers=[
        'Programming Language :: Python :: 3.6'
    ],
    python_requires='>=3.6'
)