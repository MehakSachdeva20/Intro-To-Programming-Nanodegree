import media #it will import all the media file function automatically.

import fresh_tomatoes#it impoer the files from the already created file freash tomatoes

ms_dhoni = media.Movie("M.S. Dhoni",
                       "The story of the India's most Successful captain and about the struggle he faces while becoming the best. Directed by Neeraj Panday , this film leaves a message that a person's determination,hardwork and will power is enough for achieving the world",
                       "https://upload.wikimedia.org/wikipedia/en/3/33/M.S._Dhoni_-_The_Untold_Story_poster.jpg",
                       "https://www.youtube.com/watch?v=6L6XqWoS8tw")#it contains the title, story -line , the linking image and the linking you tube trailer

pk = media.Movie("PK",
                 "It tells the story of an alien which comes to Earth in search of something and open the eyes of the people from various myth ",
                 "https://upload.wikimedia.org/wikipedia/en/c/c3/PK_poster.jpg",
                 "https://www.youtube.com/watch?v=SOXWc32k4zA")#it contains the title, story -line , the linking image and the linking you tube trailer

raees = media.Movie("Raees",
                    "Here comes the blockbuster of the KING KHAN - RAEES.Directed under the guidance of Rahul Dholakia this film mainly focuses on criminal life of Abdul Latif's",
                    "https://upload.wikimedia.org/wikipedia/en/2/2b/Raees_Poster.jpg",
                    "https://www.youtube.com/watch?v=J7_1MU3gDk0")#it contains the title, story -line , the linking image and the linking you tube trailer

dangal = media.Movie("DANGAL",
                     "Aamir Khan - once again his film DANGAL has broken all the records. The saying mari chooriyan choro se kam hai ke is making the world go crazy. This film mainly focuses that if proper rigths are given to girls they can bring laurels to the family",
                     "https://upload.wikimedia.org/wikipedia/en/9/99/Dangal_Poster.jpg",
                     "https://www.youtube.com/watch?v=x_7YlGv9u1g")#it contains the title, story -line , the linking image and the linking you tube trailer


kaabil = media.Movie("KAABIL",
                     "This story inspires a person that inspite of varous problems a person can lead a happy life if he is determined",
                     "https://upload.wikimedia.org/wikipedia/en/c/ce/Kaabil_Movie_Poster.jpg",
                     "https://www.youtube.com/watch?v=nubDFeiUAsI")#it contains the title, story -line , the linking image and the linking you tube trailer

ae_dil_hai_mushkil = media.Movie("ADHM",
                                 "This story is based on thr live in relationships",
                                 "https://upload.wikimedia.org/wikipedia/en/2/2a/Ae_Dil_Hai_Mushkil2.jpg",
                                 "https://www.youtube.com/watch?v=Z_PODraXg4E")#it contains the title, story -line , the linking image and the linking you tube trailer




movies = [ms_dhoni,pk,raees,dangal,kaabil,ae_dil_hai_mushkil]#a list or an array is made in order to store the name of the videos

fresh_tomatoes.open_movies_page(movies)#calling function in order to show the videos


