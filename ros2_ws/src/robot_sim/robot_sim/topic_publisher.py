import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TopicPublisherNode(Node):
    def __init__(self):
        super().__init__('topic_publisher_node')

        # Publishers setup
        self.counter = 0
        self.sensor_data_publisher = self.create_publisher(String, 'sensor_data', 10)

        # Timer setup
        self.create_timer(2.0, self.publish_sensor_data)

    def publish_sensor_data(self):
        message = String()
        message.data = f"Sensor Data #{self.counter}"
        self.sensor_data_publisher.publish(message)
        self.counter+=1


def main(args=None):
    rclpy.init(args=args)
    node = TopicPublisherNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()