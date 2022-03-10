cmake_minimum_required(VERSION 3.10)
project(nav2_bt_example)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 17)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclcpp_action REQUIRED)
find_package(rclpy REQUIRED)
find_package(behaviortree_cpp_v3 REQUIRED)
find_package(nav2_behavior_tree REQUIRED)
find_package(nav2_bt_example_msgs REQUIRED)

include_directories(
  include
)

set(DEPENDENCIES
"rclcpp"
"behaviortree_cpp_v3"
"nav2_behavior_tree"
"nav2_bt_example_msgs")



add_library(test_action_client SHARED src/test_action_client.cpp)
list(APPEND TEST_PLUGINS test_action_client)
add_library(test_srv_client SHARED src/test_srv_client.cpp)
list(APPEND TEST_PLUGINS test_srv_client)

foreach(BT_PLUGIN ${TEST_PLUGINS})
  ament_target_dependencies(${BT_PLUGIN} ${DEPENDENCIES})
  target_compile_definitions(${BT_PLUGIN} PRIVATE BT_PLUGIN_EXPORT)
endforeach()

install(TARGETS ${TEST_PLUGINS}
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION bin
)
ament_export_libraries(
  ${TEST_PLUGINS}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # uncomment the line when a copyright and license is not present in all source files
  #set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # uncomment the line when this package is not in a git repo
  #set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()
ament_python_install_package(${PROJECT_NAME})
install(PROGRAMS
  scripts/action_test.py
  DESTINATION lib/${PROJECT_NAME}
)
install(DIRECTORY launch config
DESTINATION share/${PROJECT_NAME}
)
ament_export_include_directories(
  include
)

ament_export_libraries(
  ${plugin_libs}
)

ament_export_dependencies(${DEPENDENCIES})

ament_package()
