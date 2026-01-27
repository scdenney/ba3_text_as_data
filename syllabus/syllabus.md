---
layout: default
title: Syllabus
---

<div class="page-layout">
  <aside class="page-sidebar">
    <div class="page-sidebar-inner">
      <h2 class="page-sidebar-title">On this page</h2>
      <nav class="page-toc">
        <ul>
          <li><a href="#expanded-description">Expanded Description</a></li>
          <li><a href="#tutorials">Tutorials</a></li>
          <li>
            <a href="#assignments">Assignments</a>
            <ul>
              <li><a href="#format">Format</a></li>
              <li><a href="#submission">Submission</a></li>
            </ul>
          </li>
          <li><a href="#optional-r-programming">Optional: R Programming</a></li>
          <li><a href="#github-repository">GitHub Repository</a></li>
          <li><a href="#corpus-overview">Corpus Overview</a></li>
          <li>
            <a href="#weekly-outline">Weekly Outline</a>
            <ul>
              <li><a href="#week-1">Week 1 (Oct. 10)</a></li>
              <li><a href="#week-2">Week 2 (Oct. 17)</a></li>
              <li><a href="#week-3">Week 3 (Oct. 24)</a></li>
              <li><a href="#week-4">Week 4 (Nov. 7)</a></li>
              <li><a href="#week-5">Week 5 (Nov. 14)</a></li>
              <li><a href="#week-6">Week 6 (Nov. 21)</a></li>
              <li><a href="#final-project">Final Project (Dec. 05)</a></li>
            </ul>
          </li>
          <li><a href="#assessment">Assessment</a></li>
          <li><a href="#attendance">Attendance</a></li>
        </ul>
      </nav>
    </div>
  </aside>

  <div class="page-content" markdown="1">

# Topical Reading: Digital Humanities

**Course:** BA3 Korean Studies, Leiden University<br>
**Instructor:** Dr. Steven Denney<br>
**Time & Place:** Fridays, 11:15-13:00, Huizinga 0.09<br>
**Duration:** 6 seminars (October 10 - November 21)

---

## Expanded Description {#expanded-description}

This is the DH strand of the BA3 course **Contemporary Korea and Digital Humanities**. This course is meant to introduce students to digital humanities (DH) methods, focusing on text-as-data approaches. Using Orange Data Mining and pre-prepared Korean corpora, students will learn how to clean, analyze, and interpret textual data.

The DH strand complements the topical reading seminars by equipping students with methodological skills to support their undergraduate research and to introduce them to the DH side of research in the Humanities and Social Sciences. There are no programming requirements whatsoever in this course, although students will have the opportunity to explore ways to acquire such skills.

Students will learn how to prepare, analyze, and interpret text using **Orange Data Mining**. The aim is not technical mastery, but to understand how computational methods can support thesis research in the KoreaStudies (BA) program at Leiden University.

---

## Tutorials {#tutorials}

Each week lists required **Orange Data Mining Tutorials**.

- These tutorials are **required viewing before class**
- They are short (5-10 minutes each) and introduce the widgets you will use hands-on
- Watching them in advance will free up class time and have you better prepared for applying methods to Korean corpora

