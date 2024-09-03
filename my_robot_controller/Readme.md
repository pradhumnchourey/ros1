## my_robot_controller:
The my_robot_controller package contains a collection of ROS nodes for controlling and interacting with a robot (specifically a turtle in Turtlesim). The nodes included in this package demonstrate various ROS concepts such as publishing, subscribing, and using services.

### Nodes Overview
#### 1. my_first_node
- Description: A basic ROS node that logs a "Hello" message to the console at a rate of 1 Hz.
- File: my_first_node.py
- Usage: This node is useful for understanding the basics of node creation and logging in ROS.
#### 2. draw_circle_node
- Description: This node publishes velocity commands to move the turtle in a circular pattern in the Turtlesim simulation.
- File: draw_circle_node.py
- Published Topic: /turtle1/cmd_vel (Type: geometry_msgs/Twist)
- Usage: Run this node to see the turtle drawing a circle in the Turtlesim window. 
#### 3. pose_subscriber
- Description: A node that subscribes to the turtle's pose in Turtlesim and logs the pose information to the console.
- File: pose_subscriber.py
- Subscribed Topic: /turtle1/pose (Type: turtlesim/Pose)
- Usage: This node helps in understanding how to subscribe to topics and process the received data.
#### 4. turtle_controller
- Description: A controller node that commands the turtle to move within certain boundaries in the Turtlesim environment. If the turtle     reaches the boundary, it changes direction.
- File: turtle_controller.py
- Published Topic: /turtle1/cmd_vel (Type: geometry_msgs/Twist)
- Subscribed Topic: /turtle1/pose (Type: turtlesim/Pose)
- Usage: Use this node to see how a basic controller can be implemented using ROS.
#### 5. turtle_controller_with_service
- Description: An advanced version of the turtle controller that changes the turtle's pen color when it crosses a specific boundary in      the Turtlesim environment. It demonstrates the use of ROS services.
- File: turtle_controller_with_service.py
- Published Topic: /turtle1/cmd_vel (Type: geometry_msgs/Twist)
- Subscribed Topic: /turtle1/pose (Type: turtlesim/Pose)
- Used Service: /turtle1/set_pen (Type: turtlesim/SetPen)
- Usage: Run this node to see how to use ROS services in combination with topic-based control.
