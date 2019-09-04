;;; Scheme Recursive Art Contest Entry
;;;
;;; Please do not include your name or personal info in this file.
;;;
;;; Title: Recursive CS61A
;;;
;;; Description:
;;;   CS61A

; list manipuation
(define (cadr s) (car (cdr s)))
(define (cddr s) (cdr (cdr s)))

; utility functions
(define (reverse s)
  (define (helper s sofar)
    (if (null? s)
        sofar
        (helper (cdr s) (cons (car s) sofar))))
  (helper s ()))

(define (map f s)
  (define (map-reverse s result)
    (if (null? s)
        result
        (map-reverse (cdr s) (cons (f (car s)) result))))
  (reverse (map-reverse s ())))

(define (foldl value s f)
  (if (null? s)
      value
      (foldl (f value (car s)) (cdr s) f)))

(define (range start stop step)
  (define (helper x result)
    (if (> x stop)
        result
        (helper (+ x step) (cons x result))))
  (reverse (helper start ())))

(define (zip s1 s2)
  (define (helper s1 s2 result)
    (if (null? s1)
        result
        (helper (cdr s1) (cdr s2) (cons (cons (car s1) (car s2)) result))))
  (reverse (helper s1 s2 ())))

; for macro
(define-macro (for formal iterable body)
  (list 'map (list 'lambda (list formal) body) iterable))

; for-to macro
(define (for-to-impl start end step f)
    (if (> start end)
        '()
        (begin (f start) (for-to-impl (+ start step) end step f))))
(define-macro (for-to formal start end step body)
  (list 'for-to-impl start end step (list 'lambda (list formal) body)))

; vector manipulation
(define (length p)
  (sqrt (+ (* (car p) (car p)) (* (cdr p) (cdr p)))))

(define (add-vector p q)
  (cons (+ (car p) (car q)) (+ (cdr p) (cdr q))))
(define (subtract-vector p q)
  (cons (- (car p) (car q)) (- (cdr p) (cdr q))))
(define (multiply-vector a p)
  (cons (* a (car p)) (* a (cdr p))))

(define (inner-point p q t)
  (add-vector (multiply-vector (- 1 t) p)
             (multiply-vector t q)))

(define (dot-product p q)
  (+ (* (car p) (car q)) (* (cdr p) (cdr q))))

; matrix opertion
; a matrix is represented as ((a11 . a12) a21 . a22)
(define (apply-matrix A p)
  (cons (dot-product (car A) p) (dot-product (cdr A) p)))

(define (multiply-matrix A B)
  (let ((a11 (car (car A)))
        (a12 (cdr (car A)))
        (a21 (cadr A))
        (a22 (cddr A))
        (b11 (car (car B)))
        (b12 (cdr (car B)))
        (b21 (cadr B))
        (b22 (cddr B)))
       (cons
         (cons (+ (* a11 b11) (* a12 b21)) (+ (* a11 b12) (* a12 b22)))
         (cons (+ (* a21 b11) (* a22 b21)) (+ (* a21 b12) (* a22 b22))))))

(define (rotation-matrix rad)
  (cons
    (cons (cos rad) (- (sin rad)))
    (cons (sin rad) (cos rad))))

(define (scale-matrix scale)
  (cons
    (cons scale 0)
    (cons 0 scale)))

(define identity (scale-matrix 1))

(define (matrix-to-function mat)
  (lambda (x) (apply-matrix mat x)))

; retrieve a corresponding point to t in the bezier curve according to the given control points
; control-points is a four-length list of pairs, which represents the coordinates
(define (bezier-point origin transform control-points t)
  (let ((A (matrix-to-function transform)))
       (let ((control-points (map A control-points)))
            (let ((bp (car control-points))
                  (bcp (cadr control-points))
                  (ecp (cadr (cdr control-points)))
                  (ep (cadr (cdr (cdr control-points)))))
                 (let ((bp-bcp (inner-point bp bcp t))
                       (bcp-ecp (inner-point bcp ecp t))
                       (ecp-ep (inner-point ecp ep t)))
                      (let ((bp-bcp-ecp (inner-point bp-bcp bcp-ecp t))
                            (bcp-ecp-ep (inner-point bcp-ecp ecp-ep t)))
                           (add-vector origin (inner-point bp-bcp-ecp bcp-ecp-ep t))))))))

