# Player Behaviour Profiling

This project aims to highlight the profile of a League of Legends player based on their in-game performances.

## Goal

The goal of this project is to use machine learning techniques to identify and categorize typical player behaviors based on in-game statistics.  
By analyzing various performance indicators, we aim to detect patterns that reflect different playstyles and strategic tendencies among players.

Key metrics include:
- KDA (Kill/Death/Assist ratio)  
- CS per minute (Creep Score)  
- Gold generated per minute  
- Damage dealt and received  
- Vision score  
- Objectives participation  
- And more...

---

## I. Data Scraping

The first step involves collecting data from a large number of players in order to design and train our models.  
We use the official [Riot Games API](https://developer.riotgames.com/apis), which is freely accessible with an API key tied to a Riot Games account.

⚠️ It's important to note that API requests are **rate-limited** — by default, you can only send **100 requests per 2 minutes**, and **20 requests per second** for most endpoints. Efficient request management and caching are essential.

The API allows us to retrieve:
- **Summoner IDs** and **PUUIDs** (unique player identifiers)  
- **Match histories** (lists of match IDs)  
- **Detailed match data**, including:
  - Game duration and type  
  - Kills, assists, deaths  
  - Gold earned  
  - Damage dealt and taken  
  - CS count  
  - Vision score  
  - Role and lane information  

This data forms the foundation of our dataset and will be aggregated and preprocessed to extract meaningful behavioral patterns.

---

## II. Data Preprocessing

After retrieving raw data, several steps are taken to prepare it for analysis:

- Cleaning inconsistent or missing data  
- Aggregating statistics over multiple games per player  
- Feature engineering: building composite metrics or normalizing values  

---

## III. Modelling

We explore various machine learning methods to group and analyze player behaviors, but the main one will be :

- **Unsupervised Learning**:  
  - Clustering techniques (k-Means) to identify behavior types  
  - Dimensionality reduction (PCA, t-SNE) for visualization

We evaluate the models using scores, confusion matrices.

---

## 🛠️ Tech Stack

- **Language**: Python 3  
- **Libraries**: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `requests`.  
- **API**: [Riot Games API](https://developer.riotgames.com/apis)  
