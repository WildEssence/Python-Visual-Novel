define r = Character('Sir Raymond')
define f = Character('Fae Clan Representative')
define e = Character('Elven Clan Representative')
define d = Character('Dwarven Clan Representative')



define WM = 5 # Water Magic
define FM = 5 # Fire Magic
define AM = 0 # Air Magic
define EM = 0 # Earth magic
define ELM = 0 # Eletric magic
define PM = 0 # Physic magic
define MM = 0 # Metal Magic
define DM = 0 # Dawn Magic
define Faunia = '' # Faunia
define Money = 1000
define Health = 100
define Allies = 0

label start:

    scene bg Isle of peace
    with fade

    label Prologue:
     'PROLOGUE'
     'Isle of peace, 1 Feb, 19 Dynasty years'
     'It was a cold foggy night. An assembly of all the clan Chieftains was called,
     to the storm castle to discuss the terms of the peace treaty between the various factions of the humans,
     the fae and the other inhabitants of this land'
     'you are currently playing as Sir Raymond, a representative of the Human clans'

    scene throne room
    with fade
    show r grim
    r 'This is what the human clans have decided: What you ask of the world
    is madness'
    r 'We will not give up our magic'
    r 'all our clans apart from the dragon clan stands with us on this matter'
    r 'even the elven clans and dwarven clan stand with us'
    $ ui.timer(5.0, ui.jumps('slow'))
    menu:
        'Bribe the elven and dwarven clans to stand with you to gain more allies!'
        'You have [Money] Coins'
        'I will ask (500 coins)':
            $Money-=100
            $Allies+=5
            e 'We pledge to stand with you dear humans!
            All our armies are in your disposal'
            e 'We just want territories for our own in the mountains'
            d 'We second that!'
            'Ally point:[Allies]'
        "Never Mind, i don't have money":
            e 'We will try stand with you, but some of our clans may not join you'
            d 'And we will be neutral in this fight'
            $Allies+=1
            'Ally Point:[Allies]'
    label slow:
        'Too Slow'
        jump scene2
label scene2:
    