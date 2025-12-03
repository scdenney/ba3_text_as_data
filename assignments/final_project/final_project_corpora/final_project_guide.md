# Guide to information in the `final_project_corpora` Folder

This folder contains several curated datasets for your final Text-as-Data project/hackathon. Each dataset consists of:

  * **A primary CSV file** — the actual corpus you will analyze.  
  * **A Markdown (.md) documentation file** — your *data dictionary*, containing the dataset overview, context, variable definitions, and any additional information needed to interpret and work with the corpus.

The fodlers containing "interview" responses also include articles for refernce. You should **read the `.md` file first** before planning or doing any analysis.

---

## **Available Corpora for Analysis**

| Folder Name             | Data File (.csv)                     | Documentation File (.md)             | High-Level Topic                         | Possible Analysis                                                                                                           |
|------------------------|---------------------------------------|--------------------------------------|------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| `immigrant_interviews`  | **immigrant_interview.csv**           | **immigrant_interviews.md**           | **General Immigration Attitudes**         | Analyze vocabulary and reasoning in open-text responses explaining immigrant preference (e.g., language, economy, cultural fit). |
| `nkmigrants_interviews` | **nkmigrants_interviews.csv**         | **nkmigrants_interviews.md**          | **North Korean Migrant Integration**      | Study language and rationales supporting or rejecting North Korean migrants across type of integration (political, ecnomnic, social).         |
| `moon_twitter`          | **moon_twitter.csv**                  | **moon_twitter.md**                   | **President Moon Jae-in’s Twitter**       | Temporal analysis of political language, tone, and agenda setting across pre-presidency, transition, and presidency phases.   |
| `kr_newspapers`         | **korean_newspapers_twitter.csv**     | **korean_newspapers_twitter.md**      | **South Korean Newspapers on Twitter**    | Compare left–right media framing, agenda setting, and issue emphasis across six newspapers (Jul–Aug 2017).                   |
| `kyongje_yongu`         | **kjyg_reduced.csv**                  | **kjyg.md**                            | **North Korean Economic Discourse**       | Analyze ideological and economic narratives in a DPRK economics journal across leadership periods and economic eras.          |
| `president_speeches`    | **president_speeches_reduced.csv**  | **president_speeches.md**             | **South Korean Presidential Speeches**    | Examine long-run political rhetoric across administrations (Rhee → Moon), changes in issue emphasis, tone, and framing.      |

---

## **Suggested Workflow for Students**

1. **Select a Dataset:**  
   Choose one corpus that aligns with your substantive interests and research question.

2. **Read the Documentation:**  
   Open the `.md` file *before* examining the data. It explains context, variables, coding decisions, and features added to support analysis. Some files reference articles (included in the folder) or external websites for reference.

3. **Explore the CSV:**  
   Inspect the text and metadata. Use the documentation as your guide during cleaning, preprocessing, and analysis.

4. **Design Your Analysis:**  
   Decide what your project will focus on, including but perhaps not limited to the follwoing:
   - Sentiment or tone  
   - Topic modeling  
   - Comparative framing  
   - Temporal trends  
   - Classification or prediction  
   - Qualitative theme identification  

Your chosen dataset and its `.md` documentation provide everything you need to begin your final project.
