---
license: cc-by-nc-4.0
task_categories:
- text-classification
language:
- en
pretty_name: Frugal AI Challenge 2025 - Text - Climate Disinformation
size_categories:
- 1K<n<10K
dataset_info:
  features:
  - name: quote
    dtype: string
  - name: label
    dtype: string
  - name: source
    dtype: string
  - name: url
    dtype: string
  - name: language
    dtype: string
  - name: subsource
    dtype: string
  - name: id
    dtype: 'null'
  - name: __index_level_0__
    dtype: int64
  splits:
  - name: train
    num_bytes: 1966375
    num_examples: 4872
  - name: test
    num_bytes: 471849
    num_examples: 1219
  download_size: 1270522
  dataset_size: 2438224
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
---

# [Frugal-AI-Challenge](https://frugalaichallenge.org/)

## Goal

To encourage both academic and industry actors to keep `efficiency` in mind when deploying **AI** models. 

## The Challenges

By tracking both `energy consumption` and `performance` for different **AI** for `climate` tasks, we can incentive **frugality** in AI deployment while also addressing real-world challenges.

We have chosen *three* tasks across *three* modalities, all of which are useful in the `global fight` against the `climate crisis`:

- **Detecting Climate Disinformation**
- **Classifying regions at risk of wildfires**
- **Detecting Illegal Deforestation**

We will evaluate both `performance` and `efficiency` on each of the datasets, based on the real-world constraints of each `task` and the `energy` used.

