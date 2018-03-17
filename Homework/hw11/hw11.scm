(define (find s predicate)
  'YOUR-CODE-HERE
 (if (null? s)
  #f
  (if (eq? (predicate (car s)) #t)
   (car s)
   (find (cdr-stream s) predicate)))
)

(define (scale-stream s k)
  'YOUR-CODE-HERE
 (cond
  ((null? s) ())
  (else (cons-stream (* (car s) k) (scale-stream (cdr-stream s) k))))
)

(define (has-cycle s)
  'YOUR-CODE-HERE
 (define (in? lst s)  ;Check if stream s is in list lst
  (cond
   ((null? lst) #f)
   ((eq? (car lst) s) #t)
   (else (in? (cdr lst) s))))

 (define (has-cycle-helper memo s)
   (cond
    ((null? s) #f)
    ((in? memo s) #t)
    (else (has-cycle-helper (cons s memo) (cdr-stream s)))))

 (has-cycle-helper nil s)

)
(define (has-cycle-constant s)
  'YOUR-CODE-HERE
 (define (has-cycle-constant-helper fast slow)
  (cond
   ((or (null? fast) (null? slow)) #f)
   ((eq? fast slow) #t)
   ((null? (cdr-stream fast)) #f)  ;If (cdr-stream fast) is nil, then the next line would cause an error
   (else (has-cycle-constant-helper (cdr-stream (cdr-stream fast)) (cdr-stream slow)))))

 (has-cycle-constant-helper (cdr-stream s) s)

)

;; Official solution

(define (has-cycle-constant s)
  (let ((slow s)
        (fast (cdr-stream s)))
       (cycle-stepper slow fast)
  )
)
(define (cycle-stepper slow fast)
  (cond ((or (null? fast) (null? (cdr-stream fast))) #f)
        ((eq? fast slow) #t)
        (else (cycle-stepper (cdr-stream slow) (cdr-stream (cdr-stream fast))))
  )
)