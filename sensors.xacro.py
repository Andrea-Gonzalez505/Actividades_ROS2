<?xml version="1.0"?>
<robot xmlns:xacro="http://www.ros.org/wiki/xacro">
  <!-- ========================= -->
  <!-- IMU -->
  <!-- ========================= -->
  <link name="imu_link">
    <visual>
      <geometry>
        <box size="0.08 0.08 0.04"/>
      </geometry>
      <material name="red">
        <color rgba="1 0 0 1"/>
      </material>
    </visual>
    <collision>
      <geometry>
        <box size="0.08 0.08 0.04"/>
      </geometry>
    </collision>
    <xacro:box_inertia m="0.1" x="0.08" y="0.08" z="0.04"/>
  </link>
  <joint name="imu_joint" type="fixed">
    <parent link="base_link"/>
    <child link="imu_link"/>
    <origin xyz="0 0 0.12" rpy="0 0 0"/>
  </joint>
  <!-- ========================= -->
  <!-- LIDAR -->
  <!-- ========================= -->
  <link name="lidar_link">
    <visual>
      <geometry>
        <cylinder radius="0.06" length="0.05"/>
      </geometry>
      <material name="red">
        <color rgba="1 0 0 1"/>
      </material>
    </visual>
    <collision>
      <geometry>
        <cylinder radius="0.06" length="0.05"/>
      </geometry>
    </collision>
    <xacro:cylinder_inertia m="0.2" r="0.06" h="0.05"/>
  </link>
  <joint name="lidar_joint" type="fixed">
    <parent link="base_link"/>
    <child link="lidar_link"/>
    <origin xyz="0 0 0.18" rpy="0 0 0"/>
  </joint>
  <!-- ========================= -->
  <!-- CÁMARA -->
  <!-- ========================= -->
  <link name="camera_link">
    <visual>
      <geometry>
        <box size="0.08 0.04 0.04"/>
      </geometry>
      <material name="red">
        <color rgba="1 0 0 1"/>
      </material>
    </visual>
    <collision>
      <geometry>
        <box size="0.08 0.04 0.04"/>
      </geometry>
    </collision>
    <xacro:box_inertia m="0.15" x="0.08" y="0.04" z="0.04"/>
  </link>
  <joint name="camera_joint" type="fixed">
    <parent link="base_link"/>
    <child link="camera_link"/>
    <origin xyz="0.23 0 0.04" rpy="0 0 0"/>
  </joint>
