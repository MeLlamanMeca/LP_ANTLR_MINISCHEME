(define numberList '(1 2 3 4 5))
(define numberListCopy numberList)
(define boolList '(#t #t #f #t #f))
(define stringList '("text1" "text2" "text3"))
(define mixedLit '(1 2 #t #f "text1" "text2"))
(define emptyList '())

(define NUMBER 5)
(define BOOLEAN #t)
(define STRING "string")


(define (main)
    ; display lists
    (display numberList)
    (newline)
    (display numberListCopy)
    (newline)
    (display boolList)
    (newline)
    (display stringList)
    (newline)
    (display mixedLit)
    (newline)
    (display emptyList)
    (newline)

    ; display CAR lists
    (display (car numberList)) ; car [1 2 3 4 5] = 1
    (newline)
    (display (car numberListCopy)) ; car [1 2 3 4 5] = 1
    (newline)
    (display (car boolList)) ; car [#t #t #f #t #f] = #t
    (newline)
    (display (car stringList)) ; car ["text1" "text2" "text3"] = "text1"
    (newline)
    (display (car mixedLit)) ; car [1 2 #t #f "text1" "text2"] = 1
    (newline)
    (display (car emptyList)) ; car [] = []
    (newline)
    (display (car NUMBER)) ; car 5 = 5
    (newline)
    (display (car BOOLEAN)) ; car #t = #t
    (newline)
    (display (car STRING)) ; car "string" = "string"
    (newline)

    ; display CDR lists
    (display (cdr numberList)) ; cdr [1 2 3 4 5] = [2 3 4 5]
    (newline)
    (display (cdr numberListCopy)) ; cdr [1 2 3 4 5] = [2 3 4 5]
    (newline)
    (display (cdr boolList)) ; cdr [#t #t #f #t #f] = [#t #f #t #f]
    (newline)
    (display (cdr stringList)) ; cdr ["text1" "text2" "text3"] = ["text2" "text3"]
    (newline)
    (display (cdr mixedLit)) ; cdr [1 2 #t #f "text1" "text2"] = [2 #t #f "text1" "text2"]
    (newline)
    (display (cdr emptyList)) ; cdr [] = []
    (newline)
    (display (cdr NUMBER)) ; cdr 5 = []
    (newline)
    (display (cdr BOOLEAN)) ; cdr #t = []
    (newline)
    (display (cdr STRING)) ; cdr "string" = []
    (newline)

    ; display CONS lists
    (display (cons 0 numberList)) ; cons 0 [1 2 3 4 5] = [0 1 2 3 4 5]
    (newline)
    (display (cons #f boolList)) ; cons #f [#t #t #f #t #f] = [#f #t #t #f #t #f]
    (newline)
    (display (cons "newText" stringList)) ; cons "newText" ["text1" "text2" "text3"] = ["newText" "text1" "text2" "text3"]
    (newline)
    (display (cons 42 mixedLit)) ; cons 42 [1 2 #t #f "text1" "text2"] = [42 1 2 #t #f "text1" "text2"]
    (newline)
    (display (cons '() emptyList)) ; cons [] [] = [[]]
    (newline)
    (display (cons numberList boolList)) ; cons [1 2 3 4 5] [#t #t #f #t #f] = [[1 2 3 4 5] #t #t #f #t #f]
    (newline)
    (display (cons stringList mixedLit)) ; cons ["text1" "text2" "text3"] [1 2 #t #f "text1" "text2"] = [["text1" "text2" "text3"] 1 2 #t #f "text1" "text2"]
    (newline)
    (display (cons emptyList numberList)) ; cons [] [1 2 3 4 5] = [[] 1 2 3 4 5]
    (newline)
    (display (cons emptyList NUMBER)) ; cons [] 5 = [[] 5]
    (newline)
    (display (cons emptyList BOOLEAN)) ; cons [] #t = [[] #t]
    (newline)
    (display (cons emptyList STRING)) ; cons [] "string" = [[] "string"]
    (newline)

    ; display APPEND lists
    (display (append numberList boolList)) ; append [1 2 3 4 5] [#t #t #f #t #f] = [1 2 3 4 5 #t #t #f #t #f]
    (newline)
    (display (append stringList mixedLit)) ; append ["text1" "text2" "text3"] [1 2 #t #f "text1" "text2"] = ["text1" "text2" "text3" 1 2 #t #f "text1" "text2"]
    (newline)
    (display (append emptyList numberList)) ; append [] [1 2 3 4 5] = [1 2 3 4 5]
    (newline)
    (display (append numberList stringList)) ; append [1 2 3 4 5] ["text1" "text2" "text3"] = [1 2 3 4 5 "text1" "text2" "text3"]
    (newline)
    (display (append boolList emptyList)) ; append [#t #t #f #t #f] [] = [#t #t #f #t #f]
    (newline)
    (display (append (cons numberList emptyList) numberList)) ; append [[1 2 3 4 5]] [1 2 3 4 5] = [[1 2 3 4 5] 1 2 3 4 5]
    (newline)
    (display (append "text1" "text2")) ; append "text1" "text2" = [text1 text2]
    (newline)
    (display (append 5 4)) ; append 5 4 = [5 4]
    (newline)
    (display (append #f #t)) ; append #f #t = [#f #t]
    (newline)
    (display (append emptyList NUMBER)) ; cons [] 5 = [5]
    (newline)
    (display (append emptyList BOOLEAN)) ; append [] #t = [#t]
    (newline)
    (display (append emptyList STRING)) ; append [] "string" = ["string"]
    (newline)

    ; display NULL? lists
    (display (null? numberList)) ; null? [1 2 3 4 5] = False
    (newline)
    (display (null? numberListCopy)) ; null? [1 2 3 4 5] = False
    (newline)
    (display (null? boolList)) ; null? [#t #t #f #t #f] = False
    (newline)
    (display (null? stringList)) ; null? ["text1" "text2" "text3"] = False
    (newline)
    (display (null? mixedLit)) ; null? [1 2 #t #f "text1" "text2"] = False
    (newline)
    (display (null? emptyList)) ; null? [] = True
    (newline) 
    (display (null? (cons emptyList emptyList))) ; null? [[]] = False
    (newline)
    (display (null? NUMBER)) ; null? 5 = False
    (newline)
    (display (null? BOOLEAN)) ; null? #t = False
    (newline)
    (display (null? STRING)) ; null? "string" = False
    (newline)

    ; display LENGTH lists
    (display (length numberList)) ; length [1 2 3 4 5] = 5
    (newline)
    (display (length numberListCopy)) ; length [1 2 3 4 5] = 5
    (newline)
    (display (length boolList)) ; length [#t #t #f #t #f] = 5
    (newline)
    (display (length stringList)) ; length ["text1" "text2" "text3"] = 3
    (newline)
    (display (length mixedLit)) ; length [1 2 #t #f "text1" "text2"] = 6
    (newline)
    (display (length emptyList)) ; length [] = 0
    (newline)
    (display (length 5)) ; length 5 = 1
    (newline)
    (display (length (cons emptyList emptyList))) ; length [[]] = 1
    (newline)
    (display (length NUMBER)) ; length 5 = 1
    (newline)
    (display (length BOOLEAN)) ; length #t = 1
    (newline)
    (display (length STRING)) ; length "string" = 1
)
