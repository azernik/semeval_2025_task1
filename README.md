# semeval_2025_task1
- Code is provided as colab notebooks. 
- Data will be pulled in from our (public) Google drive and model definitions and weights are downloaded from online sources. 
- Notebooks perform any required training and evaluation. 
- An OpenAI API key is required to interact with GPT. I have included a key with a limit of $10, which should be more than enough to run everything a couple of times.

## Prompting GPT, experiments with contrastive loss models
- `admire_experiments_v2.ipynb`
- Prompting GPT for definitions and classification of target phrases. 
- Using these definitions as input to contrastive loss models (CLIP, ALIGN, OpenCLIP) and evaluate performance. 

## Fine tuning OpenCLIP
- `tuning_open_clip.ipynb`
- Pulls in results of prompting and fine tunes for the SemEval task applied to these different text input. 

## Analysis and plots
- `admire_results_analysis.ipynb`

## Type classifier
- `sentence_type_classifier.ipynb`
- To fine tune BERT using MAGPIE dataset and test on SemEval data. 

## Text to text experiments 
- `shubham_admire_experiments.ipynb`

## Results
- `experiment_results.csv` contains summarized results (accuracy, spearman rank, weighted accuracy) from all experiment configurations.
- `combined_predictions.csv` contains detailed results for every sample for all experiment configurations. 
