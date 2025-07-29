from setuptools import setup, find_packages

setup(
    name='EmotionDetector',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    description='A package to detect emotions using Watson NLP',
    author='Mauricio Garcia',
    author_email='maupessoagarcia@yahoo.ccom',
    url='https://github.com/yourusername/emotion-detector',
)