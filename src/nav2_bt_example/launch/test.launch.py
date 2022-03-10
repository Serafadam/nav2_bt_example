import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import OpaqueFunction
from launch_ros.actions import Node


def launch_setup(context, *args, **kwargs):

    bt_example_dir = get_package_share_directory('nav2_bt_example')
    nav_params_file = os.path.join(bt_example_dir, 'config', 'params.yaml')
    lifecycle_nodes = ['bt_navigator']
    nav = Node(
        package='nav2_bt_navigator',
        executable='bt_navigator',
        name='bt_navigator',
        output='screen',
        parameters=[nav_params_file],)
    lfc = Node(
        package='nav2_lifecycle_manager',
        executable='lifecycle_manager',
        name='lifecycle_manager_navigation',
        output='screen',
        parameters=[{'use_sim_time': True},
                    {'autostart': True},
                    {'node_names': lifecycle_nodes}])
    return [nav, lfc]


def generate_launch_description():
    return LaunchDescription(
        [
            OpaqueFunction(function=launch_setup),
        ]
    )
