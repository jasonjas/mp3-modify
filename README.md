# mp3-modify
Python 3.7 utility to add Title and Artist to files based on name

# Requires 
mutagen

# Filename Format
\<artist\>-\<title\>.mp3

Filename can contain any number of dashes (-) and will set the title as the text after the last dash. 

# Examples
- john smith-music.mp3
  - Title = music
  - Artist = john smith

- Blink-182-Feeling This.mp3
  - Title = Feeling This
  - Artist = Blink-182
