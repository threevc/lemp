import pybullet as p
from environment.dynamic_env import DynamicEnv
from robot.multi_robot.dual_kuka_robot import DualKukaRobot

class DualKukaEnv(DynamicEnv):

    def __init__(self, objects, robot_config=None):
        if robot_config is None:
            robot = DualKukaRobot()
        else:
            robot = DualKukaRobot(**robot_config)
        super(DualKukaEnv, self).__init__(objects, robot)

    def set_camera_angle(self):
        p.resetDebugVisualizerCamera(
            cameraDistance=2.,
            cameraYaw=25,
            cameraPitch=-20,
            cameraTargetPosition=[0.5, 0.5, 0.5])
