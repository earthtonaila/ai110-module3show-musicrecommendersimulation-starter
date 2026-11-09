"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs

Run from the project root with:  python -m src.main
"""

from src.recommender import load_songs, recommend_songs

WIDTH = 60
TOP_K = 3


def print_header(title: str) -> None:
    print("=" * WIDTH)
    print(title.center(WIDTH))
    print("=" * WIDTH)


def print_preferences(user_prefs: dict) -> None:
    print("\nUser preferences")
    print("-" * WIDTH)
    print(f"  Favorite genre : {user_prefs['genre']}")
    print(f"  Favorite mood  : {user_prefs['mood']}")
    print(f"  Target energy  : {user_prefs['energy']:.2f}")


def print_recommendations(recommendations: list) -> None:
    print(f"\nTop {len(recommendations)} recommendations")
    print("-" * WIDTH)
    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        # recommend_songs joins score_song's reasons with "; ", so split them back out.
        reasons = explanation.split("; ") if explanation else []
        print(f"\n{rank}. {song['title']} by {song['artist']}")
        print(f"   Score: {score:.2f}")
        print("   Reasons:")
        for reason in reasons:
            print(f"     - {reason}")
    print()


def main() -> None:
    songs = load_songs("data/songs.csv")

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=TOP_K)

    print_header("Music Recommender Simulation")
    print(f"\nSongs loaded: {len(songs)}")
    print_preferences(user_prefs)
    print_recommendations(recommendations)


if __name__ == "__main__":
    main()
