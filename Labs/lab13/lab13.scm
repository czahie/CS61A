;; Scheme ;;
(define (compose-all funcs)
 (lambda (x)
  (if (null? funcs)
   x
   ((compose-all (cdr funcs)) ((car funcs) x))
  )
 )
)

(define (deep-map fn s)
 (cond
  ((null? s) nil)
  ((list? (car s)) (cons (deep-map fn (car s)) (deep-map fn (cdr s))))
  (else (cons (fn (car s)) (deep-map fn (cdr s))))
 )
)