The datasets for each task are hosted on the [Hugging Face organization page](https://huggingface.co/collections/frugal-ai-challenge/frugal-ai-challenge-tasks-673dd5ee724c6659a5b42443) - you can download them and start training models!



## Environment Setup

```bash
python -V
# Output: Python 3.12.1
```

```bash
# create a environment named -> samba-ai
python -m venv frugal-ai
```

```bash
# activate the environment
source frugal-ai/bin/activate
```

```bash
# deactivate the virtual environment
deactivate
```

```bash
# create a Jupyter Notebook kernel
pip install jupyter ipykernel
```

```bash
# add the virtual environment as a kernel for the jupyter notebook
python -m ipykernel install --user --name=frugal-ai --display-name="Py3.12-frugal-ai"
```

```bash
# verify kernel installation
jupyter kernelspec list
```

```bash
# If needed
jupyter kernelspec uninstall frugal-ai
```

```bash
# A python package estimating the hardware energy consumption (CPU + GPU + RAM) of your program.

pip install codecarbon
```

## CHOSEN TASK: 📝 Detecting climate disinformation 📝: based on text from news articles

A major problem is the rise of climate related disinformation. A recent [scientific article](https://www.nature.com/articles/s41598-023-50591-6) estimated that **`14.8%`** of Americans do not believe in anthropogenic climate change. Much of this is probably due to disinformation. With climate change being one of the central threats to the wellbeing of our societies, this is a problem that must urgently be addressed.

Therefore, the task is to **Detect the Climate Disinformation in Newspaper articles.**

## Dataset

### Dataset Summary

A comprehensive collection of **~6000** `climate-related quotes and statements`, specifically `focused on identifying and categorizing climate disinformation narratives`. The dataset combines quotes and statements from various media sources, including television, radio, and online platforms, to help train models that can identify different types of climate disinformation claims. The labels are drawn from a simplified version of the [CARDS taxonomy](https://cardsclimate.com/) with only the **7** main labels.

## Dataset Creation

### Curation and Annotation

This dataset was compiled to help identify and understand common climate disinformation narratives in media and public discourse. **`It serves as a tool for training models that can automatically detect and categorize climate disinformation claims.`**

The dataset combines data from two main sources curated by the QuotaClimat & Data For Good team.

1. [DeSmog](https://www.desmog.com/climate-disinformation-database/) climate disinformation database with extracted and annotated quotes with GPT4o-mini and manual validations

2. [FLICC dataset](https://huggingface.co/datasets/fzanartu/FLICCdataset) from the paper ["Detecting Fallacies in Climate Misinformation: A Technocognitive Approach to Identifying Misleading Argumentation"](https://arxiv.org/abs/2405.08254) by Francisco Zanartu, John Cook, Markus Wagner, Julian Garcia - re-annotated with GPT4o-mini and manual validations.

### Data Dictionary

| Field Name          | Data Type | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Possible Values/Information                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Example Value                                                                                                                                                                                                                                                                                                                                                                                      |
|----------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `quote`              | string    | The actual quote or statement related to climate change. This field contains the textual data that is labeled for climate disinformation.                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 6091 unique values (matches the number of rows in the dataset). These quotes are drawn from various media sources, including television, radio, and online platforms.                                                                                                                                                                                                                                                                                                                                                                                        | "There is clear, compelling evidence that many of the major conclusions of the IPCC, your new religions constantly-changing Holy Book, are based on evidence that has been fabricated. The hockey stick graph that purported to abolish the mediaeval warm period is just one example."                                                                                                       |
| `label`              | string    | The category of the climate-related claim. This field represents the type of climate disinformation or related claim present in the `quote`. The labels are based on a simplified version of the CARDS taxonomy.                                                                                                                                                                                                                                                                                                                                                                       | **Possible Values:** `5_science_unreliable`, `1_not_happening`, `4_solutions_harmful_unnecessary`, `0_not_relevant`, `6_proponents_biased`, `7_fossil_fuels_needed`, `2_not_human`, `3_not_bad`. These string labels correspond to the numerical categories 0-7 defined in the Label Descriptions below.                                                                                                                                                                                                                                                                                       | "5_science_unreliable"                                                                                                                                                                                                                                                                                                                                                                         |
| `source`             | string    | The source of the quote or claim. This indicates the origin of the quote within the dataset.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | **Possible Values:** `FLICC`, `Desmog`. <br> - **FLICC:**  Quotes sourced from the FLICC dataset, which focuses on detecting fallacies in climate misinformation. This data was re-annotated for this challenge.<br> - **Desmog:** Quotes sourced from the DeSmog climate disinformation database, which were extracted and annotated for this challenge.                                                                                                                                                                                                                                                           | "FLICC"                                                                                                                                                                                                                                                                                                                                                                                          |
| `url`                | string    | The URL associated with the quote, pointing to the original source or a relevant page where the quote was found.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 780 unique values. These URLs represent a variety of sources, including news articles, websites, and potentially social media platforms. Note that external links may become inactive over time.                                                                                                                                                                                                                                                                                                                                                                        | "https://huggingface.co/datasets/fzanartu/FLICCdataset"                                                                                                                                                                                                                                                                                                                                          |
| `language`           | string    | The language of the quote.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | **Possible Value:** `"en"` (English). All quotes in this dataset are in English.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | "en"                                                                                                                                                                                                                                                                                                                                                                                           |
| `subsource`          | string    | A more specific sub-source or category within the main `source`. This can indicate the specific dataset or split from which the quote originated or a detail about the annotation process.                                                                                                                                                                                                                                                                                                                                                                                             | **Possible Values:** `CARDS`, `hamburg_test1`, `hamburg_test3`, `jindev`, `jintrain`, `hamburg_test2`, `Alhindi_train`, `jintest`, `Alhindi_dev`, `Alhindi_test`, `None`. These values likely correspond to different subsets or annotation stages from the original data sources or specific test sets created for the challenge.                                                                                                                                                                                                                                                              | "CARDS"                                                                                                                                                                                                                                                                                                                                                                                          |
| `id`                 | null      | An identifier for the quote.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | This field is consistently `null`, indicating that unique identifiers for each quote were not included in this version of the dataset.                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `None`                                                                                                                                                                                                                                                                                                                                                                                         |
| `__index_level_0__` | int64     | The original index or row number in the dataset. This likely represents the row number in the original data file before any processing or splitting.                                                                                                                                                                                                                                                                                                                                                                                                                                       | 6091 unique values (matches the number of rows in the dataset). This field likely serves as an internal index or identifier within the dataset structure.                                                                                                                                                                                                                                                                                                                                                                                                                               | 0                                                                                                                                                                                                                                                                                                                                                                                            |

#### Labels and their Description

| Label | Description                                                                                                                                                                                                                                                        | Example Keywords/Concepts                                                                                                                                                                                                                                                          |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **0_not_relevant** | No relevant claim detected or claims that don't fit other categories.                                                                                                                                                                                | General discussion, unrelated topics, acknowledgments, procedural statements.                                                                                                                                                                                                    |
| **1_not_happening** | Claims denying the occurrence of global warming and its effects.                                                                                                                                                                                      | Global warming is not happening, climate change is a hoax, no warming, it's getting colder, no melting ice, no sea level rise, extreme weather is normal, cold weather proves no warming.                                                                                    |
| **2_not_human**   | Claims denying human responsibility in climate change.                                                                                                                                                                                               | Greenhouse gases from humans are not causing climate change, natural cycles, solar activity, volcanoes are the cause, it's a natural phenomenon.                                                                                                                                   |
| **3_not_bad**     | Claims minimizing or denying negative impacts of climate change.                                                                                                                                                                                          | The impacts of climate change will not be bad, might even be beneficial, it's not a threat, it's exaggerated, plants will benefit from more CO2, warmer temperatures are good.                                                                                                |
| **4_solutions_harmful_unnecessary** | Claims against climate solutions.                                                                                                                                                                                                     | Climate solutions are harmful, unnecessary, expensive, ineffective, renewable energy won't work, electric vehicles are bad, carbon taxes are a scam, the Green New Deal is a disaster, it's too late to do anything.                                                               |
| **5_science_is_unreliable** | Claims questioning climate science validity.                                                                                                                                                                                                   | Climate science is uncertain, unsound, unreliable, biased, flawed models, scientists are manipulating data, it's just a theory, the data is wrong, historical records don't support it, consensus is not science.                                                                 |
| **6_proponents_biased** | Claims attacking climate scientists and activists.                                                                                                                                                                                               | Climate scientists are alarmist, biased, wrong, hypocritical, corrupt, politically motivated, they are in it for the money, activists are exaggerating, it's a political agenda.                                                                                                   |
| **7_fossil_fuels_needed** | Claims promoting fossil fuel necessity.                                                                                                                                                                                                          | We need fossil fuels for economic growth, prosperity, to maintain our standard of living, renewable energy is not reliable, fossil fuels are essential, they provide cheap energy, transitioning away from fossil fuels will hurt the economy. 

## Training Data

The models use the QuotaClimat/frugalaichallenge-text-train dataset:

- Size: ~6000 examples
- Split: 80% train, 20% test
- 8 categories of climate disinformation claims

## Personal and Sensitive Information

The dataset contains publicly available statements and quotes. Care has been taken to focus on the claims themselves rather than personal information about individuals.