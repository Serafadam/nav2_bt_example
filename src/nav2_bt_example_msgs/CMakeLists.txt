cmake_minimum_required(VERSION 3.10)
project(nav2_bt_example_msgs)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 17)
endif()

if(CMAKE_COMPILER_IS_GNUXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(rosidl_default_generators REQUIRED)
find_package(std_msgs REQUIRED)

rosidl_generate_interfaces(
${PROJECT_NAME}
"action/Test.action"
"srv/Test.srv"
DEPENDENCIES std_msgs
)

ament_package()
