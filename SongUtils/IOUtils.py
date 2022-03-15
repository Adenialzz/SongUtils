import torch
import torchvision.transforms as transforms
import numpy as np
from PIL import Image
import cv2
import os
import os.path as osp

def readByLines(file_name, strip=True):
    with open(file_name, 'r') as f:
        f_lines = f.readlines()
    if strip:
        return [line.strip() for line in f_lines]
    else:
        return f_lines

def readSingleImagePIL(image_path, rgb=False):
    img = Image.open(image_path)
    if rgb:
        return img.convert("RGB") 
    else:
        return img

def readSingleImageCV2(image_path):
    img = cv2.imread(image_path)
    img = img[:, :, ::-1]       # bgr 2 rgb
    return img

def readTensorImage(image_path, expand=False, through='pil', transform=None):
    if through == 'pil':
        img = readSingleImagePIL(image_path)
        img_tensor = pil2tensor(img, transform)
    elif through == 'opencv':
        arr = readSingleImageCV2(image_path)
        img_tensor = cv2tensor(arr.copy())
    else:
        raise KeyError

    if expand:
        return img_tensor.unsqueeze(dim=0)
    else:
        return img_tensor

def readBatchImages(images_dir, rgb=False):
    images_list = os.listdir(images_dir)
    for image_name in imaegs_list:
        image_path = osp.join(images_dir, image_name)
    # TODO

def cv2tensor(arr, transform=None):
    if transform is not None:
        return transform(arr)
    else:
        arr = arr.transpose(2, 0, 1).astype(np.float32) / 255.  # HWC 2 CHW && normalize
        img_tensor = torch.from_numpy(arr)
        return img_tensor

def tensor2cv(img_tensor, convert_rgb=False):
    arr = img_tensor.detach().permute(1, 2, 0).numpy() * 255.
    if convert_rgb:
        return arr[:, :, ::-1]
    else:
        return arr

def pil2tensor(img, transform=None):
    if transforms is not None:
        img_tensor = transform(img)
    else:
        img_tensor = transforms.functional.to_tensor(img)
    return img_tensor

def tensor2pil(img_tesnor):
    img = transforms.functional.to_pil_image(img_tensor)
    return img

def getTransforms(crop=None, resize=None):
    t = []
    if crop is not None:
        t.append(transforms.Crop(crop))
    if resize is not None:
        t.append(transforms.Resize(resize))

    return transforms.Compose(t)


class SongImage(object):
    # TODO
    def __init__(self, src, rgb=False):
        if isinstance(src, np.ndarray):
            self.cv = src if rgb else src[:, :, ::-1]   # H, W, C
        elif isinstance(src, PIL.JpegImagePlugin.JpegImageFile):
            self.pil = src if rgb else src.convert('rgb')
        elif isinstance(src, torch.Tensor):
            if src.shape != 3:
                print("Batched Tensor NOT Supported yet, SongImage Initialization Failed.")
            self.tensor = src
        elif isinstance(src, str):
            if os.path.exists(src):
                self.pil = Image.open(src).convert('rgb')
            else:
                print(f"Error: File Not Exists: {src}, SongImage Initialization Failed.")
        else:
            print(f"Error: Unknown Initialization Type: {type(src)}, SongImage Initialization Failed.")
    
    def pil2cv(self):
        pass
    
    def pil2tensor(self, transforms=None):
        if transform is not None:
            return transform(self.pil)
        else:
            return transform.functional.to_tensor(self.pil)
    
    def cv2tensor(self, transform=None):
        pass

    def tensor2pil(self):
        return transforms.functional.to_pil_image(self.tensor)
    
    def tensor2cv(self):
        pass




if __name__ == "__main__":
    image_path = "/ssd1t/song/Datasets/AVA/shortEdge256/125.jpg"
    ten = readTensorImage(image_path, through="opencv")
    img = tensor2cv(ten, True)
    cv2.imwrite("test.jpg", img)

