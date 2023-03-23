from omni.isaac.orbit_envs.isaac_env import IsaacEnv


class SimpleSurgEnv(IsaacEnv):
    def __init__(self, cfg, headless: bool = False):
        self.cfg = cfg


        self._observation_man
