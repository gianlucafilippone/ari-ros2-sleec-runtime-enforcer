from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='sleec_enforcer_subsystem',
            executable='observation_processor',
            name='observation_processor',
            output='screen'
        ),
        Node(
            package='sleec_enforcer_subsystem',
            executable='actuation_processor',
            name='actuation_processor',
            output='screen'
        ),
    ])
