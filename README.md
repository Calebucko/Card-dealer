    # Card-dealer

    cardDB = 52
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
    13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
    26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
    39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51)
    Rank for cards gets the list ("Ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king")
    suit for cards gets the list ("diamonds", "hearts", "spades", "clubs")
    hand holders gets the list ("deck", "computer", "player")

    Deck hand holder gets value 0
    Computer hand holder gets value 1
    player hand holder gets value 2

    define main function ()
        create variable cardDB that gets initCards()
            create for loop that checks cards in range
                assigns Card from card dealer to player
                assigns Card from card dealer to computer
            create for loop that shows cardDB location and enumerate the list in (cardDB)
                print the card list in a random range of numbers
                have cardDB and player shows their hands
                have cardDB and computer show their hands
    initcard function ()
        Assign all 52 cards to DB
        All entries are listed at location zero

    assign cards function ()
        involves cardDB and hands
        pick through random range of numbers
        assign hand to that numbers location

    show database function ()
        sift through all cards
        print card number
        print card name
        print card location(all done in getcard function)

    show hand function ()
        involves cardDB and hands
        index=0
        look through all cards
        if there is a card in one of the hands
            print the cards name and number (this will be getcard name function)

    getcard name function ()
        involves card number and name
        divide all card numbers by 13 for suit
        use remainder of division to assign rank to card
        assign names of suits and ranks as strings
        return(name of suit and rank) 
    
            
            

    
    

    
