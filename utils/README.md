---
title: Submission Template
emoji: 🔥
colorFrom: yellow
colorTo: green
sdk: docker
pinned: false
---


# Random Baseline Model for Climate Disinformation Classification

## Model Description

This is a random baseline model for the Frugal AI Challenge 2024, specifically for the text classification task of identifying climate disinformation. The model serves as a performance floor, randomly assigning labels to text inputs without any learning.

### Intended Use

- **Primary intended uses**: Baseline comparison for climate disinformation classification models
- **Primary intended users**: Researchers and developers participating in the Frugal AI Challenge
- **Out-of-scope use cases**: Not intended for production use or real-world classification tasks

## Training Data

The model uses the QuotaClimat/frugalaichallenge-text-train dataset:
- Size: ~6000 examples
- Split: 80% train, 20% test
- 8 categories of climate disinformation claims

### Labels
0. No relevant claim detected
1. Global warming is not happening
2. Not caused by humans
3. Not bad or beneficial
4. Solutions harmful/unnecessary
5. Science is unreliable
6. Proponents are biased
7. Fossil fuels are needed

## Performance

### Metrics
- **Accuracy**: ~12.5% (random chance with 8 classes)
- **Environmental Impact**:
  - Emissions tracked in gCO2eq
  - Energy consumption tracked in Wh

### Model Architecture
The model implements a random choice between the 8 possible labels, serving as the simplest possible baseline.

## Environmental Impact

Environmental impact is tracked using CodeCarbon, measuring:
- Carbon emissions during inference
- Energy consumption during inference

This tracking helps establish a baseline for the environmental impact of model deployment and inference.

## Limitations
- Makes completely random predictions
- No learning or pattern recognition
- No consideration of input text
- Serves only as a baseline reference
- Not suitable for any real-world applications

## Ethical Considerations

- Dataset contains sensitive topics related to climate disinformation
- Model makes random predictions and should not be used for actual classification
- Environmental impact is tracked to promote awareness of AI's carbon footprint
```
