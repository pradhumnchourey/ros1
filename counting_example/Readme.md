## counting_example
The counting_example package is a simple demonstration of using ROS Actions in a ROS package. It consists of a server node that counts up to a specified number and a client node that sends the counting order to the server and receives feedback during the counting process.

### Nodes Overview
#### 1. count_action_server
- Description: This node implements a ROS action server that counts up to a number specified by the action client. It provides feedback during the counting process and returns the final count as a result.
- File: count_action.py
- Action Server: count_action (Type: CountAction)
- Usage: Run this node to start the action server. It will count based on the order provided by the client and send feedback during the counting process.
#### 2. count_action_client
- Description: This node acts as a ROS action client that sends a counting order to the action server. It receives feedback during the counting process and logs the result once the action is complete.
- File: count_action_client.py
- Usage: Use this node to send a counting goal to the action server. The client will log feedback during the counting and display the final result once the action is done.

### Action Definition
The action definition for the CountAction is described in the count.action file.

- Goal: order (Type: int32): The number up to which the server should count.
- Result: final_count (Type: int32): The final count value, returned after the server completes the action.
- Feedback: current_count (Type: int32): The current count value, provided as feedback during the counting process.
