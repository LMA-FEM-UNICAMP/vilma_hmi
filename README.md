# vilma_hmi

VILMA's HMI in browser using ROS2 WebSocket bridge.

## Configuration

In the `host.param.yaml`, configure the IP and ports of the server.

## How to use

HMI mode is selected by the parameter `hmi`on launch.

```shell
ros2 launch vilma_hmi vilma_hmi.launch.py interface:=vilma_autoware
```

## Interfaces

### VILMA Autoware

Interface designed to control modes and monitoring VILMA over the use of Autoware.

`interface:=vilma_autoware`

### Platooning HMI

HMI for V2X platooning.

### VILMA Status (legacy)
  
## Notes

- `roslib.min.js` come from `https://cdn.jsdelivr.net/npm/roslib/build/roslib.min.js`, that needs to be downloaded to use in LAN.
