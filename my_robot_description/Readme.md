## My Robot Description
This repository contains the URDF and Gazebo files for the robot model used in the simulation. The robot's description is modularized using Xacro for flexibility and includes the necessary configurations for visualization and simulation in Gazebo.

### Contents
- example_robot.urdf.xacro: The main Xacro file describing the robot's URDF.
- example_include.xacro: Xacro file containing reusable elements like materials and inertial macros.
- example_gazebo.xacro: Xacro file with Gazebo-specific configurations, including materials and plugins.
- example_world.world: SDF file describing the Gazebo world in which the robot operates.
### Files and Their Purposes
#### example_robot.urdf.xacro
This is the main Xacro file for describing the robot. It includes:
- World Link: Represents the world frame.
- Base Link and Joint: Defines the base of the robot and its connection to the world.
- Slider Joint and Link: Describes a prismatic joint allowing movement along the X-axis.
- Arm Joint and Link: Specifies a revolute joint for the arm's rotation.
- Camera Joint and Link: Defines the camera mounted at the end of the arm.
- Includes: References example_include.xacro and example_gazebo.xacro for additional configurations and Gazebo-specific settings.

#### example_include.xacro
This file includes:
- Materials: Definitions for colors used in the robot's visual representation.
- Inertial Macros: Standard inertial properties calculations for various geometric shapes.

#### example_gazebo.xacro
This file contains Gazebo-specific settings, including:
- Materials: Gazebo-compatible material definitions.
- Plugins: Includes plugins for joint state publishing and trajectory handling.
- Camera Sensor: Configuration for adding a camera sensor to the robot.

#### example_world.world
An SDF file defining the Gazebo simulation world:
- Lighting: Sunlight settings.
- Ground Plane: Definition of the ground plane model.
- Gravity and Physics: Simulation parameters like gravity and physics engine settings.
- Scene: Ambient and background settings for the simulation environment.
