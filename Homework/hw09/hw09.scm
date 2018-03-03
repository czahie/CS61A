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
 (if (number? s)
  (cons s nil)
  (if (or (null? s) (null? (cdr s)))
   s
   (if (pair? (car s))
    (cons (nodots (car s)) (nodots (cdr s)))
    (if (pair? (cdr s))
     (cons (car s) (nodots (cdr s)))
     (list (car s) (cdr s))
   ))))
)

; Sets as sorted lists

(define (empty? s) (null? s))

(define (contains? s v)
    (cond ((empty? s) #f)
          'YOUR-CODE-HERE
          (else nil) ; replace this line
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
          'YOUR-CODE-HERE
          (else nil) ; replace this line
          ))

(define (intersect s t)
    (cond ((or (empty? s) (empty? t)) nil)
          'YOUR-CODE-HERE
          (else nil) ; replace this line
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
          'YOUR-CODE-HERE
          (else nil) ; replace this line
          ))