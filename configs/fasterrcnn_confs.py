from yacs.config import CfgNode as CN
_C = CN()
import numpy as np
_C.RANDOM_SEED = 44
_C.LOG_PATH = 'logs/train.log'
# DATA config
_C.DATA = CN()
_C.DATA.name = 'VOC'
_C.DATA.dir = 'dataset/VOC2007'
_C.DATA.width = 416
_C.DATA.height = 416
_C.DATA.classes = ['aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus',
           'car', 'cat', 'chair', 'cow', 'diningtable', 'dog', 'horse',
           'motorbike', 'person', 'pottedplant', 'sheep', 'sofa',
           'train', 'tvmonitor']
_C.DATA.num_classes = len(_C.DATA.classes)

# MODEL config
_C.MODEL = CN()
#_C.MODEL.name = 'faster_rcnn' # 'YOLOv3'
_C.MODEL.saved_path = 'trained_model/'
# cfg.MODEL.WEIGHTS ="detectron2://COCO-Detection/faster_rcnn_R_50_FPN_3x/137849458/model_final_280758.pkl"
_C.MODEL.pretrained_path = 'trained_model/darknet53_backbone_weights.pth'
_C.MODEL.ANCHORS = [np.array([10.,13.]),  np.array([16.,30.]),  np.array([33.,23.]),  np.array([30.,61.]),  np.array([62.,45.]),  np.array([59.,119.]),  np.array([116.,90.]),  np.array([156.,198.]),  np.array([373.,326.])]
_C.MODEL.STRIDES = [8, 16, 32]
_C.MODEL.ANCHORS_PER_SCLAE = 3


# train config
_C.TRAIN = CN()
_C.TRAIN.num_workers = 3
_C.TRAIN.optimizer = 'SGD'
_C.TRAIN.batch_size = 20
_C.TRAIN.lr = 1e-2
_C.TRAIN.weight_decay = 1e-4
_C.TRAIN.epochs = 20
_C.TRAIN.device = 'cuda:0'

def get_cfg_defaults():
  """Get a yacs CfgNode object with default values for my_project."""
  # Return a clone so that the defaults will not be altered
  # This is for the "local variable" use pattern
  return _C.clone()



