# Player Behaviour Profiling

This project aims to highlight the profile of a League of Legends player based on their in-game performances in order to predict the winrate of players.

## Goal

First, we will use statistical or machine learning techniques to identify and categorize typical player behaviors based on in-game statistic by clustering.
By analyzing various performance indicators, we aim to detect patterns that reflect different playstyles and strategic tendencies among players.
In the other hand, the main goal is to predict the winrate of players with machine learning techniques with the same metrics.

Key metrics include:
- KDA (Kill/Death/Assist ratio)  
- CS per minute (Creep Score)  
- Gold generated per minute  
- Damage dealt and received  
- Vision score  
- Kill participation

---

## I. Data Scraping

The first step involves collecting data from a large number of players in order to design and train our models.  
We use the official [Riot Games API](https://developer.riotgames.com/apis), which is freely accessible with an API key tied to a Riot Games account.

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

## III. Clustering

We explore various methods to group and analyze player behaviors, but the main one will be :

- **Unsupervised Machine Learning methods**:  
  - K-Means, Expectation Maximization
- **Statistical methods**:  
  - Hierachical Clustering (Dendogramme)
 
## IV. Machine learning

...

---

## 🛠️ Tech Stack

- **Language**: Python 3  
- **Libraries**: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `requests`.  
- **API**: [Riot Games API](https://developer.riotgames.com/apis)  
