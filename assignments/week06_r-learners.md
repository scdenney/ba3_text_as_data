---
layout: default
title: Week 6 Assignment (R Track)
---

# Optional Add-On (R Programming Track): Full LDA Assignment  
## (Top Terms • Topic–Document Distribution • Word Probabilities)

This task mirrors the ODM LDA exercise but uses R to extract full statistical results.  
You will generate:
1. Top terms per topic  
2. Topic–document distribution (θ)  
3. Topic–word probabilities (φ)  
4. Coherence scores for multiple values of k  
5. A short comparison of k options  

---

## 1. Fit LDA models in R

Use the same `nikh__sentences.csv` file as in ODM.  
After preprocessing and creating a DTM, run LDA for at least three values of k:

    library(topicmodels)

    lda_k4 <- LDA(dtm, k = 4, control = list(seed = 123))
    lda_k6 <- LDA(dtm, k = 6, control = list(seed = 123))
    lda_k8 <- LDA(dtm, k = 8, control = list(seed = 123))

Pick one model to use for extraction (usually the best by coherence).

---

## 2. Compute coherence scores for choosing k

Use the `ldatuning` package:

    library(ldatuning)

    result <- FindTopicsNumber(
      dtm,
      topics = c(4, 6, 8),
      metrics = c("CaoJuan2009", "Arun2010", "Griffiths2004", "Deveaud2014"),
      method = "Gibbs",
      control = list(seed = 123),
      verbose = TRUE
    )

    FindTopicsNumber_plot(result)

Export this plot as `coherence_plot.png`.

---

## 3. Extract top terms per topic

    terms(lda_k6, 15)    # or whichever model you selected

Save the output as `lda_r_top_terms.txt`.

---

## 4. Extract the topic–document distribution (θ)

    theta <- posterior(lda_k6)$topics
    head(theta)

    write.csv(theta, "lda_r_topic_distribution.csv")

---

## 5. Extract the topic–word probabilities (φ)

    phi <- posterior(lda_k6)$terms
    head(phi)

    write.csv(phi, "lda_r_word_probabilities.csv")

---

## 6. Visualize the “Two Pillars of LDA”

Produce:
- a plot of θ for one document (`theta_example.png`)
- a bar plot of φ for one topic (`phi_example.png`)

These correspond to the Two Pillars slide.

---

## 7. Reflection (README.md)

Write 4–6 sentences:
- Which k values you tried  
- What the coherence plot suggested  
- Which k you think is most interpretable  
- Whether your preferred k matches the statistical suggestion  
- Whether R topics resemble your ODM topics  

---

## Deliverables

Place into `/week06/r_track/`:

```
coherence_plot.png
lda_r_top_terms.txt
lda_r_topic_distribution.csv
lda_r_word_probabilities.csv
theta_example.png
phi_example.png
README.md
```

---

## Notes

- θ = document–topic mixture  
- φ = topic–word probabilities (true p(w | k))  
- ODM shows relative weights; R gives normalized distributions  
- Differences between ODM and R are expected  
