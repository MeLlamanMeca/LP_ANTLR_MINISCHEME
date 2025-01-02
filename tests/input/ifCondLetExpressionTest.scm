(define x 1)
(define y 2)

(define (main)

    ; IF tests
    (display (if (> 15 10) #t #f))
    (newline)
    (display (if (> 5 10) #f #t))
    (newline)
    (display (if (> 10 10) #f #t))
    (newline)

    ; COND tests
    (display (cond 
                ((> 5 3) #t)
                ((> 5 3) #f) 
                ((> 5 3) #f) ))
    (newline)
    (display (cond 
                ((> 3 3) #f)
                ((> 5 3) #t) 
                ((> 5 3) #f) ))
    (newline)
    (display (cond 
                ((> 2 3) #f) 
                ((> 3 3) #f) 
                ((> 5 3) #t) ))
    (newline)

    ; LET tests
    (display x)
    (display " ")
    (display y)
    (newline)
    (display(let ((x 5)(y 6)) x))
    (display " ")
    (display(let ((x 5)(y 6)) y))
    (newline)
    (display x)
    (display " ")
    (display y)
    

    

)