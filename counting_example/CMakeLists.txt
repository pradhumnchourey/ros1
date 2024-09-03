cmake_minimum_required(VERSION 3.0.2)
project(counting_example)

find_package(catkin REQUIRED COMPONENTS
  rospy
  actionlib
  actionlib_msgs
)

# Add action files
add_action_files(
  DIRECTORY action
  FILES Count.action
)

# Generate added messages and services with any dependencies
generate_messages(
  DEPENDENCIES actionlib_msgs std_msgs
)

catkin_package(
  CATKIN_DEPENDS rospy actionlib actionlib_msgs message_runtime
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

# Add executable files
catkin_install_python(PROGRAMS
  scripts/count_action_server.py
  scripts/count_action_client.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
