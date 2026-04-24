from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution, TextSubstitution

def generate_launch_description():

    return LaunchDescription([

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                PathJoinSubstitution([
                    FindPackageShare("actividad1_launch"),
                    "launch",
                    "subs_events.launch.py"
                ])
            ),
            launch_arguments={
                "turtlesim_ns": "turtlesim2",
                "background_r": TextSubstitution(text="200")
            }.items()
        )
    ])
