from setuptools import find_packages, setup

package_name = 'offline_replay'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/offline_replay_camera.launch.py']),
        ('share/' + package_name + '/launch', ['launch/offline_replay_camera_viewer.launch.py']),
        ('share/' + package_name + '/config', ['config/replay.yaml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hamza',
    maintainer_email='hamzafar_89@hotmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'camera_publisher = offline_replay.camera_publisher:main',
        ],
    },
)
