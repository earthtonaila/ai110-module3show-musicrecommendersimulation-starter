# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

This music recommendation system uses content-based filtering to identify songs that match a user's musical preferences. Each song is evaluated based on its genre, mood, and energy level.

The algorithm awards 2.0 points for a genre match, 1.0 point for a mood match, and up to 1.0 point for energy similarity. The energy score is calculated using the absolute difference between the song's energy and the user's preferred energy level.

After scoring all songs, the system sorts them from highest to lowest score and returns the top recommendations. Each recommendation includes an explanation of the factors that contributed to its score.

This approach is simple and interpretable, but it may favor genre matches over songs with similar moods or energy levels. It also does not learn from a user's listening history or account for preferences that change over time.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users 

One limitation of my recommendation system is that it places more importance on genre than on mood or energy. This can cause songs from a user's favorite genre to rank higher than songs from other genres that better match their desired musical vibe. The system also relies on a small song dataset, which limits the variety of recommendations available. These limitations may create a filter bubble by repeatedly recommending similar songs instead of introducing users to different styles. Adjusting the feature weights and expanding the dataset could improve the system's diversity.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

I evaluated my music recommendation system using three different user profiles:

1 High-Energy Pop: prefers pop music, happy moods, and energy of 0.9
2 Chill Lofi: prefers lofi music, calm moods, and energy of 0.2
3 Deep intense Rock: prefers rock music, intense moods, and energy of 0.95

Each profile was tested against the same song dataset, and the top five recommendations were recorded

I tested the sensitivity of my algorithm by reducing the genre match weight from 2.0 to 1.0 and increasing the energy similarity weight from 1.0 to 2.0. The mood weight remained unchanged at 1.0.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
