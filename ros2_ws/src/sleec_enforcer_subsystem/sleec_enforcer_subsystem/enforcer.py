import rclpy
from rclpy.node import Node
import asyncio
import httpx
import threading

class EnforcerNode(Node):
    def __init__(self):
        super().__init__('enforcer_node')

        self.loop = asyncio.new_event_loop()
        self.thread = threading.Thread(target=self.start_loop, daemon=True)
        self.thread.start()

        self.mape_loop_timer = self.create_timer(5.0, self.timer_callback)

    def start_loop(self):
        asyncio.set_event_loop(self.loop)
        self.loop.run_forever()

    def timer_callback(self):
        self.loop.call_soon_threadsafe(asyncio.create_task, self.enforcer_loop())

    # async def call_rest_service(self):
    #     try:
    #         async with httpx.AsyncClient() as client:
    #             response = await client.post(
    #                 "http://localhost:8001/obligation/execute",
    #                 json={"task": "example_task"}
    #             )
    #             self.get_logger().info(f"Response: {response.json()}")
    #     except Exception as e:
    #         self.get_logger().error(f"REST call failed: {e}")

    async def enforcer_loop(self):
        try:
            async with httpx.AsyncClient() as client:
                probe_response = await client.get("http://localhost:8000/probe/latest_data")
                probe_data_json = probe_response.json()

                self.get_logger().info(f"Probe data: {probe_data_json}")

                probe_data = probe_data_json.get("latest_data")
                if probe_data is None:
                    self.get_logger().warn("No probe data")
                    return

                # Data analysis, then when done and if needed
                task = "example_task"

                obligation_response = await client.post(
                    "http://localhost:8001/obligation/execute",
                    json={"task": task}
                )
                obligation_response_json = obligation_response.json()

                self.get_logger().info(f"Obligation service response: {obligation_response_json}")

        except Exception as e:
            self.get_logger().error(f"Error in REST call: {e}")


def main(args=None):
    rclpy.init(args=args)
    node = EnforcerNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.loop.call_soon_threadsafe(node.loop.stop)
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()
