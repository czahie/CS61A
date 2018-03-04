(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  'YOUR-CODE-HERE
 (car (cdr s))
)

(define (caddr s)
 'YOUR-CODE-HERE
 (car (cddr s))
)

(define (sign x)
  'YOUR-CODE-HERE
 (cond
  ((< x 0) -1)
  ((= x 0) 0)
  ((> x 0) 1))
)

(define (square x) (* x x))

(define (pow b n)
  'YOUR-CODE-HERE
 (if (= n 0)
   1
   (if (even? n)
    (pow (square b) (/ n 2))
    (* b (pow (square b) (/ (- n 1) 2)))))
)

(define (ordered? s)
  'YOUR-CODE-HERE
 (if (or (null? s) (null? (cdr s)))
  #t
  (if (<= (car s) (cadr s))
   (ordered? (cdr s))
   #f))
)

(define (nodots s)
  (if (or (null? s) (null? (cdr s)))
   s
   (cond
    ((and (pair? (car s)) (pair? (cdr s))) (cons (nodots (car s)) (nodots (cdr s))))
    ((and (not (pair? (car s))) (pair? (cdr s))) (cons (car s) (nodots (cdr s))))
    ((and (pair? (car s)) (not (pair? (cdr s)))) (cons (nodots (car s)) (cons (cdr s) nil)))
    (else (list (car s) (cdr s)))
   ))
)

; Official solution
(define (nodots s)
  (define (dotted s) (and (pair? s)
                          (not (or (pair? (cdr s))
                                   (null? (cdr s))))))
  (cond ((null? s) s)
        ((dotted s) (list (nodots (car s)) (cdr s)))
        ((pair? s) (cons (nodots (car s)) (nodots (cdr s))))
        (else s))

  ; Alternate solution
  (define (dotted s) (and (pair? s)
                          (not (or (pair? (cdr s))
                                   (null? (cdr s))))))

  (define (car-number s) (not (pair? (car s))))

  (cond ((null? s) s)
        ((and (dotted s) (car-number s)) (list (car s) (cdr s)))
        ((dotted s) (list (nodots (car s)) (cdr s)))
        ((and (pair? s) (car-number s) (cons (car s) (nodots (cdr s)))))
        ((pair? s) (cons (nodots (car s)) (nodots (cdr s)))))
)


; Sets as sorted lists

(define (empty? s) (null? s))

(define (contains? s v)
    (cond ((empty? s) #f)
          ((< v (car s)) #f)
          ((= v (car s)) #t)
          (else (contains? (cdr s) v))
          ))

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return s is Link.empty
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)

(define (add s v)
    (cond ((empty? s) (list v))
          ((= v (car s)) s)
          ((< v (car s)) (cons v s))
          ((and (> v (car s)) (empty? (cdr s))) (cons (car s) (cons v nil)))
          ((and (> v (car s)) (< v (cadr s))) (cons (car s) (cons v (cdr s))))
          (else (cons (car s) (add (cdr s) v)))
          ))

(define (intersect s t)
    (cond ((or (empty? s) (empty? t)) nil)
          ((= (car s) (car t)) (cons (car s) (intersect (cdr s) (cdr t))))
          ((< (car s) (car t)) (intersect (cdr s) t))
          (else (intersect s (cdr t)))
          ))

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
    (cond ((empty? s) t)
          ((empty? t) s)
          ((= (car s) (car t)) (cons (car s) (union (cdr s) (cdr t))))
          ((< (car s) (car t)) (cons (car s) (union (cdr s) t)))
          (else (cons (car t) (union s (cdr t))))
          ))