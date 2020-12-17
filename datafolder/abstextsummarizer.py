from transformers import pipeline
import sys
import tokenizer

if __name__ == "__main__":
    # article = sys.argv[1]
    article = """
    Technology gets the creative bug

The hi-tech and the arts worlds have for some time danced around each other and offered creative and technical help when required.

Often this help has come in the form of corporate art sponsorship or infrastructure provision. But that dance is growing more intimate as hi-tech firms look to the creative industries for inspiration. And vice versa. UK telco BT is serious about the idea and has launched its Connected World initiative. The idea, says BT, is to shape a "21st Century model" which will help cement the art, technology, and business worlds together. "We are hoping to understand the creative industry that has a natural thirst for broadband technology," said Frank Stone, head of the BT's business sector programmes. He looks after several "centres of excellence" which the telco has set up with other institutions and organisations, one of which is focused on creative industries.

To mark the initiative's launch, a major international art installation is to open on 15 April in Brussels, with a further exhibit in Madrid later in the summer. They have both been created using the telco's technology that it has been incubating at its research and development arm, including a sophisticated graphics rendering program. Using a 3D graphics engine, the type commonly used in gaming, Bafta-winning artists Langlands & Bell have created a virtual, story-based, 3D model of Brussels' Coudenberg Cellars.

They have recently been excavated and are thought to be the remnants of Coudenberg Palace, an historical seat of European power. The 3D world can be navigated using a joystick and offers an immersive experience of a landscape that historically had a river running through it until it was bricked up in the 19th Century. "The river was integral to the city's survival for hundreds of years and it was equally essential to the city that it disappeared," said the artists. "We hope that by uncovering the river, we can greater understand the connections between the past and the present, and appreciate the flow of modernity, once concealing, but now revealing the River Senne." In their previous works they used the Quake game graphics engine. The game engine is the core component of a video game because it handles graphics rendering, game AI, and how objects behave and relate to each other in a game. They are so time-consuming and expensive to create, the engines can be licensed out to handle other graphics-intensive games. BT's own engine, Tara (Total Abstract Rendering Architecture) has been in development since 2001 and has been used to recreate virtual interactive models of buildings for planners. It was also used in 2003 in Encounter, an urban-based, pervasive game that combined both virtual play in conjunction with physical, on-the-street action. Because the artists wanted video and interactive elements in their worlds, new features were added to Tara in order to handle the complex data sets. But collaboration between art and digital technology is by no means new, and many keen coders, designers, games makers and animators argue that what they create is art itself.

As more tools for self-expression are given to the person on the street, enabling people to take photos with a phone and upload them to the web for instance, creativity will become an integral part of technology. The Orange Expressionist exhibition last year, for example, displayed thousands of picture messages from people all over the UK to create an interactive installation.

Technology as a way of unleashing creativity has massive potential, not least because it gives people something to do with their technology. Big businesses know it is good for them to get in on the creative vein too. The art world is "fantastically rich", said Mr Stone, with creative people and ideas which means traditional companies like BT want to get in with them. Between 1997 and 2002, the creative industry brought £21 billion to London alone. It is an industry that is growing by 6% a year too. The partnership between artists and technologists is part of trying to understand the creative potential of technologies like broadband net, according to Mr Stone. "This is not just about putting art galleries and museums online," he said. "It is about how can everyone have the best seat in house and asking if technology has a role in solving that problem." With broadband penetration reaching 100% in the UK, businesses with a stake in the technology want to give people reasons to want and use it. The creative drive is not purely altruistic obviously. It is about both industries borrowing strategies and creative ideas together which can result in better business practices for creative industries, or more patent ideas for tech companies. "What we are trying to do is have outside-in thinking. "We are creating a future cultural drive for the economy," said Mr Stone.

    """
    sente_gen = tokenizer.split_into_sentences(article)
    size = 0
    for sentence in sente_gen:
        size+=1
    summarizer = pipeline('summarization')
    print(summarizer(article,max_length=int((2*size)//3),min_length=int(size//3)))
    sys.stdout.flush()