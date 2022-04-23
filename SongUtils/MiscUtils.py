import torch
import numpy as np
import random

def load_weights(model, weights_path):
    ckpt = torch.load(weights_path, map_location='cpu')
    model_weights = ckpt['state_dict']
    model.load_state_dict(model_weights)
    return model

def setup_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.benchmark = False
    torch.backends.cudnn.deterministic = True
