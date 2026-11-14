import argparse
import json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', default='configs/eval.yaml')
    args = parser.parse_args()
    print(json.dumps({'recipe': 'vela-rerank-3b', 'config': args.config}))


if __name__ == '__main__':
    main()
