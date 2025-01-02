(define (main) 
    ;arithmetic + tests
    (display (+ 3 3)) (newline)
    (display (+ 3 5 2 0)) (newline)
    (display (+ 0 0 0 0)) (newline)

    ;arithmetic - tests
    (display (- 3 0)) (newline)
    (display (- 3 5 2 0)) (newline)
    (display (- 0 0 0 0)) (newline)

    ;arithmetic * tests
    (display (* 3 1)) (newline)
    (display (* 3 5 2 1)) (newline)
    (display (* 3 5 2 0)) (newline)

    ;arithmetic / tests
    (display (/ 3 1)) (newline)
    (display (/ 30 2 5 3)) (newline)

    ;;arithmetic MOD tests
    (display (mod 3 2)) (newline)
    (display (mod 10 3)) (newline)
    (display (mod 20 5)) (newline)
    (display (mod 19 10 5 3)) (newline)

    ;arithmetic ^ tests
    (display (^ 2 3)) (newline)
    (display (^ 5 2 3)) (newline)

    ;arithmetic MAX tests
    (display (max 3 5)) (newline)
    (display (max 10 20 30)) (newline)
    (display (max 1 2 3 4 5)) (newline)

    ;arithmetic MIN tests
    (display (min 3 5)) (newline)
    (display (min 10 20 30)) (newline)
    (display (min 1 2 3 4 5)) (newline)
)