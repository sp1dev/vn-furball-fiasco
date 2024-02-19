# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define me = Character("Me", color="#bf7e04")
define di = Character("Diamond", color="#43384d")
define vin = Character("Vinny", color="#042669")
define cash = Character("Cashier", color="#240244")

# An item the player can pick up. Does not affect story of game.
default foil_ball = False

# The game starts here. Each label acts as a "branch" of the game. 
# This game only has one branch, in other words, one outcome.
label start:

    # Intro Scene: Mallow's Apartment

    play music "good-night.mp3" fadein 1.0 volume 0.5

    # Show a background.
    scene bg apartment_mallow_sitting
    with fade

    me "Finally, the day has come! Time to snag that PS5 from GameStop."

    me "Hope they're not sold out!"

    "You grab a small backpack and head out the door with excitement in your stride."

    #Scene 1: Alleyway
    scene bg alley
    with fade

    play music "lady-of-the-80s.mp3" fadeout 1.0 fadein 1.0 volume 0.3
    
    "As you walk down Main Street, you hear a familiar voice coming from a dumpster in the alley." 

    "You look over..."

    me "I always called you my Diamond in the rough!"

    show diamond smiling front
    with dissolve

    di "Don't knock dumpster diving till ya try it!"

    di "You know, one person's trash is another's treasure. Join the fun!"

    # displays a menu to the player to choose an option
    menu: 
        "Us cats have a different relationship to trash than opossums… But I'll always give anything a try":
            # pass tells renpy to do nothing and continue with the script. 
            # In other words, when the option has no effect and doesn't cause a separate branch.
            pass

        "No way in feline heaven... but, alright, twist my paw why don't ya":
            pass
    
    show diamond excited
    with dissolve

    "Diamond's enthusiasm is infectious. Perhaps she caught something from the garbage…"

    "You cautiously join in on her treasure hunting adventure."

    di "Come on, Mallow! Don't you want to find something even better than a PS5? Who knows what treasures await!"
    
    scene bg dumpster_closeup
    with fade

    "You hesitantly climb into the dumpster."

    "A small thump sound echoes as you land…"

    show diamond smiling front
    with dissolve

    di "That was just the sweet sound of garbage!"

    "As you dig through the questionable items in the dumpster, your paw brushes against something unusual..."
    
    me "What's this?"

    hide diamond

    "You pull out a shiny, crinkled..."

    show foil_ball
    with dissolve

    show diamond smiling front at left
    with dissolve

    di "A foil ball!"

    "It's lightweight, perfect for batting around."
    
    me "Every cat's dream toy... but should I really take this?"

    menu:
        "One cat's trash is this cat's treasure!":
            # use this method when still, no separate branch is created, but 
            # different dialogue is shown based on player's selection
            $ foil_ball = True

        "I prefer my toys store-bought, not dumpster-sourced.":
            pass

    if foil_ball == True:     
        me "It's purr-fectly acceptable to recycle fun, right?"
        "You're already thinking about how you're going to play with this shiny foil later."
    else:
        "Let's leave this for some alley cat's treasure trove."
        me "I don't need another toy today, I already have my sights on the PS5!"

    hide foil_ball
    with dissolve

    show diamond smiling front at center
    with dissolve

    di "Only you would find a toy in a pile of trash. You have a real talent for this, Mallow!"

    me "Thanks, Diamond."

    "But your mind is still fixated on the thump sound from earlier..."

    menu:
        "I'm no trash detective, but let's see what that was.":
            pass

        "Probably just my legendary grace. Let's hope the trash cushions my fall next time.":
            pass
  
    "As you feel around one more time, you become nauseous.."
    
    me "I don't feel so good..."

    show diamond frowning front
    with dissolve

    me "Maybe a cat's place isn't in a dumpster after all."

    di "Aw, I'm sorry, Mallow."

    di "Let's get you out of here."

    "Diamond gently helps you out of the dumpster."

    scene bg alley
    with fade
    
    show diamond smiling front at left
    with dissolve

    "As you and Diamond climb out, a shadow looms over you."
    
    show vinny smirk at right
    with dissolve

    "Vinny, with his mischievous grin, leans against the alley wall."

    vin "Would ya look at what the opossum dragged in…"

    vin "Dumpster diving, really?"

    di "Hey Vincent, find any loot lately?"

    vin "No time to chat- I got Grand Theft Otter 6 waiting on my brand new PS5."

    vin "Keep digging in the trash, though. Maybe you'll find some ancient relics."

    vin "Adios, cheese bags."

    hide vinny
    with dissolve

    hide diamond
    with dissolve
    "Vinny saunters away in his exaggerated swagger, leaving you and Diamond in the alley."

    "You dust yourself off, feeling a mix of amusement and annoyance."

    show diamond smiling side
    with dissolve

    di "What a funny racoon..."

    me "We've got a PS5 to track down, remember?"

    di "I'm right behind you, Mallow. Adventure awaits, in and out of dumpsters!"

    "You exit the alley with your buddy, your quest for the PS5 continuing amidst the bustling city streets..."

    # Scene 2: The Walk to GameZoo
    play music "emotional-80s.mp3" fadeout 1.0 fadein 1.0 volume 0.3

    scene bg street_gamezoo
    with fade

    "You and Diamond stroll leisurely towards GameZoo, the most popular video game store for the urban animal kingdom."

    "The streets are bustling with other animals, each with their own errands and adventures."

    show diamond smiling front
    with dissolve

    di "I'm really glad you invited me… I can't afford a PS5 on my own right now."

    me "You're my best friend, Di!"

    me "I couldn't dream of playing without you."

    di "You're my best friend too, Mal."

    "You see a warm smile appear on her face."

    scene bg street_vinny
    with fade

    show diamond smiling front
    with dissolve

    di "So, which game are ya gonna play first?"

    menu:
        "I'm thinking of trying Fortbite first.":
            $ first_game = "fortbite"

        "Grand Theft Otter 6, for sure.":
            $ first_game = "gto"
        
        "Tony Hawk Prowl Skater looks awesome.":
            $ first_game = "tony hawk"

        "I'm leaning towards Cat of Duty.":
            $ first_game = "cod"

    if first_game == "fortbite":
        di "Fortbite, huh? Watch out for those stealthy squirrels! They're nuts about ambushes!"

        "Diamond does a fun, silly dance."

    elif first_game == "gto":
        di "I've waited years for GTO!"

        di "Make sure you don't get too caught up in those river chases, you might get your fur wet!"

        "Diamond dramatically looks around for the otter police."

    elif first_game == "tony hawk":
        di "Just don't try those stunts at home, or you'll end up more like Tony 'Hawkward'!"

        "Diamond suddenly freezes... you realize she's pretending to play dead."

    elif first_game == "cod":
        di "Cat of Duty, huh? Remember, it's not just about having nine lives; it's about how you use them!"

        "Diamond pretends to hide behind a wall, and peeks out to scope enemies."

    me "Haha. You bet, Diamond."

    scene bg gamezoo_front
    with fade

    play music "lady-of-the-80s.mp3" fadeout 1.0 fadein 1.0 volume 0.3
    
    "As you and Diamond approach GameZoo, you both can't help but pause and take in the vibrant storefront."

    show diamond smiling front
    with dissolve

    me "Here we are, the gamer's paradise!"

    di "Let's gooooo"

    "Your excitement grows as Diamond opens the door, and you both step in."

    # Scene: Inside GameZoo

    scene bg gamezoo_inside
    with fade

    show diamond excited
    with dissolve

    "The sounds of video game music and chattering customers fill the air."

    me "Wow, I feel like a bull in a candy store!"

    show diamond smiling front
    with dissolve

    di "Hah I think you mean 'kid' not 'bull'..."

    di "But yeah, it's amazing!"

    menu:
        "I just wanna get straight to it! Head to the cashier":
            pass

        "Time to dive into the sea of cool merch!":
            $ store_choice = "merch"

        "I've got to check out these games!":
            $ store_choice = "games"

    hide diamond

    cash "Attention gamers! Just a heads-up, we've got only one PlayStation left in stock!"

    if store_choice == "merch":
        scene bg gamezoo_merch
        with fade

        me "Time to dive into the sea of cool merch!"
        
        show diamond smiling side
        with dissolve

        di "I bet you could find some neat gaming gear here!"

        me "Yeah! Maybe a plushie to keep me company during gaming marathons."

        di "Hey, did you hear that about the PlayStation?"
    
    elif store_choice == "games":
        scene bg gamezoo_games
        with fade

        me "I've got to check out these games!"

        show diamond smiling side
        with dissolve

        di "Look, it's the new Super Monkey Ball!"

        di "These titles are amazing!"
        
        di "Oh, did you catch that? Only one PlayStation left!"

    me "Let's get that PS5 already!"

    scene bg gamezoo_cashier
    with fade

    me "One PS5, please."

    cash "Last one left, it's your lucky day."
    
    cash "That'll be 526 Furbucks, please."

    "As you reach for your wallet, you realize something is amiss..."

    me "Oh no..."

    me "My wallet is missing!"

    menu:
        "Arch your back and hiss in frustration":
            pass

        "Think hard and try to remember where you last had it.":
            pass

    show diamond frowning front
    with dissolve

    di "It's all my fault! You must've dropped it in the dumpster..."

    "Vinny comes rushing in, huffing and puffing."

    hide diamond

    show vinny smiling front
    with dissolve

    vin "Hey, I finally caught up to you guys!"

    vin "I found this in the alley, Mallow!"

    hide vinny

    show vinny smiling front at right
    with dissolve

    "Vinny holds up your precious wallet."

    me "Vinny, you're a lifesaver!"

    show diamond excited at left
    with dissolve

    di "We owe you big time, Vin!"

    "You fork over your Furbucks that you've been saving up for months."

    me "Here's for the PS5. What a close call!"

    me "Let's have a welcome home party for my new PlayStation!"

    me "Vinny, are you in?"

    hide diamond

    hide vinny

    show vinny excited
    with dissolve

    vin "Yeah! Can I take some unboxing footage for my MewTube channel?"

    me "Of course, Vin!"

    me "C'mon, let's get outta here."

    scene bg gamezoo_front
    with fade

    "The three of you excitedly exit GameZoo."

    scene bg mallow_apt
    with fade

    show diamond smiling front at left
    with dissolve

    show vinny smiling front at right
    with dissolve

    di "Game night just got an epic upgrade!"

    "Your cozy apartment awaits, ready to host a night of fun, laughter and virtual adventures..."

    # This ends the game.
    "{b}.:. Thank you for playing my first visual novel! .:.{/b}"

    return
