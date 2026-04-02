from launch import LaunchDescription
from launch.actions import TimerAction
from launch_ros.actions import Node

def generate_launch_description():
    agv_controller_node = Node(
        package='agv_image_processing',
        executable='controller_agv_speed_twiststamped',
        name='agv_controller_speed_update',
        output='screen'
    )

    range_detection_node = Node(
          package='agv_image_processing',
          executable='range_detection_with_safety',
          name='range_detection_with_safety',
          output='screen'
     )
      
    return LaunchDescription([
        agv_controller_node,
        range_detection_node
    ])

