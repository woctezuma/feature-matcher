import json
from pathlib import Path

import numpy as np
import torch

from src.match_utils import match_all
from src.numpy_utils import save_as_numpy_file
from src.parser_utils import get_parser

NUMPY_FILE_EXTENSION = ".npy"


def main():
    params = get_parser().parse_args()
    print(f"__log__:{json.dumps(vars(params))}")

    print('>>> Creating output directory...')
    Path(params.output_dir).mkdir(parents=True, exist_ok=True)

    print('>>> Loading features...')
    fname = Path(params.input_dir) / params.feature_filename
    if str(fname).lower().endswith(NUMPY_FILE_EXTENSION):
        embeddings = np.load(fname)
    else:
        embeddings = torch.load(fname).numpy()

    print('>>> Matching features...')
    scores, indices = match_all(embeddings, params.num_neighbors)

    print('>>> Saving similarity scores...')
    fname = Path(params.output_dir) / params.numpy_similarity_scores
    save_as_numpy_file(fname, scores, np.float16)

    print('>>> Saving matches...')
    # NB: uint16 is not ok (max value: ~ 65 k), but uint32 is ok (max value: ~ 4 billions).
    fname = Path(params.output_dir) / params.numpy_matches
    save_as_numpy_file(fname, indices, np.uint32)


if __name__ == '__main__':
    main()
