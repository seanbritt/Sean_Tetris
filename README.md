I want to see if i can make tetris without looking at a tutorial.

Objects: 
    displayed:
        pieces
        field
        buttons(volume, back, etc)

    abstract:
        shapes for the pieces(left z, right z, line, box, left L, right L, T)
        grid of the field
        game speed
        

Events:
    change speed
    change shape orientation
    fast drop
    delete row
    piece touches another piece


Flow:
    - each "round":  
        - a certain amount of time:
            - at the beginning of the timer, the piece drops a level before the timer ends, the user can flip the piece
        - the piece enters the level below in the same orientation as the level above
    
    piece movement:
        rotation:
            can be handled as a vector rotation, right?:
                1. each piece has a coordinate
                2. 
        can rotate as long as nothing is in its way:
            how can i tell nothing is in the way?:
                do i need to check every block of the piece to tell i am touching something?
                I must consider if the movement is valid by considering if there would be overlapping 
                    blocks if the movement took place
                
            does each piece need a special pivot point? 
            does each piece need a special "boundary box"?