You can download the Orange Data Mining application **[here](https://orangedatamining.com/)**

Tutorials (to watch before class) are available here: [Orange Data Mining Tutorials (YouTube Playlist)](https://www.youtube.com/playlist?list=PLmNPvQr9Tf-ZSDLwOzxpvY-HrE0yv-8Fy)

---

## Assignments {#assignments}

In addition to attending weekly sessions, you are required to complete **weekly assignments ("deliverables")**. These tasks reinforce the skills introduced in tutorials and class exercises. Assignments can be found in the folder marked with the same name ([Assignments](https://github.com/scdenney/ba3_text_as_data/tree/main/assignments)).

### Format {#format}

Each deliverable consists of:
1. One or more screenshots of your Orange workflow/output
2. A short written reflection (approximately 1 paragraph)

### Submission {#submission}

- Commit your deliverables to your GitHub repository in the appropriate weekly folder (e.g., `week01/`, `week02/`, etc.)
- **Deadline:** 17:00 on the Monday following class unless otherwise specified

**Grading:**
- `2` = fully complete and accurate
- `1` = attempted but not fully complete/accurate
- `0` = incomplete, late, or not attempted

**Note:** You do *not* need to upload assignments to Brightspace. The instructor will review your GitHub repo and record grades.

**Weekly deliverables, together with attendance, make up 30% of your DH strand grade** (see Assessment section).

---

## Optional: R Programming Extensions {#optional-r-programming}

Students interested in developing foundational R programming skills alongside the DH strand are encouraged to explore the **R Programming Extensions**. These optional activities complement our work with Orange Data Mining and offer pathways to begin coding and analyzing text directly in R.

We will make use of two platforms:
- **Swirl** - interactive, in-R tutorials for learning R at your own pace: [swirlstats.com/students.html](https://swirlstats.com/students.html)
- **DataCamp** - an online learning platform with a dedicated class account

All enrolled students have access to the shared **DataCamp classroom**. The primary course to complete there is: [Introduction to Text Analysis in R](https://app.datacamp.com/learn/courses/introduction-to-text-analysis-in-r)

**Assessment policy for the optional R Programming track:**
- **Extra credit** will be awarded upon satisfactory completion of the designated lessons or modules (up to 0.25 points added to the final DH strand grade)
- Students who opt in but do not complete required lessons may receive a **minor penalty** to their DH strand grade. Opt in only if you plan to finish.

---

## GitHub Repository Requirement {#github-repository}

See the [Getting Started]({{ '/getting-started/' | relative_url }}) guide for detailed instructions on setting up your repository.

You are required to maintain a **private GitHub repository** for this course:

1. Create a new private repo named: `DH-TopicalReading-<Surname>`
2. Add the instructor (**username: scdenney**) as a collaborator
3. Keep the repo private, unless you explicitly choose to share it
4. Organize the repo with the following structure:

```
DH-TopicalReading-<Surname>/
├── assignments/
│   ├── week01/
│   │   ├── week01-deliverable.md
│   │   └── screenshots/
│   ├── week02/
│   │   └── ...
│   ├── week06/
│   └── final-project/
└── README.md
```

Each week's deliverable (markdown file + screenshots) must be committed to the correct subfolder.

At the start of the course, submit the **URL of your repo** to the instructor at [this Google Sheet](https://docs.google.com/spreadsheets/d/1iVdwLTfmVkMn2cQGXPxCC4YIxADawSKAWltZIxD5WMs/edit?usp=sharing).

This organization mirrors best practices for **research data management** and is part of the course's learning objectives.

---

## Corpus Overview {#corpus-overview}

The primary dataset for this course is the National Institute of Korean History (NIKH) history textbook corpus. This collection brings together Korean history textbooks produced under successive national curricula, spanning from the late Joseon and Korean Empire through the Japanese colonial period, liberation, and the postwar national curricula up to the present.

You may peruse an online-navigable version of the history textbooks through the National Institute of Korean History's official website: [contents.history.go.kr](https://contents.history.go.kr/front/ta/main.do)

Because textbooks are central to the formation of collective memory and national identity, this corpus is especially well suited for exploring questions of modern Korean identity.

For **supplementary purposes**, additional pre-prepared corpora are available:
- **Kaebyok (1920-1935):** An interwar magazine reflecting cultural, intellectual, and political debates in colonial Korea
- **Kyongje Yongu (1987-2017):** A North Korean economics journal, useful for examining how policy and ideology interact in the DPRK. Read more at [38 North](https://www.38north.org/2025/05/in-memoriam-kyongje-yongu/)

Other corpora will be introduced during the course to support student exploration. For the final project, students will be required to use one of the pre-prepared corpora, except the NIKH practice corpora, or to have approved the use of one of their own.

---

## Weekly Outline {#weekly-outline}

### Week 1 (Oct. 10): Introduction to DH, GitHub & Data Management {#week-1}

- **Lecture:** What is DH? Why text-as-data matters for Korean Studies. FAIR data principles.
- **Hands-On:** GitHub setup, orientation to Orange workflows and widgets.
- **Tutorials:** *Welcome to Orange, Data Workflows, Widgets & Channels*.
- **Deliverable:** Create GitHub repo + README reflection.

---

### Week 2 (Oct. 17): Text Preprocessing {#week-2}

- **Lecture:** Tokenization, stopwords, normalization. Korean-specific preprocessing challenges.
- **Hands-On:** Import corpora, apply preprocessing, compare raw vs. cleaned.
- **Tutorials:** *Text Preprocessing, Importing Text Documents*.
- **Deliverable:** Preprocessing workflow screenshot + reflection.

---

### Week 3 (Oct. 24): Descriptive Patterns {#week-3}

- **Lecture:** Frequency, keywords, word clouds. From descriptive to interpretive claims.
- **Hands-On:** Group analysis of corpora, frequency/word cloud outputs, keyword contrasts, clustering/projection.
- **Tutorials:** *Text Clustering, Multivariate Projection (Freeviz)*.
- **Deliverable:** Word cloud + reflections.

---

### Week 4 (Nov. 7): Classification & Prediction {#week-4}

- **Lecture:** Supervised methods, labels, evaluation, and applications in thesis research.
- **Hands-On:** Apply sentiment classification, evaluate accuracy, discuss limits.
- **Tutorials:** *Text Classification, Making Predictions, Model Evaluation*.
- **Deliverable:** Sentiment analysis + reflections.

---

### Week 5 (Nov. 14): Clustering & Similarity {#week-5}

- **Lecture:** Unsupervised methods; clustering documents. Strengths and pitfalls.
- **Hands-On:** Hierarchical and k-means clustering, interpret clusters/topics and compare approaches.
- **Tutorials:** *Hierarchical Clustering, k-Means & Topic Modeling widget demo*.
- **Deliverable:** Clustering + reflections.

---

### Week 6 (Nov. 21): Topic Modeling & Wrap-Up {#week-6}

- **Lecture:** Review: Comparing clusters vs. topics. Designing a DH project.
- **Hands-On:** Review of previous week, final project preparation.
- **Tutorials:** *Review previous week*.
- **Deliverable:** None - group preparation for final project.

---

### Final Project (Dec. 05) {#final-project}

The final project will take the form of an **in-person, four-hour "hackathon"** held in the DH Lab. Working in small groups, students will complete a text-as-data analysis project that draws directly on the skills developed in this six-week strand of the course.

Each group will:
- Select from a pre-prepared corpus (or set of corpora). It will be possible to use your own.
- Formulate a research question.
- Design and carry out a workflow in Orange Data Mining.
- Generate and interpret findings.
- Write up results and reflections on the process and findings.
- Submit it to Brightspace.

This is a **timed, in-class assignment** (not a take-home project). Further details will be provided in advance.

---

## Assessment {#assessment}

The DH strand of the course is worth 25% of the full course grade. That 25% is broken down as follows:

| Component | Weight |
|-----------|--------|
| Weekly Deliverables & Attendance | 30% |
| Final Project | 70% |

---

## Attendance {#attendance}

Full attendance is expected. Missing any sessions will put you behind. If you cannot attend all sessions, speak with the instructor in advance.

  </div>
</div>
