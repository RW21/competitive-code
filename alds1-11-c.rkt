#lang racket

(require data/queue)

(define G (read))

(define graph
  (for/hash ([_ (in-range 0 G)])
	    (match (map string->number (string-split (read-line)))
		   [(list a _ (? number? b) ...) (values a (list #f +inf.0 b))]
		   [(list 1 _ (? number? b) ...) (values 1 (list #f 0 b))]
		   [_ empty]
		   )))

(display graph)

#| (define queue (make-queue)) |#

#| (define (solve g) |#
#|   (let bfs |# 
#|     ([l graph]) |#
#|     (cond |#
#|       [(empty? l) l] |#
#|       [else ( |#
	    
