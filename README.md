# :dart: Feature Matcher

This repository contains Python code to match representation vectors, using cosine similarity.

## Requirements

-   Install the latest version of [Python 3.X][python-download-url].
-   Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

Run:
```bash
!python match_fts.py \
 --output_dir matches --output_filename matches.npy \
 --input_dir features --input_filename fts.npy \
 --num_neighbors 10
```

## References

-   A [feature extractor][feature-extractor] for Github repositories which include a `hubconf.py` file.
-   [`match-steam-banners`][github-match-steam-banners]: retrieve games with similar store banners.
-   [`steam-DINOv2`][github-match-with-dinov2]: retrieve games with similar store banners, using Meta AI's DINOv2.

<!-- Definitions -->

[python-download-url]: <https://www.python.org/downloads/>
[feature-extractor]: <https://github.com/woctezuma/feature-extractor>
[github-match-steam-banners]: <https://github.com/woctezuma/match-steam-banners>
[github-match-with-dinov2]: <https://github.com/woctezuma/steam-DINOv2>
[colab-badge]: <https://colab.research.google.com/assets/colab-badge.svg>
