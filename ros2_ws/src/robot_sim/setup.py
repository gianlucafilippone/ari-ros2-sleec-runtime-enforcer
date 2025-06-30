from setuptools import find_packages, setup

package_name = 'robot_sim'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Gianluca Filippone',
    maintainer_email='gianluca.filippone@gssi.it',
    description='Mock robot package',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'task_executor = robot_sim.task_executor:main',
            'topic_publisher = robot_sim.topic_publisher:main',
        ],
    },
)
