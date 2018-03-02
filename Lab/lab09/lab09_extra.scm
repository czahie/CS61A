;; Extra Scheme Questions ;;


; Q5
(define lst
 (list (list 1) 2 (cons 3 4) 5)
)

; Q6
(define (composed f g)
 (define (h x)
  (f (g x)))
 h
)

; Q7
(define (remove item lst)
 (filter (lambda (x) (not (= item x))) lst)
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

; Q8
(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))
(define (gcd a b)
 (define x (max a b))
 (define y (min a b))
 (if(or (= a 0) (= b 0))
  x
  (if (= (modulo x y) 0)
   y
   (gcd y (modulo x y))))
)

;;; Tests
(gcd 24 60)
; expect 12
(gcd 1071 462)
; expect 21

; Q9
(define (no-repeats s)
 (if (null? s)
  s
  (cons (car s)
   (no-repeats (filter (lambda (x) (not (= x (car s)))) (cdr s)))))
)

; Q10
(define (substitute s old new)
 (if (null? s)
  s
  (if (eq? (car s) old)
   (cons new (substitute (cdr s) old new))
   (if (pair? (car s))
    (cons (substitute (car s) old new) (substitute (cdr s) old new))
    (cons (car s) (substitute (cdr s) old new)))))
)

; Q11
(define (sub-all s olds news)
 (if (or (null? s) (null? olds))
  s
  (sub-all (substitute s (car olds) (car news)) (cdr olds) (cdr news)))
)