import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from nav2_bt_example_msgs.action import Test


class TestActionServer(Node):

    def __init__(self):
        super().__init__('test_action_server')
        self._action_server = ActionServer(
            self,
            Test,
            'test_action_client',
            self.execute_callback)

        self.result = True

    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')
        result = Test.Result()
        result.response = self.result
        self.result = not self.result
        return result


def main(args=None):
    rclpy.init(args=args)

    test_action_server = TestActionServer()

    rclpy.spin(test_action_server)


if __name__ == '__main__':
    main()
