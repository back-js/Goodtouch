import argparse
from pathlib import Path
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

from PIL import Image
from psgan import Inference
from fire import Fire
import numpy as np

import faceutils as futils
from psgan import PostProcess
from setup import setup_config, setup_argparser
import os
os.chdir('C:/Users/s_ois/PycharmProjects/goodtouch/modules/PSGAN/')
def main(source_path,reference_path):
    parser = setup_argparser()

    parser.add_argument(
        "--speed",
        action="store_true",
        help="test speed")
    parser.add_argument(
        "--device",
        default="cpu",
        help="device used for inference")
    parser.add_argument(
        "--model_path",
        default="assets/models/기존G.pth",
        help="model for loading")

    args = parser.parse_args()
    config = setup_config(args)
    # Using the second cpu
    inference = Inference(
        config, args.device, args.model_path)
    postprocess = PostProcess(config)

    source = Image.open(source_path).convert("RGB")

    reference = Image.open(reference_path).convert("RGB")

        # Transfer the psgan from reference to source.
    image, face = inference.transfer(source, reference, with_face=True)
    source_crop = source.crop(
        (face.left(), face.top(), face.right(), face.bottom()))
    image = postprocess(source_crop, image)
    return image


