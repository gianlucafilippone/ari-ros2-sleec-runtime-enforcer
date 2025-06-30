from setuptools import find_packages, setup

package_name = 'sleec_enforcer_subsystem'

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
    description='SLEEC Rules Enforcer Subsystem',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'observator_processor = sleec_enforcer_subsystem.abstraction_communication_layer.observation_processor:main',
            'actuation_processor = sleec_enforcer_subsystem.abstraction_communication_layer.actuation_processor:main',
            'enforcer = sleec_enforcer_subsystem.enforcer:main',
        ],
    },
)
