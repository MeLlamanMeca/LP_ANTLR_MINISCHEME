(define (suma x y)
  (+ x y))

(define x 5)

(define llista '(1 2 3 4 5))

(define (suma-llista llista)
  (if (null? llista)
      0
      (+ (car llista) (suma-llista (cdr llista)))))

(define (aplica-dos-cops f x)
  (f (f x)))

(define (dobla x) (* x 2))

(define (map func llista)
  (cond
    ((null? llista) '())
    (else (cons (func (car llista)) (map func (cdr llista))))))

(define (filter predicat llista)
  (cond
    ((null? llista) '())  ;
    ((predicat (car llista))
     (cons (car llista) (filter predicat (cdr llista))))
    (#t (filter predicat (cdr llista)))))  

(define (parell? x) (= (mod x 2) 0))

(define (main)

    ; basic sintaxis
    (display(+ (* 2 3) 5)) ; 11
    (newline)

    ; function definition
    (display (suma 3 4)) ; 7
    (newline)

    ; constant definition
    (display x) ; 5
    (newline)

    ; conditionals
    (display (if (> 3 2) "sí" "no")) ; sí
    (newline)

    ; multiple conditionals
    (display (cond ((> 3 5) "major") ((< 3 5) "menor") (#t "igual"))) ; menor
    (newline)

    ; list
    (display llista) ; (1 2 3 4 5)
    (newline)
    (display(car llista)) ; 1
    (newline)
    (display(cdr llista)) ; (2 3 4 5)
    (newline)
    (display(cons 0 llista)) ; (0 1 2 3 4 5)
    (newline)
    (display(null? '())) ; True
    (newline)
    (display(null? llista)) ; False
    (newline)

    ; recursivity
    (display (suma-llista llista)) ; 15
    (newline)

    ; local constants
    (display (let ((x 5) (y 3)) (+ x y)))  ; 8
    (newline)

    ; booleans
    (display (and (> 3 2) (< 5 10))); True
    (newline)
    (display (or (> 3 2) (< 1 0))); True
    (newline)
    (display (not (> 3 2))); False
    (newline)

    ; Higher-order functions
    (display (aplica-dos-cops dobla 5)) ; 20
    (newline)
    (display (map dobla '(1 2 3 4))) ; (2 4 6 8)
    (newline)
    (display (filter parell? '(1 2 3 4))) ; (2 4)





)