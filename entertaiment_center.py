import media
import webbrowser
import fresh_tomato

toy_story = media.Movie("Toy Story" , 
                        "a story about toys that come to life" , 
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg" , 
                        "https://www.youtube.com/watch?v=gAjFSSUF3t8")

# webbrowser.open(f"{toy_story.trailer_youtube_url}")

avatar = media.Movie("Avatar",
                    "Human arrive at a new planet to collect a rare metal but there is a tribe of avatar living there " ,
                    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=6ziBFh3V1aM")
print(avatar.storyline)
# avatar.show_trailer()

real_steel = media.Movie("Real steel",
                         "This is set in the future where boxing is not done by human but by robots and it is awesome...",
                         "https://upload.wikimedia.org/wikipedia/en/2/22/Real_Steel_Poster.jpg",
                         "https://www.youtube.com/watch?v=T75j9CoBVzE")

# real_steel.show_trailer()

school_of_rock = media.Movie("School of Rock",
                             "The story of a amazing guitar player whos out of time and his band kick him out them he starter teaching as a substitute taking the name and identity of his friend where he encounters children that are perfect for a band",
                             "http://www.gstatic.com/tv/thumb/v22vodart/33094/p33094_v_v8_ab.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

bird_box = media.Movie("Bird Box",
                       "the world is going to end people are killing themself because of mistirous monsters that if you look at them you with have the necesity to commit suicide",
                       "https://m.media-amazon.com/images/M/MV5BMjAzMTI1MjMyN15BMl5BanBnXkFtZTgwNzU5MTE2NjM@._V1_.jpg",
                       "https://www.youtube.com/watch?v=o2AsIXSh2xo")

quien_manda = media.Movie("Quien Manda",
                          "The story of a guy who has a believe that you can only be with a women for 3 month them on to the next who falls in love",
                          "https://www.paradard.com/images/cinemard/peliculas/2013/posters/quien_manda_poster.jpg",
                          "https://www.youtube.com/watch?v=sHYH2rKAE58")

movies = [toy_story , avatar , real_steel , school_of_rock , bird_box , quien_manda]

fresh_tomato.open_movies_page(movies)

