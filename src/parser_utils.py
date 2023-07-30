import argparse


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output_dir",
        type=str,
        default='matches',
        help="The path to the output folder where matches and similarity scores will be saved.",
    )
    parser.add_argument(
        "--input_dir",
        type=str,
        default="features",
        help="The path to the input folder where features are stored.",
    )
    parser.add_argument(
        "--numpy_matches",
        type=str,
        default="matches.npy",
        help="An output file with the matches in NumPy format.",
    )
    parser.add_argument(
        "--numpy_similarity_scores",
        type=str,
        default="scores.npy",
        help="An output file with the similarity scores in NumPy format.",
    )
    parser.add_argument(
        "--numpy_features",
        type=str,
        default="fts.npy",
        help="An input file with the features in NumPy (.npy) or PyTorch (.pth) format.",
    )
    parser.add_argument(
        "--num_neighbors",
        type=int,
        default=10,
        help="Desired number of nearest neighbors to retrieve.",
    )

    return parser
