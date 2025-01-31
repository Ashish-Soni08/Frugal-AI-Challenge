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

## CHOSEN TASK: 📝 Detecting climate disinformation 📝: based on text from news articles

A major problem is the rise of climate related disinformation. A recent [scientific article](https://www.nature.com/articles/s41598-023-50591-6) estimated that **`14.8%`** of Americans do not believe in anthropogenic climate change. Much of this is probably due to disinformation. With climate change being one of the central threats to the wellbeing of our societies, this is a problem that must urgently be addressed.

Therefore, the task is to **Detect the Climate Disinformation in Newspaper articles.**

## Dataset

### Dataset Summary

A comprehensive collection of **~6000** `climate-related quotes and statements`, specifically `focused on identifying and categorizing climate disinformation narratives`. The dataset combines quotes and statements from various media sources, including television, radio, and online platforms, to help train models that can identify different types of climate disinformation claims. The labels are drawn from a simplified version of the [CARDS taxonomy](https://cardsclimate.com/) with only the **7** main labels.

```
@article{coan2021computer,
  title={Computer-assisted classification of contrarian claims about climate change},
  author={Coan, Travis G and Boussalis, Constantine and Cook, John and others},
  journal={Scientific Reports},
  volume={11},
  number={22320},
  year={2021},
  publisher={Nature Publishing Group},
  doi={10.1038/s41598-021-01714-4}
}
```

Coan, T.G., Boussalis, C., Cook, J. et al. Computer-assisted classification of contrarian claims about climate change. Sci Rep 11, 22320 (2021). https://doi.org/10.1038/s41598-021-01714-4

## Dataset Creation

### Curation and Annotation

This dataset was compiled to help identify and understand common climate disinformation narratives in media and public discourse. **`It serves as a tool for training models that can automatically detect and categorize climate disinformation claims.`**

The dataset combines data from two main sources curated by the QuotaClimat & Data For Good team.

1. [DeSmog](https://www.desmog.com/climate-disinformation-database/) climate disinformation database with extracted and annotated quotes with GPT4o-mini and manual validations

2. [FLICC dataset](https://huggingface.co/datasets/fzanartu/FLICCdataset) from the paper ["Detecting Fallacies in Climate Misinformation: A Technocognitive Approach to Identifying Misleading Argumentation"](https://arxiv.org/abs/2405.08254) by Francisco Zanartu, John Cook, Markus Wagner, Julian Garcia - re-annotated with GPT4o-mini and manual validations.

## Personal and Sensitive Information

The dataset contains publicly available statements and quotes. Care has been taken to focus on the claims themselves rather than personal information about individuals.

## Data Dictionary

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

## Labels and their Description

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

## Data Exploration

### Example Data Point

Here is an example data point from the dataset:

```json
{
    "__index_level_0__": 1109,
    "id": null,
    "label": "0_not_relevant",
    "language": "en",
    "quote": "Interesting to note that Oklahoma minimum temperatures in 2011 were in the bottom ten, including the coldest Oklahoma temperature ever recorded, -31F on February 10, 2011.",
    "source": "FLICC",
    "subsource": "CARDS",
    "url": "https://huggingface.co/datasets/fzanartu/FLICCdataset"
}
```

### Source Distribution

The dataset contains quotes from two main sources with the following distribution:

- **Desmog**: 4295 quotes
- **FLICC**: 1796 quotes

### Subsource Distribution

The dataset contains quotes from various subsources with the following distribution:

- **None**: 4295 quotes
- **CARDS**: 689 quotes
- **hamburg_test3**: 419 quotes
- **jintrain**: 192 quotes
- **hamburg_test2**: 172 quotes
- **hamburg_test1**: 107 quotes
- **jindev**: 78 quotes
- **Alhindi_train**: 63 quotes
- **jintest**: 39 quotes
- **Alhindi_dev**: 19 quotes
- **Alhindi_test**: 18 quotes

### Token Statistics

We added a `tokens` column to each data point, representing the number of tokens in the quote. Here are some statistics about the token counts:

- **Mean number of tokens**: ~49
- **Median number of tokens**: 38
- **Mode number of tokens**: 20

These statistics provide insights into the distribution of token counts across the dataset, helping us understand the typical length of quotes.

### Shortest and Longest Quotes

The dataset contains quotes with varying lengths. Here are the shortest and longest entries:

- **Shortest Quote**: This quote has only 3 tokens.
    ```json
    {
        "__index_level_0__": 277,
        "id": null,
        "label": "3_not_bad",
        "language": "en",
        "quote": "reefs are improving",
        "source": "FLICC",
        "subsource": "hamburg_test3",
        "url": "https://huggingface.co/datasets/fzanartu/FLICCdataset"
    }
    ```

- **Longest Quote**: This quote has 789 tokens.
    ```json
    {
        "__index_level_0__": 4243,
        "id": null,
        "label": "5_science_unreliable",
        "language": "en",
        "quote": "Hubris is a Greek word that means dangerously overconfident. Based on my research, hubris fairly describes our current response to the issue of climate change Here’s what many people believe One: The planet is warming catastrophically because of certain human behaviors Two: Thanks to powerful computers we can project what the climate will be like 20, 40, or even 100 years from now Three: That if we eliminate just one behavior, the burning of fossil fuels, we can prevent the climate from changing for as long we like Each of these presumptions—together, the basis of our hubris regarding the changing climate—is either untrue or so far off the mark as to be useless Yes, it’s true that the globe is warming, and that humans are exerting a warming influence upon it. But beyond that, to paraphrase a line from the classic movie The Princess Bride, ‘I do not think “The Science” says what you think it says. For example, government reports state clearly that heat waves in the US are now no more common than they were in 1900 Hurricane activity is no different than it was a century ago Floods have not increased across the globe over more than seventy years Greenland’s ice sheet isn’t shrinking any more rapidly today than it was 80 years ago Why aren’t these reassuring facts better known Because the public gets its climate information almost exclusively from the media And from a media perspective, fear sells ‘Things aren’t that bad’ doesn’t sell Very few people, and that includes journalists who report on climate news, read the actual science. I have. And what the data—the hard science—from the US government and UN Climate reports say is that… ‘things aren’t that bad. Nor does the public understand the questionable basis of all catastrophic climate change projections: computer modeling Projecting future climate is excruciatingly difficult. Yes, there are human influences, but the climate is complex. Anyone who says that climate models are “just physics” either doesn’t understand them or is being deliberately misleading. I should know: I wrote one of the first textbooks on computer modeling While modelers base their assumptions upon both fundamental physical laws and observations of the climate, there is still considerable judgment involved. And since different modelers will make different assumptions, results vary widely among different models Let’s just take one simple, but significant assumption modelers must make: the impact of clouds on the climate Natural fluctuations in the height and coverage of clouds have at least as much of an impact on the flows of sunlight and heat as do human influences. But how can we possibly know global cloud coverage say 10, let alone 50 years from now? Obviously, we can’t. But to create a climate model, we have to make assumptions. That’s a pretty shaky foundation on which to transform the world’s economy By the way, creating more accurate models isn’t getting any easier. In fact, the more we learn about the climate system, the more we realize how complex it is Rather than admit this complexity, the media, the politicians, and a good portion of the climate science community attribute every terrible storm, every flood, every major fire to ‘climate change.’ Yes, we’ve always had these weather events in the past, the narrative goes, but somehow ‘climate change’ is making everything ‘worse. Even if that were true, isn’t the relevant question, how much worse? Not to mention that ‘worse’ is not exactly a scientific term And how would we make it better For the alarmists, that’s easy: we get rid of fossil fuels Not only is this impractical—we get over 80% of the world’s energy from fossil fuels—it’s not scientifically possible. That’s because CO2 doesn’t disappear from the atmosphere in a few days like, say, smog. It hangs around for a really long time About 60 percent of any CO2 that we emit today will remain in the atmosphere 20 years from now, between 30 and 55 percent will still be there after a century, and between 15 and 30 percent will remain after one thousand years In other words, it takes centuries for the excess carbon dioxide to vanish from the atmosphere. So, any partial reductions in CO2 emissions would only slow the increase in human influences—not prevent it, let alone reverse it CO2 is not a knob that we can just turn down to fix everything. We don’t have that ability. To think that we do is… hubris Hubris leads to bad decisions A little humility and a little knowledge would lead to better ones I’m Steve Koonin, former Undersecretary for Science in the Obama Administration, and author of Unsettled: What Climate Science Tells Us, What It Doesn’t, and Why It Matters, for Prager University.",
        "source": "Desmog",
        "subsource": null,
        "url": "https://www.desmog.com/steve-koonin/"
    }
    ```

### Vocabulary Analysis

* **Vocabulary Size**: 30,807 words
* **Vocabulary for Words Appearing More Than Once**: 14,009 words
* **Vocabulary for Words Appearing More Than Three Times**: 7,035 words

### Label Distribution

The dataset contains the following distribution of labels:

- **0_not_relevant**: 1618
- **1_not_happening**: 741
- **2_not_human**: 702
- **3_not_bad**: 386
- **4_solutions_harmful_unnecessary**: 774
- **5_science_unreliable**: 801
- **6_proponents_biased**: 782
- **7_fossil_fuels_needed**: 287

![Label Distribution](/label_distribution.png)

### Data Preprocessing




## Training Data

The models use the 

- Size: ~6000 examples
- Split: 80% train, 20% test
- 8 categories of climate disinformation claims

### Getting Started

Example usage:

```python
from datasets import load_dataset
dataset = load_dataset("quotaclimat/frugalaichallenge-text-dataset")

print(next(iter(dataset['train'])))
```

### Licensing Information

The dataset is provided under the [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) license.