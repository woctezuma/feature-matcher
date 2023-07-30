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
 --output_dir matches --input_dir features \
 --numpy_matches matches.npy --numpy_similarity_scores scores.npy \
 --numpy_features fts.npy \
 --num_neighbors 10
```

## Example

For instance, to match features for images in the `balloon` dataset:

```bash
%cd /content
!git clone https://github.com/woctezuma/feature-extractor.git
%cd feature-extractor
%pip install --quiet -r requirements.txt

!wget https://github.com/matterport/Mask_RCNN/releases/download/v2.1/balloon_dataset.zip
!unzip -q balloon_dataset.zip

!python extract_fts.py --data_dir balloon

%cd /content
!git clone https://github.com/woctezuma/feature-matcher.git
%cd feature-matcher
%pip install --quiet -r requirements.txt

!python match_fts.py --input_dir /content/feature-extractor/features
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
