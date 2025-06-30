import rclpy
from rclpy.node import Node
from robot_sim_interfaces.srv import TaskExecutorService


class TaskExecutorNode(Node):
    def __init__(self):
        super().__init__('task_executor_node')

        # Service setup
        self.task_executor_service = self.create_service(TaskExecutorService, 'task_executor_service', self.execute_task_callback)

    def execute_task_callback(self, request, response):
        self.get_logger().info(f"Now executing: {request.task}")
        response.result = "Done!"
        return response

def main(args=None):
    rclpy.init(args=args)
    node = TaskExecutorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()