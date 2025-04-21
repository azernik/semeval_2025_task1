# SemEval Idiom Interpretation Project

## SemEval_Admire_UCSC.ipynb

This notebook contains code for processing and analyzing idioms for the SemEval task:

* Loads and preprocesses datasets (test or extended)
* Classifies sentence_type as *literal* or *idiomatic*
* Implements two prompting strategies to generate definitions for idioms
* Ranks images for examples using CLIP, OpenCLIP, ALIGN
* Creates submission files for evaluation

## prompting_outputs

The `prompting_outputs` directory contains the outputs for sentence type classification and idiom definition.

Results are organized by dataset (test vs. extended).