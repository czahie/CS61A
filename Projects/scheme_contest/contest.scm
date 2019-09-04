;;; Scheme Recursive Art Contest Entry
;;;
;;; Please do not include your name or personal info in this file.
;;;
;;; Title: <Your title here>
;;;
;;; Description:
;;;   <It's your masterpiece.
;;;    Use these three lines to describe
;;;    its inner meaning.>
(define (draw)
  (drawfunc raytrace 0 (screen_width) (screen_height))
)


(define (drawfunc f y w h)
  (if (= y h)
    '()
    (begin
      (drawline f 0 y w)
      (drawfunc f (+ y 1) w h)
    )
  )
)

(define (fromto a b)
  (if (= a b)
    '()
    (cons a (fromto (+ a 1) b))
  )
)

(define (drawline f x y l)
  (if (= x l)
    '()
    (begin
      ; let's apply anti aliasing by rendering at 2x resolution then average them all
      (pixel x y (colorToRGB (scaleColor
        (addColors
          (f x y)
          (addColors
            (f (+ x 0.5) y)
            (addColors
              (f x (+ y 0.5))
              (f (+ x 0.5) (+ y 0.5))
            )
          )
        ) 0.25)))
      (drawline f (+ x 1) y l)
    )
  )
)

; type = 0 = no solutions
; type = 1 = one solution
; type = 2 = two solutions
(define quadratic_output_0 '(0))
(define (quadratic_output_1 sol1) (list 1 sol1))
(define (quadratic_output_2 sol1 sol2) (list 2 sol1 sol2))

(define (solve_quadratic a b c)
 (let
   (
     (discrim (- (* b b) (* 4 a c)))
   )
   (cond
     ((> discrim 0)
       (quadratic_output_2
         (/ (+ (- 0 b) (sqrt (- (* b b) (* 4 a c)))) (* 2 a))
         (/ (- (- 0 b) (sqrt (- (* b b) (* 4 a c)))) (* 2 a))
       )
     )
     ((= discrim 0)
       (quadratic_output_1
         (/ (- 0 b) (* 2 a))
       )
     )
     ((< discrim 0)
       quadratic_output_0
     )
   )
 )
)

(define (vec3 x y z)
 (list x y z)
)

(define (vecx vec)
 (car vec)
)

(define (vecy vec)
 (car (cdr vec))
)

(define (vecz vec)
 (car (cdr (cdr vec)))
)

(define (addvecs vec0 vec1)
 (vec3 (+ (vecx vec0) (vecx vec1)) (+ (vecy vec0) (vecy vec1)) (+ (vecz vec0) (vecz vec1)))
)

(define (subvecs vec0 vec1)
 (vec3 (- (vecx vec0) (vecx vec1)) (- (vecy vec0) (vecy vec1)) (- (vecz vec0) (vecz vec1)))
)

(define (scalevec vec scalar)
 (vec3 (* (vecx vec) scalar) (* (vecy vec) scalar) (* (vecz vec) scalar))
)

(define (dot vec0 vec1)
 (+ (* (vecx vec0) (vecx vec1)) (* (vecy vec0) (vecy vec1)) (* (vecz vec0) (vecz vec1)))
)

(define (square x) (* x x))

(define (scalar_product vec)
 (+ (square (vecx vec)) (square (vecy vec)) (square (vecz vec)))
)

(define (mag vec)
 (sqrt (scalar_product vec))
)

(define (ray origin direction)
 (list origin direction)
)

(define (origin ray)
 (car ray)
)

(define (direction ray)
 (car (cdr ray))
)

(define (object type data)
  (list type data)
)

(define (objecttype object)
  (car object)
)

(define (objectdata object)
  (car (cdr object))
)

(define (is_sphere object)
  (= (objecttype object) 0)
)

(define (is_plane object)
  (= (objecttype object) 1)
)

(define (is_cube object)
  (= (objecttype object) 2)
)

(define (cube extentMin extentMax c reflectiveness)
  (list extentMin extentMax c reflectiveness)
)

(define (cube_min c)
  (car c)
)

(define (cube_max c)
  (car (cdr c))
)

(define (cube_normal c p)
  (cond
    ((< (abs (- (vecx (cube_min c)) (vecx p))) 0.0000001) (vec3 -1 0 0))
    ((< (abs (- (vecy (cube_min c)) (vecy p))) 0.0000001) (vec3 0 -1 0))
    ((< (abs (- (vecz (cube_min c)) (vecz p))) 0.0000001) (vec3 0 0 -1))
    ((< (abs (- (vecx (cube_max c)) (vecx p))) 0.0000001) (vec3 1 0 0))
    ((< (abs (- (vecy (cube_max c)) (vecy p))) 0.0000001) (vec3 0 1 0))
    ((< (abs (- (vecz (cube_max c)) (vecz p))) 0.0000001) (vec3 0 0 1))
    ; (else (print c p))
  )
)

(define (cube_color c)
  (car (cdr (cdr c)))
)

(define (cube_ref c)
  (car (cdr (cdr (cdr c))))
)

(define (plane point normal)
  (list point normal)
)

(define (planePoint plane)
  (car plane)
)

(define (planeNormal plane)
  (car (cdr plane))
)

(define (sphere center r c reflectiveness)
  (list center r c reflectiveness)
)

(define (sphere_center sphere)
  (car sphere)
)

(define (sphere_r sphere)
  (car (cdr sphere))
)

(define (sphere_col sphere)
  (car (cdr (cdr sphere)))
)

(define (sphere_ref sphere)
  (car (cdr (cdr (cdr sphere))))
)

(define (newColor r g b)
  (list r g b)
)

(define (color_r c)
  (car c)
)

(define (color_g c)
  (car (cdr c))
)

(define (color_b c)
  (car (cdr (cdr c)))
)

(define (scaleColor c brightness)
  (newColor (* (color_r c) brightness) (* (color_g c) brightness) (* (color_b c) brightness))
)

(define (addColors a b)
  (newColor (+ (color_r a) (color_r b)) (+ (color_g a) (color_g b)) (+ (color_b a) (color_b b)))
)

(define (colorToRGB c)
  (rgb (if (> (color_r c) 0) (color_r c) 0) (if (> (color_g c) 0) (color_g c) 0) (if (> (color_b c) 0) (color_b c) 0))
)

(define (min a b) (if (> a b) b a))
(define (max a b) (if (> a b) a b))
(define (safediv n) (if (= n 0) 0.000001 n))

(define (intersect_ray ray object)
  (cond
    ((is_sphere object)
      (let
        (
          (L (addvecs (origin ray) (scalevec (sphere_center (objectdata object)) -1)))
        )
        (let
          (
            (out (solve_quadratic
              (scalar_product (direction ray))
              (* 2 (dot (direction ray) L))
              (- (scalar_product L) (square (sphere_r (objectdata object))))
            ))
          )
          (if (and (= (car out) 2) (> (car (cdr out)) (car (cdr (cdr out)))))
            (list (car out) (car (cdr (cdr out))) (car (cdr out)))
            out
          )
        )
      )
    )
    ((is_plane object)
      (let
        (
          (denom (dot (planeNormal (objectdata object)) (direction ray)))
        )
        (if (> (abs denom) 0.0000001)
          (quadratic_output_1 (/ (dot (subvecs (planePoint (objectdata object)) (origin ray)) (planeNormal (objectdata object))) denom))
          quadratic_output_0
        )
      )
    )
    ((is_cube object)
      (let
        (
          (m (cube_min (objectdata object)))
          (mx (cube_max (objectdata object)))
        )
        (define dirfrac (vec3 (/ 1 (safediv (vecx (direction ray)))) (/ 1 (safediv (vecy (direction ray)))) (/ 1 (safediv (vecz (direction ray))))))
        (define t1 (* (- (vecx m) (vecx (origin ray))) (vecx dirfrac)))
        (define t2 (* (- (vecx mx) (vecx (origin ray))) (vecx dirfrac)))
        (define t3 (* (- (vecy m) (vecy (origin ray))) (vecy dirfrac)))
        (define t4 (* (- (vecy mx) (vecy (origin ray))) (vecy dirfrac)))
        (define t5 (* (- (vecz m) (vecz (origin ray))) (vecz dirfrac)))
        (define t6 (* (- (vecz mx) (vecz (origin ray))) (vecz dirfrac)))
        (define tmin (max (max (min t1 t2) (min t3 t4)) (min t5 t6)))
        (define tmax (min (min (max t1 t2) (max t3 t4)) (max t5 t6)))
        (if (or (< tmax 0) (> tmin tmax))
          quadratic_output_0
          (quadratic_output_1 tmin) ; technically it intersects both tmin and tmax, but we don't really care
        )
      )
    )
  )
)


(define (doesRayIntersectTwoPoints quad_out)
  (cond
    ((= (car quad_out) 0) #f)
    ((= (car quad_out) 1) (> (car (cdr quad_out)) 0))
    ((= (car quad_out) 2) (and (> (car (cdr quad_out)) 0) (> (car (cdr (cdr quad_out))) 0))) ; we won't render it if the ray hits only one side
  )
)

(define (doesRayIntersectToPrecision quad_out prec)
  (cond
    ((= (car quad_out) 0) #f)
    ((= (car quad_out) 1) (> (car (cdr quad_out)) prec))
    ((= (car quad_out) 2) (and (> (car (cdr quad_out)) prec) (> (car (cdr (cdr quad_out))) prec))) ; we won't render it if the ray hits only one side
  )
)

; this should return the closest object that the ray intersects
(define (getObjectFromRayTraceOrNil ray objects)
  (define (getObjectFromRayTraceOrNilInner ray objects smallest_dist smallest_object) ; tail recursion, yay!
    (if (null? objects)
      (list smallest_object smallest_dist)
      (let
        (
          (quad_out (intersect_ray ray (car objects)))
        )
        ;(print quad_out)
        (if (and (doesRayIntersectTwoPoints quad_out) (< (car (cdr quad_out)) smallest_dist))
          (getObjectFromRayTraceOrNilInner ray (cdr objects) (car (cdr quad_out)) (car objects))
          (getObjectFromRayTraceOrNilInner ray (cdr objects) smallest_dist smallest_object)
        )
      )
    )
  )
  (getObjectFromRayTraceOrNilInner ray objects 1000 '())
)

(define (shouldShadow ray objects)
  (if (null? objects)
    #f
    (if (doesRayIntersectToPrecision (intersect_ray ray (car objects)) -0.1)
      #t
      (shouldShadow ray (cdr objects))
    )
  )
)

(define (delete item list)
    (cond
     ((= item (car list)) (cdr list))
     (else (cons (car list) (delete item (cdr list))))))

(define (getColor r objects light)
  (define (getColorInner r objects light rec)
    (let
      (
        (object (getObjectFromRayTraceOrNil r objects))
      )
      (if (null? (car object))
        (newColor 0 0 0)
        (let
          (
            (intersectionpoint (addvecs (origin r) (scalevec (direction r) (car (cdr object)))))
            (objectd (objectdata (car object)))
          )
          (define intensity (modulo (+ (floor (/ (vecx intersectionpoint) 5)) (floor (/ (vecz intersectionpoint) 5))) 2))
          (cond
            ((is_plane (car object))
              (define shadow (shouldShadow (ray (addvecs intersectionpoint (scalevec (planeNormal objectd) 0.1)) (normalize (subvecs light intersectionpoint))) objects))
              (define intensity (modulo (+ (floor (/ (vecx intersectionpoint) 5)) (floor (/ (vecz intersectionpoint) 5))) 2))
              (define shadowedIntensity (if shadow (* intensity 0.5) intensity))
              (newColor shadowedIntensity shadowedIntensity shadowedIntensity))
            ((is_sphere (car object))
              (define normal (normalize (addvecs intersectionpoint (scalevec (sphere_center objectd) -1))))
              (define shadow (shouldShadow (ray intersectionpoint (normalize (subvecs light intersectionpoint))) objects))
              (if (or (= rec 0) (= (sphere_ref objectd) 0))
                (if shadow
                  (scaleColor (sphere_col objectd) (* 0.5 (dot normal (scalevec (direction r) -1))))
                  (scaleColor (sphere_col objectd) (dot normal (scalevec (direction r) -1)))
                )
                (addColors
                  (scaleColor (sphere_col objectd) (* (- 1 (sphere_ref objectd)) (dot normal (scalevec (direction r) -1))))
                  (scaleColor (getColorInner
                    (ray intersectionpoint (normalize (subvecs (direction r) (scalevec normal (* 2 (dot (direction r) normal))))))
                    objects
                    light
                    (- rec 1)
                  ) (sphere_ref objectd))
                )
              )
            )
            ((is_cube (car object))
              (define normal (cube_normal objectd intersectionpoint))
              (define shadow (shouldShadow (ray (addvecs intersectionpoint (scalevec normal 0.01)) (normalize (subvecs light intersectionpoint))) objects))
              (if (or (= rec 0) (= (cube_ref objectd) 0))
                (if shadow
                  (scaleColor (cube_color objectd) (* 0.5 (dot normal (scalevec (direction r) -1))))
                  (scaleColor (cube_color objectd) (dot normal (scalevec (direction r) -1)))
                )
                (addColors
                  (scaleColor (cube_color objectd) (* (- 1 (cube_ref objectd)) (dot normal (scalevec (direction r) -1))))
                  (scaleColor (getColorInner
                    (ray intersectionpoint (normalize (subvecs (direction r) (scalevec normal (* 2 (dot (direction r) normal))))))
                    objects
                    light
                    (- rec 1)
                  ) (cube_ref objectd))
                )
              )
            )
          )
        )
      )
    )
  ) ; rec is how many bounces we allow light to make
  (getColorInner r objects light 2)
)

(define (normalize vec)
 (scalevec vec (/ 1 (mag vec)))
)


; camera is at (0 0 0) pointing at +x
(define (raytrace x y)
  (let
    (
      (spheres
        (list
          (object 1 (plane (vec3 0 -8 0) (vec3 0 1 0)))
          (object 2 (cube (vec3 4 -8 9) (vec3 4.5 -4 9.5) (newColor 1 0 0) 0))
          (object 2 (cube (vec3 4 -8 13) (vec3 4.5 -4 13.5) (newColor 1 0 0) 0))
          (object 2 (cube (vec3 -4 -8 13) (vec3 -4.5 -4 13.5) (newColor 1 0 0) 0))
          (object 2 (cube (vec3 -4 -8 9) (vec3 -4.5 -4 9.5) (newColor 1 0 0) 0))
          (object 2 (cube (vec3 -5 -4 8.5) (vec3 -1.6667 -3.5 14) (newColor 1 0 0) 0))
          (object 2 (cube (vec3 -1.6667 -4 8.5) (vec3 1.6667 -3.5 14) (newColor 0 1 0) 0))
          (object 2 (cube (vec3 1.6667 -4 8.5) (vec3 5 -3.5 14) (newColor 0 0 1) 0))
          (object 0 (sphere (vec3 0 -1.5 11.25) 2 (newColor 0.2 0.2 0.7) 0.5))
          (object 0 (sphere (vec3 -3 -2.5 11.25) 1 (newColor 0.2 0.7 0.2) 0.5))
          (object 0 (sphere (vec3 3 -2.5 11.25) 1 (newColor 0.7 0.2 0.2) 0.5))
        )
      )
      (i (* (- (/ x (screen_width)) 0.5) 2))
      (j (* (- (/ y (screen_height)) 0.5) 2))
    )
    (getColor (ray (vec3 0 0 0) (normalize (vec3 i j 1))) spheres (vec3 0 9 5))
  )
)

;  (exitonclick))

; Please leave this last line alone.  You may add additional procedures above
; this line.
(draw)