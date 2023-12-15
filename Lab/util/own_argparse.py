import argparse

def get_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--wandb', action=argparse.BooleanOptionalAction, default=False, help="Usage of wandb, True or False"
    )

    parser.add_argument(
        '-r', '--learing_rate', type=int, default=1e-3, help='Model learning rate, default 1e-3'
    )

    parser.add_argument(
        '-p', '--early_stop_patience', type=int, default=10, help='# of early stop patience, defalut 10'
    )

    parser.add_argument(
        '-d', '-early_stop_delta', type=int, default=0.00001, help='Standard of early stop, default = 0.00001'
    )

    return parser