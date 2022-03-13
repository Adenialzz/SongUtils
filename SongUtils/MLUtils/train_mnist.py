import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import datasets, transforms
import os
import sys
import argparse
from BaseTrainers import BaseTrainer, BaseDistTrainer, init_dist
from BaseArgs import YamlParams, get_dist_base_parser, get_base_parser

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.conv2_drop = nn.Dropout2d()
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
        x = x.view(-1, 320)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)


def get_args():
    parser = get_dist_base_parser()
    parser.add_argument("--dataset-name", type=str, default="mnist")
    cfg = parser.parse_args()
    return cfg

def main(cfg):
    # os.environ['CUDA_VISIBLE_DEVICES'] = cfg.gpu_id
    # torch.distributed.init_process_group(backend="nccl")
    # local_rank = torch.distributed.get_rank()
    # torch.cuda.set_device(local_rank)
    init_dist(cfg.gpu_id)

    pipeline = transforms.Compose([
            transforms.ToTensor(),
    ])
    train_set = datasets.MNIST("../data", train=True, transform=pipeline, download=True)
    val_set = datasets.MNIST("../data", train=False, transform=pipeline, download=True)
    dataset_list = [train_set, val_set]
    model = Net()
    mnist_trainer = BaseDistTrainer(cfg, model, dataset_list, metrics_list=['loss', 'acc'])
    # mnist_trainer = BaseTrainer(cfg, model, dataset_list, metrics_list=['loss', 'acc'])
    mnist_trainer.forward()


if __name__ == "__main__":
    # cfg = YamlParams(sys.argv[1])
    cfg = get_args()
    main(cfg)