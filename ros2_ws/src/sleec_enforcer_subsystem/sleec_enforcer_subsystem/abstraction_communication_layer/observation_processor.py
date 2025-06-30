import threading
import asyncio
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from fastapi import FastAPI
import uvicorn

app = FastAPI()

class ObservationProcessorNode(Node):
    def __init__(self):
        super().__init__('observation_processor_node')

        self.create_subscription(String, 'sensor_data', self.listener_callback, 10)
        self.latest_message = {"data": None}

    def listener_callback(self, msg):
        self.get_logger().info(f'Received: {msg.data}')
        self.latest_message["data"] = msg.data

# FastAPI edpoints
@app.get("/probe/latest_data")
async def get_last_data():
    if node.latest_message["data"] is None:
        return {"message": "No data received yet."}
    return {"latest_data": node.latest_message["data"]}

def ros2_thread():
    global node
    rclpy.init()
    node = ObservationProcessorNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

def main(args=None):
    spin_thread = threading.Thread(target=ros2_thread, daemon=True)
    spin_thread.start()
    uvicorn.run(app, port=8000, log_level='info')

if __name__ == "__main__":
    main()
