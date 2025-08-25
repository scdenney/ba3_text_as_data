# Topical Reading: Digital Humanities  
Course: BA3 Korean Studies, Leiden University  
Instructor: Dr. Steven Denney  
Time & Place: Fridays, 11:15–13:00, Huizinga 0.09  
Duration: 6 seminars starting October 10 and ending November 21

---

## Expanded Course Description
This is the DH strand of the BA3 course **Contemporary Korea and Digital Humanities**. This course is meant to introduce students to digital humanities (DH) methods, focusing on text-as-data approaches. Using Orange Data Mining and pre-prepared Korean corpora, students will learn how to clean, analyze, and interpret textual data.  

The DH strand complements the topical reading seminars by equipping students with methodological skills to support their undergraduate research and to introduce them to the DH side of research in the Humanities and Social Sciences. There are no programming requirements whatsoever in this course, although students will have the opportunity to explore ways to acquire such skills.

Students will learn how to prepare, analyze, and interpret text using **Orange Data Mining**. The aim is not technical mastery, but to understand how computational methods can support thesis research in the KoreaStudies (BA) program at Leiden University.

---

## Tutorials  
Each week lists required **Orange Data Mining Tutorials**.  
- These tutorials are **required viewing before class**.  
- They are short (≈5–10 minutes each) and introduce the widgets you will use hands-on.  
- Watching them in advance will free up class time and have you better prepared for applying methods to Korean corpora.

