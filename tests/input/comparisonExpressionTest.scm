(define (main) 
    ;comparison = tests
    (display (= 3 3)) (newline)
    (display (= 3 5)) (newline)
    (display (= #f #f)) (newline)
    (display (= #f #t)) (newline)
    (display (= #t #t)) (newline)

    ;comparison < tests
    (display (< 3 5)) (newline)
    (display (< 5 3)) (newline)

    ;comparison > tests
    (display (> 5 3)) (newline)
    (display (> 3 5)) (newline)

    ;comparison <= tests
    (display (<= 3 3)) (newline)
    (display (<= 3 5)) (newline)
    (display (<= 5 3)) (newline)

    ;comparison >= tests
    (display (>= 3 3)) (newline)
    (display (>= 5 3)) (newline)
    (display (>= 3 5)) (newline)
    
    ;comparison <> tests
    (display (<> 3 5)) (newline)
    (display (<> 5 5)) (newline)
)