; the length of the bezier curve specified by the given control points
(define (bezier-length control-points)
  (foldl 0 (range 0 1 0.1)
    (lambda (value t)
      (let ((current (bezier-point (cons 0 0) identity control-points t))
            (next (bezier-point (cons 0 0) identity control-points (+ t 0.1))))
        (+ value (length (subtract-vector next current)))))))

; draw a bezier curve according to the given control points
(define (draw-bezier line origin transform control-points len)
  (let ((bezier-speed (/ 25 len)))
    (for-to t 0 (- 1 (/ bezier-speed 2)) bezier-speed
     (line (bezier-point origin transform control-points t) (bezier-point origin transform control-points (+ t bezier-speed))))))

; primitive draw functions
(define control-points-c
  '(
    ((0 . 0) (0 . 50) (0 . 100) (40 . 100))
    ((30 . 100) (60 . 100) (80 . 100) (80 . 50))
    ((0 . 0) (0 . -50) (0 . -100) (40 . -100))
    ((30 . -100) (60 . -100) (80 . -100) (80 . -50))
   ))
(define length-c
  (map bezier-length control-points-c))
(define (draw-c line origin transform)
  (for x (zip control-points-c length-c)
    (draw-bezier line origin transform (car x) (cdr x))))

(define control-points-s
  '(((80 . 50) (80 . 75) (80 . 100) (120 . 100))
  ((120 . 100) (140 . 100) (160 . 100) (160 . 50))
  ((80 . 50) (80 . 0) (110 . 0) (120 . 0))
  ((120 . 0) (130 . 0) (160 . 0) (160 . -50))
  ((80 . -50) (80 . -75) (80 . -100) (130 . -100))
  ((120 . -100) (140 . -100) (160 . -100) (160 . -50))))
(define length-s
  (map bezier-length control-points-s))
(define (draw-s line origin transform)
  (for x (zip control-points-s length-s)
    (draw-bezier line origin transform (car x) (cdr x))))

(define control-points-6
  '(((160 . 0) (160 . 50) (160 . 100) (200 . 100))
  ((190 . 100) (220 . 100) (240 . 100) (240 . 40))
  ((160 . 0) (160 . -50) (160 . -100) (200 . -100))
  ((190 . -100) (220 . -100) (240 . -100) (240 . -40))
  ((240 . -40) (240 . 0) (210 . 0) (200 . 0))
  ((200 . 0) (190 . 0) (160 . 0) (162 . -45))))
(define length-6
  (map bezier-length control-points-6))
(define (draw-6 line origin transform)
  (for x (zip control-points-6 length-6)
    (draw-bezier line origin transform (car x) (cdr x))))

(define control-points-1
  '(((240 . 40) (240 . 40) (280 . 100) (280 . 100))
  ((280 . 100) (280 . 100) (280 . -100) (280 . -100))
  ((240 . -100) (240 . -100) (320 . -100) (320 . -100))))
(define length-1
  (map bezier-length control-points-1))
(define (draw-1 line origin transform)
  (for x (zip control-points-1 length-1)
    (draw-bezier line origin transform (car x) (cdr x))))

(define control-points-a
  '(((320 . -100) (340 . 0) (340 . 40) (360 . 100))
  ((400 . -100) (380 . 0) (380 . 40) (360 . 100))
  ((335 . -20) (360 . -10) (360 . -10) (385 . -20))))
(define length-a
  (map bezier-length control-points-a))
(define (draw-a line origin transform)
  (for x (zip control-points-a length-a)
    (draw-bezier line origin transform (car x) (cdr x))))

(define (draw-cs61a line origin transform)
  (color (symbol-to-string 'red))
  (draw-c line origin transform)
  (color (symbol-to-string 'orange))
  (draw-s line origin transform)
  (color (symbol-to-string 'green))
  (draw-6 line origin transform)
  (color (symbol-to-string 'blue))
  (draw-1 line origin transform)
  (color (symbol-to-string 'purple))
  (draw-a line origin transform))

(define (line-cs61a start end)
  (let ((direction (subtract-vector end start)))
    (let ((scale (scale-matrix (/ (length direction) 400)))
          (rotation (rotation-matrix (atan2 (cdr direction) (car direction)))))
      (let ((transform (multiply-matrix scale rotation)))
        (draw-cs61a line start transform)))))

(define (draw)
  (speed 0)
  (draw-cs61a line-cs61a (cons -400 0) (scale-matrix 2))
  (exitonclick))

; Please leave this last line alone.  You may add additional procedures above
; this line.
(draw)