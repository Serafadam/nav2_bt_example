// Copyright 2022 Adam Serafin
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.


#ifndef NAV2_BT_EXAMPLE__TEST_ACTION_CLIENT_HPP_
#define NAV2_BT_EXAMPLE__TEST_ACTION_CLIENT_HPP_

#include <string>

#include "nav2_behavior_tree/bt_action_node.hpp"
#include "nav2_bt_example_msgs/action/test.hpp"

namespace nav2_bt_example
{

class TestActionClient : public nav2_behavior_tree::BtActionNode<nav2_bt_example_msgs::action::Test>
{
public:
  TestActionClient(
    const std::string & xml_tag_name,
    const std::string & action_name,
    const BT::NodeConfiguration & conf);

  void on_tick() override;

  static BT::PortsList providedPorts()
  {
    return providedBasicPorts({});
  }
};

}  // namespace nav2_bt_example

#endif  // NAV2_BT_EXAMPLE__TEST_ACTION_CLIENT_HPP_
