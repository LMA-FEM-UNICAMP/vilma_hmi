import os
import json
import yaml
import errno
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch.actions import IncludeLaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
from launch.actions import OpaqueFunction

def load_yaml(yaml_file_path):
    with open(yaml_file_path, 'r') as f:
        return yaml.safe_load(f)
    
def symlink_force(target, link_name):
    try:
        os.symlink(target, link_name)
    except OSError as e:
        if e.errno == errno.EEXIST:
            os.remove(link_name)
            os.symlink(target, link_name)
        else:
            raise e

def launch_setup(context, *args, **kwargs):
    
    server_dir = os.path.join(get_package_share_directory("vilma_hmi"), "website")
    params_dir = os.path.join(get_package_share_directory("vilma_hmi"), "config")
    
    interface = LaunchConfiguration("interface").perform(context)
    
    params = load_yaml(os.path.join(params_dir, "host.param.yaml"))
    
    rosbridge_ip = params['vilma_hmi']['ros__parameters']['server_ip']
    rosbridge_port = params['vilma_hmi']['ros__parameters']['rosbridge_port']
    hmi_port = params['vilma_hmi']['ros__parameters']['server_port']
    # index = params['vilma_hmi']['ros__parameters']['index']
    
    # Create index.html file
    symlink_force(os.path.join(server_dir, interface+".html"), os.path.join(server_dir, 'index.html'))
    
    
    config = {"serviceIp": f"{rosbridge_ip}:{rosbridge_port}"}
    with open(f"{server_dir}/config.json", "w") as f:
        json.dump(config, f)
        
    # Start rosbridge_websocket on port 9090
    launch_rosbridge_server = ExecuteProcess(
        cmd=['ros2', 'launch', 'rosbridge_server', 'rosbridge_websocket_launch.xml', 'port:='+rosbridge_port],
        output='screen'
    )

    # Start Python HTTP server on port hmi_port
    launch_http_server = ExecuteProcess(
        cmd=['python3', '-m', 'http.server', hmi_port],
        cwd=server_dir,
        output='screen'
    )
        
    return [launch_rosbridge_server, launch_http_server]
        
        
def generate_launch_description():

    return LaunchDescription(
        [
        DeclareLaunchArgument("interface", default_value="vilma_status")
        ]
        +
        [OpaqueFunction(function=launch_setup)]
    )