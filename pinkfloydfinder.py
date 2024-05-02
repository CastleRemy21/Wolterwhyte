albums = {
  "The Dark Side of the Moon": ["Speak to Me","Breathe", "On the Run", "Time", "The Great Gig in the Sky","Money","Us and Them","Any Colour You Like","Brain Damage","Eclipse"], 
  "Wish You Were Here": ["Shine On You Crazy Diamond Pt 1-5", "Welcome to the Machine","Have a Cigar","Wish You Were Here","Shine on You Crazy Diamond Pt 6-9"],
  "The Wall": ["In the Flesh?","The Thin Ice","Another Brick in the Wall Pt 1","The Happiest Days of Our Lives","Another Brick in the Wall Pt 2","Mother","Goodbye Blue Sky","Empty Spaces","Young Lust","One of my Turns","Don't Leave Me Now","Another Brick in the Wall Pt 3","Goodbye Cruel World","Hey You","Is There Anybody out There","Nobody Home","Vera","Bring the Boys Back Home","Comfortably Numb","The Show Must go on","In the Flesh","Run Like Hell","Waiting for the Worms","Stop","The Trial"," Outside the Wall"]
}

for album, songs in albums.items():
  print(f"{album}:")
  for song in songs:
    print(f"- {song}")