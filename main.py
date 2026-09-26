import os
import subprocess
import time
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>KinoOnline — Трейлеры</title>
        <style>
            * { box-sizing: border-box; margin: 0; padding: 0; }
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #141414; color: #ffffff; padding: 20px; }
            header { text-align: center; padding: 20px 0; border-bottom: 2px solid #E50914; margin-bottom: 30px; }
            h1 { color: #E50914; font-size: 28px; }
            .movies-grid { display: flex; flex-direction: column; gap: 25px; }
            .movie-card { background-color: #1f1f1f; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 10px rgba(0,0,0,0.5); }
            .movie-card img { width: 100%; height: 350px; object-fit: cover; }
            .movie-info { padding: 15px; }
            .movie-title { font-size: 20px; margin-bottom: 8px; }
            .movie-desc { font-size: 14px; color: #aaa; margin-bottom: 15px; line-height: 1.4; }
            .btn-watch { display: block; width: 100%; padding: 12px; background-color: #E50914; color: white; text-align: center; text-decoration: none; font-weight: bold; border-radius: 5px; }
        </style>
    </head>
    <body>
        <header>
            <h1>🎬 Кино и Игры</h1>
            <p style="color: #888; margin-top: 5px;">Смотри трейлеры на YouTube</p>
        </header>

        <div class="movies-grid">
            <!-- Человек-паук -->
            <div class="movie-card">
                <img src="https://images.unsplash.com/photo-1635863138275-d9b33299680b?w=500" alt="Человек-паук">
                <div class="movie-info">
                    <div class="movie-title">Человек-паук: Нет пути домой</div>
                    <div class="movie-desc">Жизнь Питера Паркера переворачивается, когда личность Человека-паука раскрывается.</div>
                    <a href="https://www.youtube.com/watch?v=JfVOs4VSpmA" target="_blank" class="btn-watch">▶ Смотреть трейлер на YouTube</a>
                </div>
            </div>

            <!-- GTA 6 -->
            <div class="movie-card">
                <img src="https://images.unsplash.com/photo-1542751371-adc38448a05e?w=500" alt="GTA 6">
                <div class="movie-info">
                    <div class="movie-title">Grand Theft Auto VI (GTA 6)</div>
                    <div class="movie-desc">Официальный первый трейлер долгожданного продолжения серии от Rockstar Games.</div>
                    <a href="https://www.youtube.com/watch?v=QdBZY2fkU-0" target="_blank" class="btn-watch">▶ Смотреть трейлер на YouTube</a>
                </div>
            </div>
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

	