from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, RegisterEventHandler, LogInfo, TimerAction
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch.event_handlers import OnProcessStart

def generate_launch_description():

    turtlesim_ns = LaunchConfiguration("turtlesim_ns")
    background_r = LaunchConfiguration("background_r")

    turtlesim_node = Node(
        package="turtlesim",
        namespace=turtlesim_ns,
        executable="turtlesim_node",
        name="sim",
        output="screen"
    )

    change_background = TimerAction(
        period=2.0,
        actions=[
            ExecuteProcess(
                cmd=[
                    PythonExpression([
                        "'ros2 param set /",
                        turtlesim_ns,
                        "/sim background_r ",
                        background_r,
                        "'"
                    ])
                ],
                shell=True,
                output="screen"
            )
        ]
    )

    return LaunchDescription([
        DeclareLaunchArgument("turtlesim_ns", default_value="turtlesim1"),
        DeclareLaunchArgument("background_r", default_value="200"),

        turtlesim_node,

        RegisterEventHandler(
            OnProcessStart(
                target_action=turtlesim_node,
                on_start=[
                    LogInfo(msg="Turtlesim iniciado correctamente"),
                    change_background
                ]
            )
        )
    ])
