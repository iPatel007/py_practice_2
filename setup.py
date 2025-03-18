from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='mlproject-2',
    version='0.1.0',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    entry_points={
        'console_scripts': [
            # Define your command line scripts here
        ],
    },
    author='Amit Jarsaniya',
    author_email='amit.patel@example.com',
    description='A short description of your package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/your-repo',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)