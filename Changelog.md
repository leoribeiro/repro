# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

## [v0.1.4](https://github.com/danieldeutsch/repro/releases/tag/v0.1.4) - 2022-01-29
### Changed
- Relaxed the `datasets` version requirement to match the GEM Metrics library
- Moved some dependencies into `dev-requirements.txt`

### Fixed
- Removed warnings that may happen if the Docker clients are not closed.

## [v0.1.3](https://github.com/danieldeutsch/repro/releases/tag/v0.1.3) - 2022-01-22
### Added
- Added [CLIPScore](models/hessel2021/Readme.md)
- Added a [QA SRL Parser](models/fitzgerald2018/Readme.md)
- Added [SUPERT](models/gao2020/Readme.md)
- Added [BLANC](models/vasilyev2020/Readme.md)
- Added [METEOR](models/denkowski2014/Readme.md)
- Added a role question generator from [Pyatkin et al. (2021)](models/pyatkin2021/Readme.md)
- Added using [Prism](models/thompson2020/Readme.md) as an MT model
- Added [COMET](models/rei2020/Readme.md)

### Fixed
- Fixed an error in [Lite3Pyramid](models/zhang2021/Readme.md) by updating to a newer version of the code.

## [v0.1.2](https://github.com/danieldeutsch/repro/releases/tag/v0.1.2) - 2021-10-07
### Changed
- Changed backend of Lite3Pyramid to use our own fork of the official repo with some modifications.

## [v0.1.1](https://github.com/danieldeutsch/repro/releases/tag/v0.1.1) - 2021-10-05
### Added
- Added [Benepar](models/kitaev2019/Readme.md)
- Added [Lite3Pyramid](models/zhang2021/Readme.md)
- Added [BARTScore](models/yuan2021/Readme.md)

### Changed
- Fixed silly variable name typo: `DOCKERHUB_REPRO` to `DOCKERHUB_REPO`

## [v0.1.0](https://github.com/danieldeutsch/repro/releases/tag/v0.1.0) - 2021-08-10
### Added
- Added [DAE](models/goyal2020/Readme.md)
- Adding [FactCC and FactCCX](models/kryscinski2019/Readme.md)
- Added utilities to remove empty inputs and insert values at specific indices
- Added automatically building and publishing model images
- Added a command to pull default Docker images for each model
- Added [SummaQA](models/scialom2019/Readme.md)
- Added [NUBIA](models/kane2020/Readme.md)
- Added [Prism](models/thompson2020/Readme.md)

### Changed
- BERTScore now returns 0 for its metrics if the input is empty. 
- BLEURT now returns the mean and max scores over the references.
- Changing Lewis et al. (2020) to download CNN/DM and XSum models by default
- Changing Liu et al. (2019) to download all models by default  

## [v0.0.3](https://github.com/danieldeutsch/repro/releases/tag/v0.0.3) - 2021-08-04
### Added
- Added [BLEURT](models/sellam2020/Readme.md)
- Added [BERTScore](models/zhang2020/Readme.md)
- Added [BLEU and SentBLEU](models/papineni2002/Readme.md)
- Added [QuestEval](models/scialom2021/Readme.md)
- Added [MoverScore](models/zhao2019/Readme.md)
- Added [FEQA](models/durmus2020/Readme.md)

### Changed
- Changed the QAEval interface to match other text generation metrics.
The backend was also changed to not rely on SacreROUGE.

## [v0.0.2](https://github.com/danieldeutsch/repro/releases/tag/v0.0.2) - 2021-07-30
### Added
- Added a `RecipeGenerationModel` class
- Added a [recipe generation model](models/dugan2020/Readme.md) from [Dugan et al. (2020)](https://arxiv.org/abs/2010.03070)
- Added a `TruecasingModel` class
- Added an RNN-based truecaser from [Susanto et al. (2016)](https://aclanthology.org/D16-1225/) based on an implementation [here](https://github.com/mayhewsw/pytorch-truecaser).
- Added the question-generation and question-answering models used in the [QAEval metric](https://arxiv.org/abs/2010.00490).
See [here](models/deutsch2021/Readme.md).
- Added [ROUGE](models/sacrerouge/Readme.md)
- Added `--predict-kwargs` arguments to the `predict` command
- Added support for running and writing evaluation metrics, for instance, ROUGE.
- Added a jsonl dataset reader (`JSONLinesDatasetReader`)
- Added the `SQuADv2Evaluation` metric
- Added the [BART-based sentence-guided models](models/dou2021/Readme.md) from [Dou et al. (2021)](https://arxiv.org/abs/2010.08014).
- Added the [LERC model](models/chen2020/Readme.md) from [Chen et al. (2020)](https://arxiv.org/abs/2010.03636)
- Added the [QAEval metric](models/deutsch2021/Readme.md)
- Adding a wrapper around the original Perl implementation of ROUGE.
See [here](models/lin2004/Readme.md)

### Changed
- Renamed the `--model-args`, `--dataset-reader-args`, and `--output-write-args` `predict` arguments to `--model-kwargs`, `--dataset-reader-kwargs`, and `--output-write-kwargs`.
- Renamed the `--output-file` argument in `predict` to `--output` to allow for output files or directories.

## [v0.0.1](https://github.com/danieldeutsch/repro/releases/tag/v0.0.1) - 2021-07-22
### Added
- Initial prototype of the library with `setup` and `predict` commands as well as implementations of [Gupta et al. (2020)](models/gupta2020/Readme.md), [Lewis et al. (2020)](models/lewis2020/Readme.md), and [Liu & Lapata (2019)](models/liu2019/Readme.md).
