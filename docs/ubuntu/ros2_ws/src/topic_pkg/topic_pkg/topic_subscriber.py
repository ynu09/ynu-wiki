import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Subscriber(Node):
    def __init__(self):
        super().__init__('subscriber')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10)
        self.subscription

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: "{msg.data}"')

def main():
    rclpy.init()
    node = Subscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass # Ctrl+c 무시
    finally:
        node.destroy_node()
        rclpy.shutdown()