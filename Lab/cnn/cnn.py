import sys
import os
import torch
from torch import nn, optim
from datetime import datetime
from pathlib import Path

BASE_PATH = str(Path(__file__).resolve().parent.parent)
sys.path.append(BASE_PATH)

CURRENT_FILE_PATH = os.path.dirname(os.path.abspath(__file__))
CHECKPOINT_FILE_PATH = os.path.join(CURRENT_FILE_PATH, 'checkpoints')

if not os.path.isdir(CHECKPOINT_FILE_PATH):
    os.makedirs(CHECKPOINT_FILE_PATH)

from util.own_argparse import get_parser


def get_data():
    data = 0

    return data


def train(args, data):

    return 0


def test(args, data):

    return 0


def main(args):
    print("### Getting Data ###")
    data = get_data()
    print("### Done ###\n")

    print("### Training Start ###")
    train(args, data)
    print("### Training End ###\n")

    print("### Test Start ###")
    test(args, data)
    print("### Test End ###")

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    main(args)


