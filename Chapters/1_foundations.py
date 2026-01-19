from header import *

def one_one():
    return "test"

sub_chapters = {'1.1 BASICS': one_one()}

print("""\n[PREFACE]\nDiscrete mathematics is foundational to modern computer science and machine learning,
so I decided I should learn it at an intuitive level. The book Discrete Mathematics for Computer Scientists (Mott) 
is the resource I'm using for this. The overall idea of this project is that I want to reinforce and supplement
my learning in a unique way that will keep this information in my head. **Press enter to continue through the course content!**""")
input('')

for name, content in sub_chapters.items():
    print(f"[{name}] {content}")
    input('')