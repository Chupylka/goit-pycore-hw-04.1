from setuptools import setup, find_packages

setup(
    name='personal_assistant',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'assistant=personal_assistant.main:main',
        ],
    },
    install_requires=[
        'python-dateutil',
    ],
    description='A command-line personal assistant for managing contacts and notes.',
    author='Your Name',
    author_email='your.email@example.com',
)
