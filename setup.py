from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'vilma_hmi'

def package_files(directory):
    paths = []
    for (path, _, filenames) in os.walk(directory):
        install_path = os.path.join('share', package_name, path)
        files = [os.path.join(path, f) for f in filenames]
        if files:
            paths.append((install_path, files))
    return paths

data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
        (os.path.join('share', package_name, 'config'), glob(os.path.join('config', '*')))
    ]

data_files += package_files('website')

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=data_files,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Gabriel Toffanetto',
    maintainer_email='gabriel.rocha@ieee.org',
    description='VILMA HMI',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
