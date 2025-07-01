from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='robot_sim',
            executable='task_executor',
            name='task_executor',
            output='screen'
        ),
        Node(
            package='robot_sim',
            executable='topic_publisher',
            name='topic_publisher',
            output='screen'
        ),
    ])
