import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that comes to life",
                        "https://bit.ly/2M2uCP8",
                        "https://bit.ly/2ctDg5y")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://pt.wikipedia.org/wiki/Avatar_(filme)#/media/File:Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

spectre = media.Movie("007 Spectre",
                      "007 against Spectre",
                      "https://upload.wikimedia.org/wikipedia/pt/1/1a/Spectre-007.png",
                      "https://www.youtube.com/watch?v=z4UDNzXD3qA")


#print (spectre.storyline)

#spectre.show_trailer()
movies = [toy_story,avatar,spectre]
fresh_tomatoes.open_movies_page(movies)
