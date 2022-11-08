from abc import ABC, abstractmethod
import numpy as np
from robot.kuka_robot import KukaRobot
import pybullet as p

class ExtendKukaRobot(KukaRobot): # The kuka with 13 DoF
    
    # Initialize env
    def __init__(self, kuka_file="../data/robot/kuka_iiwa/model_3.urdf", collision_eps=0.5):
        super().__init__(kuka_file=kuka_file, collision_eps=collision_eps)   