import argparse
from argparse import Namespace
import yaml

class Params:
    def __init__(self, yaml_path):
        self.params = yaml.safe_load(open(yaml_path).read())

    def __getattr__(self, item):
        return self.params.get(item, None)

class BaseArgs(object):
    def __init__(self, yaml_path):
        base_cfg = self.get_base_args()
        yaml_params = Params(yaml_path)
        self.cfg = self.merge_args(base_cfg, yaml_params)
        
    def get_base_args(self):
        parser = argparse.ArgumentParser()
        # training procedure
        parser.add_argument("--epochs", type=int, default=100)
        parser.add_argument("--batchSize", type=int, default=64)

        # optimizing procedure
        parser.add_argument("--optimizer-type", type=str, choices=['sgd', 'adam'], default='sgd')
        parser.add_argument("--lr", type=float, default=0.001)
        parser.add_argument("--weight-decay", type=float, default=0.)

        # save logs and results
        parser.add_argument("--log-freq", type=int, default=100)
        parser.add_argument("--log-level", type=str, choices=['INFO', 'DEBUG'], default='DEBUG')
        parser.add_argument("--summary-path", type=str, default="./summary")
        parser.add_argument("--model-path", type=str, default="./saved_model")

        # Misc
        parser.add_argument("--device", type=str, default="cuda:0")
        base_cfg = parser.parse_args()
        return base_cfg

    def get_customized_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--test", type=str, default="testing")
        customized_cfg = parser.parse_args()
        return customized_cfg
    
    def merge_args(self, base_cfg, customized_cfg):
        for k, v in customized_cfg.params.items():
            base_cfg.k = v
        return base_cfg
    
    def get_args(self):
        return self.cfg


if __name__ =="__main__":
    Args = BaseArgs(yaml_path="yml_config.yml")
    cfg = Args.get_args()
    for k, v in vars(cfg).items():
        print(k, v)