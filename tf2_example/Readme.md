## tf2_example
The tf2_example package demonstrates the use of the tf2 package in ROS to broadcast static and dynamic transforms between coordinate frames and to listen for these transforms. It includes examples of static and dynamic broadcasting, as well as a listener to query and transform points between frames.

### Nodes Overview
#### 1. static_transform_broadcast.py
- Description: This node broadcasts a static transform between two coordinate frames: base_link and camera_link. The transformation is static, meaning it doesn't change over time.
- Usage: Run this node to broadcast a fixed transformation that defines the relationship between base_link and camera_link.
- Frame IDs:
  -  base_link: The parent frame.
  -  camera_link: The child frame.
#### 2. dynamic_transform_broadcast.py
- Description: This node broadcasts a dynamic transform between base_link and gripper_link. The transformation changes over time, simulating a moving or rotating part of a robot.
- Usage: Run this node to broadcast a transformation that dynamically changes over time, representing movement or rotation between the frames.
- Frame IDs:
  - base_link: The parent frame.
  - gripper_link: The child frame.
- Transformation: The translation in the x direction varies sinusoidally over time, simulating oscillation.
#### 3. listener.py
- Description: This node listens to the transformations being broadcasted and queries the transformation between gripper_link and base_link. It transforms a point from the gripper_link frame to the base_link frame and logs the transformed point.
- Usage: Run this node to listen for transformations, query the transformation between gripper_link and base_link, and transform a point from one frame to another.
#### 4. tf2_broadcast_listen.launch
- Description: This launch file starts both the dynamic transform broadcaster and the listener nodes simultaneously. It simplifies running the example by launching both nodes together.
- Usage: Use this launch file to start the dynamic_transform_broadcast.py and listener.py nodes together.
- Run the launch file: `roslaunch tf2_example tf2_broadcast_listen.launch`
