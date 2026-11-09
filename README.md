# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

Music recommendation systems predict which songs users might enjoy by analyzing their listening behavior and musical preferences. Collaborative filtering identifies patterns among users with similar listening habits, while content-based filtering recommends songs based on their musical attributes. My simulation will use content-based filtering to compare each song's genre, mood, energy, and tempo with a user's preferences. Each song will receive a weighted similarity score, and songs with the highest scores will be recommended first. I will prioritize genre and mood while using energy and tempo to identify songs with a similar musical vibe.

Each song recieves a score based on how closely its attributes match the user's preferences. Genre contributes up to 40 points, mood contributes up to 30 points, energy similarity contributes up to 20 points, and tempo similarity contributes up to 10 points. The songs are then ranked from highest to lowest score, and the best matches are recommended first.

Because genre contributes more points than mood or energy, the system may over-prioritize genre and overlook songs from other genres that match the user's desired vibe. The recommender also depends on a limited dataset and cannot account for individual listening history, changing preferences, or musical characteristics not included in the CSV. Increasing the diversity of songs and adjusting feature weights could improve recommendations.

You can include a simple diagram or bullet list if helpful.

Song Features
genre : the song's musical category
mood : the emotional feeling of the song
energy : the song's intensity or activity level
tempo_bpm : the song's speed in beats per minute

UserProfile Features
preferred_genre : the user's favorite musical genre
preferred_mood : the user's desired musical mood
preferred_energy : the user's preferred energy level
preferred_tempo : the user's preferred tempo in BPM

user_profile = {
  "favorite_genre": "pop",
  "favorite_mood": "calm",
  "target_energy": 0.3,
}

The system calculates a score for each song using the following rules:
genre match: +2.0 points if the song's genre matches the user's favorite genre
mood match: +1.0 point if the song's mood matches the user's favorite mood
energy similarity: 1 - abs(song_energy - target_energy)
The maximum possible score is 4.0 points. After calculating the scores for all songs, the system sorts them from highest to lowest and returns the top 3 recommendations.

1 Input: read the user's preferred genre, mood, and energy
2 Process: read each song from songs.csv and calculate its similarity score
3 Ranking: sort songs by their total scores
4 Output: display the top 3 highest-scoring songs

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



