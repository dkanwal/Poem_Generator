# Poem_Generator
This poem generator, named Genpo Supreme, generates a poem based on a possible four inspiring sets.

The inspiring sets are poems about Autumn, Love poems, Poems written by Native Americans, and poems about Climate Change. The poems used are as follows:

  	Climate Change:
      Water Devil by Jamaal May
      Lullaby in Fracktown by Lilace Mellin Guignard
      The Greenhouse Effect by Carl Dennis
    Native American:
       Carrizo by Crisosto Apache
       The Powwow at the End of the World by Sherman Alexie
    Fall Season:
       The Beautiful Changes by Richard Wilbur
       Beyond the Red River by Thomas McGrath
       November for Beginners by Rita Dove
    Love Poems:
       First Kiss by Kim Addonizio
       To have without holding by Marge Piercy
       Errata by Kevin Young 

In order to run the code, clone the repository and run Main.py. If you would like to change the number of iterations the genererator runs per cycle, you can modify the 'num_iterations' parameter on line 21 of Main.py. 

Building Genpo Supreme challenged me in a number of ways. First and foremost it taught me to use nlp for the first time in my computer science career, it was fascinating to investigate and learn to use all of the different functions within Spacy. Second, I found it difficult to come up with a metric for Genpo Supreme to evaluate itself on, but after some time on the whiteboard the syllable similarity statistic works effectively. Lastly, I hadn't used os.system before and it was cool to learn to incorporate terminal commands into a Python script. 

Schololary Articles: 


"Natural Language Processing and Computational Linguistics," by Bhargav Srinivasa-Desikan.
https://books.google.com/books?hl=en&lr=&id=48RiDwAAQBAJ&oi=fnd&pg=PP1&dq=natural+language+processing+spacy&ots=R3AbI5q_f0&sig=QPMH_y9GNm1KHpkrmh5W4cvIZd4#v=onepage&q=natural%20language%20processing%20spacy&f=false
Bhargav's book was a nice guide to using Spacy for nlp and inspired my free form design choice. 

"EloquentRobot: A Tool for Automatic Poetry Generation," by Jeffery D. McGovern & Gavin Scott.
https://www.gavinoscott.com/uploads/5/7/4/0/57406539/cpe582_paper.pdf
McGovern and Scott's work on the EloquentRobot tool inspired my idea for inspiring sets and how I could make my system creative. 

"Deep-Learning Powered AI for Poetry Generation with Author Linguistic Style Transfer," by Alejandro Rodriguez Pascual.
https://arxiv.org/abs/2112.11483
Pascual's article showed me the possibiliaties of more complex poem generators and the potential more advnaced NLP has in computational creativity. 
