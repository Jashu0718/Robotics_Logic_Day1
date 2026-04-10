import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class PIDControllerNode(Node):
    def __init__(self):
        super().__init__('pid_controller_node')
        
        # 1. Subscriber: Listening for the robot's current position
        self.subscription = self.create_subscription(
            Float64, 
            '/current_position', 
            self.listener_callback, 
            10)
        
        # 2. Publisher: Telling the motor what force to apply
        self.publisher_ = self.create_publisher(Float64, '/motor_command', 10)
        
        # 3. PID Variables (Your Day 1 Logic)
        self.kp = 1.2
        self.ki = 0.5
        self.kd = 0.1
        self.setpoint = 10.0  # The target distance
        self.prev_error = 0.0
        self.integral = 0.0

        self.get_logger().info('--- PID Node Initialized ---')
        self.get_logger().info(f'Target Setpoint: {self.setpoint}')

    def listener_callback(self, msg):
        # This function runs EVERY TIME a new position is "heard"
        current_pos = msg.data
        error = self.setpoint - current_pos
        
        # The Core PID Math
        self.integral += error
        derivative = error - self.prev_error
        output = (self.kp * error) + (self.ki * self.integral) + (self.kd * derivative)
        
        # Create a ROS2 message and publish it
        cmd = Float64()
        cmd.data = output
        self.publisher_.publish(cmd)
        
        # Log the progress so we can see it in the terminal
        self.get_logger().info(f'POS: {current_pos:.2f} | ERROR: {error:.2f} | CMD: {output:.2f}')
        
        self.prev_error = error

def main(args=None):
    rclpy.init(args=args)
    node = PIDControllerNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
