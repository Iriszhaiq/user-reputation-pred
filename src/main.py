"""Stack Exchange - User Reputation Prediction."""


import argparse


def parse_args():
    """Parse parameters."""
    parser = argparse.ArgumentParser()

    # directory
    parser.add_argument('--traindata', type=str, default="../data/Reputation_prediction_data_train.txt", help='path to dataset')
    parser.add_argument('--trainlabel', type=str, default="../data/Reputation_prediction_labels_train.txt", help='path to training labels')

    # hyperparameters settings
    parser.add_argument('--lr', type=float, default=0.0001, help='learning rate')
    parser.add_argument('--weight_decay', type=float, default=1e-5, help='weight decay (L2 penalty)')

    parser.add_argument('--epochs', type=int, default=120, help='number of epochs to train without generator')
    parser.add_argument('--start_epoch', type=int, default=0, help='pre-trained epochs')
    parser.add_argument('--batch_size_train', type=int, default=128, help='training set input batch size')
    parser.add_argument('--batch_size_test', type=int, default=128, help='test set input batch size')

    # training settings
    parser.add_argument('--resume', type=bool, default=False, help='whether re-training from ckpt')
    parser.add_argument('--cuda', type=bool, default=True, help='whether training using cudatoolkit')

    # parse the arguments
    args = parser.parse_args()

    return args


def main():
    """Main pipeline for User Reputation Prediction."""
    pass


if __name__ == '__main__':
    main()
