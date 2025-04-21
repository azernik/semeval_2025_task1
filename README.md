# SemEval Idiom Interpretation Project

## SemEval_Admire_UCSC.ipynb

This notebook contains code for processing and analyzing idioms for the SemEval task:

* **Data Processing**: Loads and preprocesses datasets (test or extended) containing idioms, sentences, and associated images
* **Sentence Type Classification**: Uses GPT-4 to classify sentences as either literal or idiomatic usage of target phrases
* **Idiom Definition Generation**: Implements two different prompting strategies to generate definitions for idiomatic phrases
* **Multimodal Model Evaluation**: Evaluates several vision-language models (CLIP, OpenCLIP, ALIGN) on their ability to rank images based on idiom interpretations
* **Results Export**: Exports classification results, definitions, and model predictions for further analysis

## prompting_outputs

The `prompting_outputs` directory contains the outputs for sentence type classification and idiom definition. Results are organized by dataset (test/extended).

* **Classification Files**: TSV files containing sentence type classifications (literal vs. idiomatic) for each idiom. Voting results are also included.
* **Definition Files**: CSV files with definitions generated for each idiom using different prompting approaches.
  * **exp4**: ...
  * **exp5**: ...
  * **exp6**: See `prompt_exp6_idiomatic` in notebook
  * **exp7**: See `prompt_exp7_idiomatic` in notebook