👉 Tutorials (to watch before class) are available here: [Orange Data Mining Tutorials (YouTube Playlist)](https://www.youtube.com/playlist?list=PLmNPvQr9Tf-ZSDLwOzxpvY-HrE0yv-8Fy)

---

## GitHub Repository Requirement  
See the ["how-to" guide](repo_how-to.md) (located in the syllabus folder) on how to get started with GitHub and repo management.

You are required to maintain a **private GitHub repository** for this course:  

1. Create a new private repo named: `DH-TopicalReading-<Surname>`.  
2. Add the instructor (**username: scdenney**) as a collaborator.  
3. Keep the repo private, unless you explicitly choose to share it.  
4. Organize the repo with the following structure:

📂 Student Repository Structure
<pre>
DH-TopicalReading-<Surname>/
  ├── assignments/    # Where you commit your assignments
│   ├── week01/
│   │   ├── week01-deliverable.md
│   │   └── screenshots/
│   ├── week02/
│   │   └── ...
│   ├── week06/
│   └── final-project/
└── README.md          # Use the README to introduce yourself and what your repo will do for you.
</pre>

5. Each week’s deliverable (markdown file + screenshots) must be committed to the correct subfolder.  
6. At the start of the course, submit the **URL of your repo** to the instructor.  

This organization mirrors best practices for **research data management** and is part of the course’s learning objectives.  

---

## Corpus Overview

The primary dataset for this course is the **국사편찬위원회 (Guksa Pyeonchan Wiwonhoe, National Institute of Korean History, NIKH) history textbook corpus**. This collection brings together Korean history textbooks produced under successive national curricula, spanning from the late **조선 (Joseon)** and **대한제국 (Daehan Jeguk)** through the **일제강점기 (Ilje Gangjeomgi, Japanese colonial period)**, liberation, and the postwar **교육과정 (gyoyuk gwajeong, national curricula)** up to the present. These textbooks, published and authorized by the state, offer an authoritative view of how the Korean nation, state, and people have been represented by state-sanctioned education across different political eras.  

You may peruse an online-navigable version of the history textbooks through the National Institute of Korean History’s official website: [contents.history.go.kr](https://contents.history.go.kr/front/ta/main.do)  

Because textbooks are central to the formation of collective memory and national identity, this corpus is especially well suited for exploring questions of **modern Korean identity**: how ideas of **민족 (minjok, nation/people)**, **국민 (gukmin, citizens)**, **시민 (simin, civic belonging)**, and **통일 (tongil, unification)** have been framed, contested, and transmitted to generations of (South) Korean students. In this way, the corpus links directly to broader themes in modern political sociology in Korea, which you are also examining in the topical reading strand of this course.  

For **supplementary purposes**, additional pre-prepared corpora are available:  
- **개벽 (Kaebyŏk, 1920–1935):** An interwar magazine reflecting cultural, intellectual, and political debates in colonial Korea. *Kaebyŏk* has been used extensively in scholarship on cultural nationalism and modern identity, including Michael Robinson’s *Cultural Nationalism in Colonial Korea, 1920–1925* (1988), Andre Schmid’s *Korea Between Empires, 1895–1919* (2002), and Henry Em’s “Minjok as a Modern and Democratic Construct: Sin Ch’aeho’s Historiography” (1999).  
- **경제연구 (Kyŏngje Yŏngu, 1987–2017):** A North Korean economics journal, useful for examining how policy and ideology interact in the DPRK. Read more about this at [38 North](https://www.38north.org/2025/05/in-memoriam-kyongje-yongu/).  

Other corpora may be introduced during the course to support student exploration.  

👉 You will make use of these corpora not only for weekly exercises but also for your **final project** and, if relevant and of interest, for your **BA thesis research**. We will discuss how to design a mini text-as-data project throughout the course and especially in Week 6.  


---

## Weekly Outline

### Week 1 (Oct. 10): Introduction to DH, GitHub & Data Management
- **Lecture:** What is DH? Why text-as-data matters for Korean Studies. FAIR data principles.  
- **Hands-On:** GitHub setup, orientation to Orange workflows and widgets.  
- **Tutorials:** *Welcome to Orange, Data Workflows, Widgets & Channels*.  
- **Deliverable:** Create GitHub repo + README reflection.  

---

### Week 2 (Oct. 17): Text Preprocessing with Aron v/d Pol
- **Lecture:** Tokenization, stopwords, normalization. Korean-specific preprocessing challenges.  
- **Hands-On:** Import corpora, apply preprocessing, compare raw vs. cleaned.  
- **Tutorials:** *Text Preprocessing, Importing Text Documents*.  
- **Deliverable:** Preprocessing workflow screenshot + reflection.  

---

### Week 3 (Oct. 24): Descriptive Patterns
- **Lecture:** Frequency, keywords, word clouds. From descriptive to interpretive claims.  
- **Hands-On:** Group analysis of corpora, frequency/word cloud outputs, keyword contrasts, clustering/projection.  
- **Tutorials:** *Text Clustering, Multivariate Projection (Freeviz)*.  
- **Deliverable:** Word cloud + clustering screenshot + reflection.  

---

### Week 4 (Nov. 7): Classification & Prediction
- **Lecture:** Supervised methods, labels, evaluation, and applications in thesis research.  
- **Hands-On:** Apply sentiment classification, evaluate accuracy, discuss limits.  
- **Tutorials:** *Text Classification, Making Predictions, Model Evaluation*.  
- **Deliverable:** Classification screenshot + reflection.  

---

### Week 5 (Nov. 14): Clustering & Similarity
- **Lecture:** Unsupervised methods; clustering documents. Strengths and pitfalls.  
- **Hands-On:** Hierarchical and k-means clustering, silhouette evaluation, interpret clusters.  
- **Tutorials:** *Hierarchical Clustering, k-Means, Silhouette*.  
- **Deliverable:** Clustering screenshot + ≈1-page reflection.  

---

### Week 6 (Nov. 21): Topic Modeling & Wrap-Up
- **Lecture:** Introduction to topic modeling (LDA). Comparing clusters vs. topics. Designing a DH project.  
- **Hands-On:** Run topic modeling on a corpus, interpret top words per topic, compare with clustering.  
- **Tutorials:** *Topic Modeling widget demo*.  
- **Deliverable:** Topic model output + reflection.  

---

## Final Project (after Week 6: deadline TBD)
- A **mini text-as-data analysis** project (≈3–4 pages). 
- Include: research question, corpus, workflow (screenshots), findings, and reflection on thesis relevance.
- More information to be provided.

---

## Assessment
The DH strand of the course is worth 25% of the full course grade. That 25% is broken down as follows:
- Weekly Deliverables & Attendance (6 × 5% = 30%)  
- Final Project (70%)

---

## Attendance
Full attendance is expected. Missing any sessions will put you behind. If you cannot attend all sessions, speak with the instructor in advance.
