import threading
import asyncio
import rclpy
from rclpy.node import Node
from robot_sim_interfaces.srv import TaskExecutorService
from fastapi import FastAPI
from  pydantic  import  BaseModel 
import uvicorn

app = FastAPI()

class ActuationProcessorNode(Node):
    def __init__(self):
        super().__init__('actuation_processor_node')

        self.task_executor_client = self.create_client(TaskExecutorService, 'task_executor_service')
        while not self.task_executor_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for task_executor_service...')

    async def call_service(self, task):
        request = TaskExecutorService.Request()
        request.task = task
        future = self.task_executor_client.call_async(request)
        await future
        return future.result()

class ServiceInput(BaseModel):
    task: str

@app.post("/obligation/execute")
async def call_service(request: ServiceInput):
    if node is None:
        return {"error": "ROS node not initialized"}
    response = await node.call_service(request.task)
    return {
        "result": response.result
    }

def ros2_thread():
    global node
    rclpy.init()
    node = ActuationProcessorNode()
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
    uvicorn.run(app, port=8001, log_level='info')

if __name__ == "__main__":
    main()