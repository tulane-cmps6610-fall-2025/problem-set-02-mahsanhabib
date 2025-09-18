# CMPS 6610 Problem Set 02

**Name:** Md. Ahsan habib

In this assignment we'll work on applying the methods we've learned to
analyze recurrences, and also see their behavior in practice. As with
previous assignments, some of of your answers will go in
`main.py`. Please add your written answers to `answers.md` which you can convert
to a PDF using `convert.sh`. Alternatively, you may scan and upload written answers
to a file named `answers.pdf`. 


1. Prove that $\log n! \in \Theta(n \log n).$

  - *Answer:*
    - To prove $\log n! \in \Theta(n \log n)$, we need to find $c_1 > 0$, $c_2 > 0$ and a number $n_0$ such that $c_1 \cdot n \log n \le \log n! \le c_2 \cdot n \log n$ for all $n \ge n_0$. 

    - Let's express $\log \ n!$ as a sum: $\log \ n! = \log n \ +  \log n - 1 \ + \cdot \cdot \cdot \ +  \log 2 \ +  \log 1$
    
    - To determine the upper bound, we can easily find that, 
    $\log n! = \sum_{k=1}^{n} \log k \le \sum_{k=1}^{n} \log n = n \log n$. So, for $c_2 \ge 1$ and $n_0 \ge 1$, we can have: $\log n! \in O(n \log n)$.

    - To determine the lower bound, if we set  $c_1 = \frac{1}{2}$ and $n_0 \ge 1$, then we can find, 
    $n \log n = \sum_{k=1}^{n} \log n \le \sum_{k=1}^{n} \log k = \log n!$. So, for $c_1 = \frac{1}{2}$ and $n_0 \ge 1$, we can have: $\log n! \in \Omega(n \log n)$.
    
    - So, we can say: $\log n! \in \Theta(n \log n).$
 
2. Derive asymptotic upper bounds for each recurrence below, using a method of your choice.
   
  * $T(n)=2 \cdot T(n/6)+1$
  - *Answer:*
      - Using *brick* method, 
        - **Work:**
          - $W(n)=2 \cdot W(n/6)+1$ \
          $= 2^2 \cdot W(n/6^2) + 2 + 1 $ \
          $= 2^3 \cdot W(n/6^3) + 2^2 + 2 + 1 $ \
          $ \cdot \cdot \cdot $ 
                
          - Here, number of leaf nodes, $L = 2^{log_6n} = n^{log_62}$.
          As, it is leaf dominated, upper bound: $O(n^{log_62})$.

        - **Span:**
          - $S(n)=S(n/6)+1$ \
          $= S(n/6^2) + 1 + 1 $ \
          $= S(n/6^3) + 1 + 1 + 1 $ \
          $ \cdot \cdot \cdot $ 
          - At each recursion level, the additional work outside the recursive calls is constant, i.e., $O(1)$. Since the recursion depth is $O(\log_6 n) = O(\log n)$, the total span is: $S(n) = O(\log n).$



  * $T(n)=6 \cdot T(n/4)+n$
  - *Answer:*
    - Using *brick* method, 
        - **Work:**
            - $W(n)=6 \cdot W(n/4) + n$ \
            $= 6^2 \cdot W(n/4^2) + 6n/4 + n $ \
            $= 6^3 \cdot W(n/4^3) + 6^2n/4^2 + 6n/4 + n $ \
            $ \cdot \cdot \cdot $ 
            
            - Here, number of leaf nodes, $L = 6^{\log_4 n} = n^{\log_4 6}$.
            As, it is leaf dominated, upper bound: $O(n^{\log_4 6})$.

        - **Span:**
            - $S(n)=S(n/4)+n$ \
            $= S(n/4^2) + n/4 + n $ \
            $= S(n/4^3) + n/4^2 + n/4 + n $ \
            $ \cdot \cdot \cdot $ 
            
            - This forms a geometric series: $n + n/4 + n/4^2 + \dots = O(n)$.
            - As, it is root dominated, upper bound is: $O(n)$.
  

  * $T(n)=7 \cdot T(n/7)+n$
  - *Answer:*
    - Using *brick* method, 
        - **Work:**
            - $W(n)=7 \cdot W(n/7)+n$ \
            $= 7^2 \cdot W(n/7^2) + n + n $ \
            $= 7^3 \cdot W(n/7^3) + n + n + n $ \
            $ \cdot \cdot \cdot $ 
            
            - Here, number of levels, $l = \log_7 n$.
            As, it is balanced, upper bound is: $O(\# levels \cdot cost \ per \ level) = O(n \ \log_7 n)$.

        - **Span:**
            - $S(n)=S(n/7)+n$ \
            $= S(n/7^2) + n/7 + n $ \
            $= S(n/7^3) + n/7^2 + n/7 + n $ \
            $ \cdot \cdot \cdot $ 
            
            - This forms a geometric series: $n + n/7 + n/7^2 + \dots = O(n)$.
            - As, it is root dominated, upper bound is: $O(n)$.
  
  

  * $T(n)=9 \cdot T(n/4)+n^2$
  - *Answer:*
    - Using *brick* method, 
        - **Work:**
            - $W(n)=9 \cdot W(n/4)+n^2$ \
            $= 9^2 \cdot W(n/4^2) + 9n^2/4^2 + n^2 $ \
            $= 9^3 \cdot W(n/4^3) + 9^2n^2/4^4 + 9n^2/4^2 + n^2 $ \
            $ \cdot \cdot \cdot $ 
            
            As, it is root dominated, upper bound: $O(n^2)$.

        - **Span:**
            - $S(n)=S(n/4)+n^2$ \
            $= S(n/4^2) + n^2/4^2 + n^2 $ \
            $= S(n/4^3) + n^2/4^3 + n^2/4^2 + n^2 $ \
            $ \cdot \cdot \cdot $ 
            
            - As, it is root dominated, upper bound: $O(n^2)$.

  

  * $T(n)=4 \cdot T(n/2)+n^3$
  - *Answer:*
    - Using *brick* method, 
        - **Work:**
            - $W(n)=4 \cdot W(n/2)+n^3$ \
            $= 4^2 \cdot W(n/2^2) + 4n^3/2^3 + n^3 $ \
            $= 4^3 \cdot W(n/2^3) + 4^2n^3/2^6 + 4n^3/2^3 + n^3 $ \
            $ \cdot \cdot \cdot $ 
            
            - Here, number of leaf nodes, $L = 4^{\log_2 n} = n^{\log_2 4} = n^2$.
            - As, it is root dominated, upper bound: $O(n^3)$.

        - **Span:**
            - $S(n)=S(n/2)+n^3$ \
            $= S(n/2^2) + n^3/2^3 + n^3 $ \
            $= S(n/2^3) + n^3/2^6 + n^3/2^3 + n^3 $ \
            $ \cdot \cdot \cdot $ 
            
            - As, it is root dominated, so the upper bound is $O(n^3)$.



  * $T(n)=49 \cdot T(n/25)+n^{3/2}\log n$
  - *Answer:*
    - Using *brick* method, 
        - **Work:**
            - $W(n)=49 \cdot W(n/25)+n^{3/2}\log n$ \
            $= 49^2 \cdot W(n/25^2) + 49(n/25)^{3/2}\log (n/25) + n^{3/2}\log n $ \
            $= 49^3 \cdot W(n/25^3) + 49^2(n/25^2)^{3/2}\log (n/25^2) + 49(n/25)^{3/2}\log (n/25) + n^{3/2}\log n $ \
            $ \cdot \cdot \cdot $ 
            
            - As, it is root dominated, upper bound is $O(n^{3/2} \log \ n)$.

        - **Span:**
            - $S(n)=S(n/25)+n^{3/2}\log n$ \
            $= S(n/25^2) + (n/25)^{3/2}\log (n/25) + n^{3/2}\log n $ \
            $= S(n/25^3) + (n/25^2)^{3/2}\log (n/25^2) + (n/25)^{3/2}\log (n/25) + n^{3/2}\log n  $ \
            $ \cdot \cdot \cdot $ 
            
            - The span is also dominated by the root, so the upper bound is $O(n^{3/2}\log n)$.



  * $T(n)=T(n-1)+2$
  - *Answer:*
    - Using *brick* method, 
        - **Work:**
            - $W(n)=W(n-1)+2$ \
            $= W(n-2) + 2 + 2$ \
            $= W(n-3) + 2+2+2 $ \
            $ \cdot \cdot \cdot $ 
            
            - Here, the recurrence is linear and sequential, after $n$ steps, we will get $W(n) = O(2n)$. So the upper bound: $O(n)$.

        - **Span:**
            - $S(n)=S(n-1)+2$ \
            $= S(n-2) + 2 + 2$ \
            $= S(n-3) + 2 + 2 + 2 $ \
            $ \cdot \cdot \cdot $ 
            
            - The upper bound of span is also $O(n)$.



  * $T(n)= T(n-1)+n^c$, with $c\geq 1$
  - *Answer:*
    - Using *brick* method, 
        - **Work:**
            - $W(n)=W(n-1)+n^c$ \
            $= W(n-2) + (n-1)^c + n^c$ \
            $= W(n-3) + (n-2)^c + (n-1)^c + n^c $ \
            $ \cdot \cdot \cdot $ 
            
            - As, it is a decrease-by-one recurrence, and the recursion tree is a chain of length $n$, the upper bound: $O(n \cdot n^c) = O(n^{c+1})$.

        - **Span:**
            - $S(n)=S(n-1)+n^c$ \
            $= S(n-2) + (n-1)^c + n^c$ \
            $= S(n-3) + (n-2)^c + (n-1)^c + n^c $ \
            $ \cdot \cdot \cdot $ 
            
            - The span is the sum of the additive terms, so the upper bound is $O(n^{c+1}) = O(n^{c+1})$.



  * $T(n)=T(\sqrt{n})+1$
  - *Answer:*
    - Using *brick* method, 
        - **Work:**
            - $W(n)=W(\sqrt{n})+1$ \
            $= W(\sqrt{\sqrt{n}}) + 1 + 1$ \
            $= W(\sqrt{\sqrt{\sqrt{n}}}) + 1 + 1 + 1$ \
            $ \cdot \cdot \cdot $ 
            
            - Levels: If at each level we go like $(n \to \sqrt{n} \to \sqrt{\sqrt{n}} \to \cdot \cdot \cdot \to 2)$, then after k steps: $n^{\frac{1}{2^k}} = 2$. So, $\frac{1}{2^k} \cdot log \ n = log \ 2$.
            - So, the number of levels is $\log_2 \log n$, so the total work is $O(\log \ \log \ n)$.

        - **Span:**
            - $S(n)=S(\sqrt{n})+1$ \
            $= S(\sqrt{\sqrt{n}}) + 1 + 1$ \
            $= S(\sqrt{\sqrt{\sqrt{n}}}) + 1 + 1 + 1$ \
            $ \cdot \cdot \cdot $ 
            
            - The span is also $O(\log \ \log \ n)$.



3. Suppose that for a given task you are choosing between the following three algorithms:

	* Algorithm $\mathcal{A}$ solves problems by dividing them into
      two subproblems of one fifth of the input size, recursively
      solving each subproblem, and then combining the solutions in quadratic time.
	  
	* Algorithm $\mathcal{B}$ solves problems of size $n$ by
      recursively one subproblems of size $n-1$ and then
      combining the solutions in logarithmic time.
		
	* Algorithm $\mathcal{C}$ solves problems of size $n$ by dividing
      them into a subproblems of size $n/3$ and a subproblem of size
      $2n/3$, recursively solving each subproblem, and then combining
      the solutions in $O(n^{1.1})$ time.

    What is the work and span of these algorithms? For the span, just
    assume that it is the same as the work to combine solutions
    (i.e. the non-recursive quantity).
    Which algorithm would you choose? Why?
  
  - *Answer:*
    - For algorithm $\mathcal{A}$, the work and span are as follows using *brick* method, 
      - **Work:**
        - $W(n)=2 \cdot W(n/5)+ n^2$ \
        $= 2^2 \cdot W(n/5^2) + 2n^2/5^2 + n^2 $ \
        $= 2^3 \cdot W(n/5^3) + 2^2n^2/5^4  + 2n^2/5^2  + n^2 $ \
        $ \cdot \cdot \cdot $ 
              
        - As, it is root dominated, upper bound is: $O(n^2)$.

      - **Span:**
        - $S(n)=S(n/5)+n^2$ \
        $= S(n/5^2) + n^2/5^2 + n^2 $ \
        $= S(n/5^3) + n^2/5^4 + n^2/5^2 + n^2 $ \
        $ \cdot \cdot \cdot $ 
        
        - As, it is root dominated, upper bound is: $O(n^2)$.

    - For algorithm $\mathcal{B}$, the work and span are as follows, 
      - **Work:**
        - $W(n)= W(n-1)+ \log n$ \
        $= W(n-2)+ \log (n-1) + \log n$ \
        $= W(n-3)+ \log (n-2) + \log (n-1) + \log n $ \
        $ \cdot \cdot \cdot $ 
              
        - As, it is linear, upper bound is: $O(n \log n)$.

      - **Span:**
        - $S(n)=S(n-1)+ \log n$ \
        $= S(n-2)+ \log (n-1) + \log n$ \
        $= S(n-3)+ \log (n-2) + \log (n-1) + \log n $ \
        $ \cdot \cdot \cdot $ 
        
        - Similar to the work, the span is also: $O(n \log n)$.

    - For algorithm $\mathcal{C}$, the work and span are as follows using *brick* method, 
      - **Work:**
        - $W(n)= W(n/3) + W(2n/3)+ O(n^{1.1})$ \
        $= W(n/3^2) + W(2n/3^2) + W(2^2n/3^2)+ O((n/3)^{1.1}) + O((2n/3)^{1.1}) + O(n^{1.1}) $ \
        $= \cdot \cdot \cdot $ 

        - Here, the tree has two different branches $n/3$ and $2n/3$. For this unbalanced division, the work is roughly dominated by the largest branch, which is $2n/3$. So, 
        - $W(n)= W(2n/3)+ O(n^{1.1})$ \
        $= W(2^2n/3^2)+ O((2n/3)^{1.1}) + O(n^{1.1}) $ \
        $= \cdot \cdot \cdot $ 

        - As, it is root dominated, upper bound is: $O(n^{1.1})$.

      - **Span:**
        - $S(n)=S(n/3) + S(2n/3) +O(n^{1.1})$ \
        $= \cdot \cdot \cdot $ 
        
        - Similar to work, the upper bound of span is also: $O(n^{1.1})$.

    - Implication: I would choose ...

4. Suppose that for a given task you are choosing between the following three algorithms:

	* Algorithm $\mathcal{A}$ solves problems by dividing them into
      five subproblems of half the size, recursively solving each
      subproblem, and then combining the solutions in linear time.
	  
	* Algorithm $\mathcal{B}$ solves problems of size $n$ by
      recursively solving two subproblems of size $n-1$ and then
      combining the solutions in constant time.
		
	* Algorithm $\mathcal{C}$ solves problems of size $n$ by dividing
      them into nine subproblems of size $n/3$, recursively solving
      each subproblem, and then combining the solutions in $O(n^2)$
      time.

    What is the work and span of these algorithms? For the span, just
    assume that it is the same as the work to combine solutions (i.e.,
    the non-recursive quantity). Which algorithm would you choose? Why?

  - *Answer:*
    - For algorithm $\mathcal{A}$, the work and span are as follows using *brick* method, 
      - **Work:**
        - $W(n)=5 \cdot W(n/2)+ n$ \
        $= 5^2 \cdot W(n/2^2) + 5n/2 + n $ \
        $= 5^3 \cdot W(n/2^3) + 5^2n/2^2  + 5n/2  + n $ \
        $ \cdot \cdot \cdot $ 
        
        - Here, the number of leaves in the last level is $= 5^{\log_2 n} = n^{\log_2 5}$.
        - As, it is leaf dominated, upper bound is: $O(n^{\log_2 5})$.

      - **Span:**
        - $S(n)=S(n/2)+n$ \
        $= S(n/2^2) + n/2 + n $ \
        $= S(n/2^3) + n/2^2 + n/2 + n $ \
        $ \cdot \cdot \cdot $ 
        
        - As, it is root dominated, upper bound is: $O(n)$.

    - For algorithm $\mathcal{B}$, the work and span are as follows, 
      - **Work:**
        - $W(n)= 2 \cdot W(n-1)+ 1$ \
        $= 2^2 \cdot W(n-2)+ 2 + 1$ \
        $= 2^3 \cdot W(n-3)+ 2^2 + 2 + 1 $ \
        $ \cdot \cdot \cdot $ 
              
        - At each step, the number of subproblems doubles, so the total work grows expoentially.
        - So, the upper bound is: $O(2^n)$.

      - **Span:**
        - $S(n)=S(n-1) + 1$ \
        $= S(n-2)+ 1+ 1$ \
        $= S(n-3)+ 1 + 1 + 1$ \
        $ \cdot \cdot \cdot $ 
        
        - As it is liear, the span is: $O(n)$.

    - For algorithm $\mathcal{C}$, the work and span are as follows using *brick* method, 
      - **Work:**
        - $W(n)= 9 \cdot W(n/3) + O(n^2)$ \
        $= 9^2 \cdot W(n/3^2) + 9 \cdot O(n^2/3^2) + O(n^2)$ \
        $= 9^3 \cdot W(n/3^3) + 9^2 \cdot O(n^2/3^4) + 9 \cdot O(n^2/3^2) + O(n^2)$ \
        $= \cdot \cdot \cdot $ 

        - As, it is root dominated, upper bound is: $O(n^2)$.

      - **Span:**
        - $S(n)=S(n/3) +O(n^2)$ \
        $= S(n/3^2) +O(n^2/3^2) +O(n^2)$ \
        $= \cdot \cdot \cdot $ 
        
        - Similar to work, the upper bound is also root dominated: $O(n^2)$.

    - Implication: I would choose ...




5. In Module 2 we discussed two algoriths for integer multiplication. The
  first algorithm was simply a recapitulation of the "grade school"
  algorithm for integer multiplication, while the second was the
  Karatsaba-Ofman algorithm. For this problem, you will use the stub
  functions in `main.py` to implement these two algorithms for integer
  multiplication. Once you've correctly implemented them, test the
  empirical running times across a variety of inputs to test whether
  your code scales in the manner predicted by our analyses of the
  asymptotic work.


.  
.  
.  
.  
.  



6. A "white hat" conducts hacking activities for the common good, while a
"black hat" hacker does so for nefarious reasons. Let's consider a
computer security class with $n$ students who are all either white hat
or black hat hackers. You're the instructor, and you don't know who is
a white hat or a black hat, but all of the student do. 

Your goal is to identify the white hats and you're allowed to ask a
pair of students about one another. White hats will always tell the
truth, but you cannot trust a black hat's response. For a pair of students $A$ and
$B$ then there are several possible outcomes:


|$A$ says | $B$ says | Conclusion |
|---------|----------|------------|
|$B$ is a white hat | $A$ is a white hat | both are good, or both are bad |
|$B$ is a white hat | $A$ is a black hat | at least one is bad |
|$B$ is a black hat | $A$ is a white hat | at least one is bad |
|$B$ is a black hat | $A$ is a black hat | at least one is bad |

*6a.* Show that if more than $n/2$ students are black hats, you cannot determine which students are white hats based on a pairwise test. Note that you must assume the black hats are conspiring to fool you.

- *Answer:*
  - Here, $>n/2$ students are black hats and they always try to conspire. In such case, if we do the pairwise test to determine a white hat student we cannot do so because the dominating outcomes will be from the black hats. 
  - Example: 
    - Let the student set is $S = \{s_1, s_2, s_3, s_4, s_5\}$ with $n=5$. Black hat and white hat sets are $S_b = \{s_1, s_3, s_5\}$ and $S_w = \{s_2, s_4\}$, respectively. Here, $|S_b| > n/2$ and $|S_w| < n/2$. 


    - Let's do pairwise tests to try to determine a white hat student (let's say $s_4$). Here is how the pairwise tests could go, assuming the black hats conspire:


      Let's do pairwise tests to try to determine a white hat student (let's say $s_3$) and see how the elimination process works:

      - Pair up the students: $(s_1, s_2), (s_3, s_4)$. $s_5$ is left unpaired (since $n$ is odd, we can ignore $s_5$ for this round or carry them to the next round).

      - Test $s_1$ (black hat) vs $s_2$ (white hat):
        - $s_1$ can say anything (black hat), suppose $s_1$ says $s_2$ is a black hat
        - $s_2$ says $s_1$ is a black hat (truthful)
        - At least one says the other is a black hat → Discard both $s_1$ and $s_2$

      - Test $s_3$ (white hat) vs $s_4$ (white hat):
        - $s_3$ says $s_4$ is a white hat (truthful)
        - $s_4$ says $s_3$ is a white hat (truthful)
        - Both say the other is a white hat → Keep one (say, keep $s_3$)

      - $s_5$ (black hat) is left unpaired, so carry $s_5$ to the next round.

      - After this round, the survivors are $s_3$ (white hat) and $s_5$ (black hat). Now $n=2$.

      - Pair $s_3$ and $s_5$:
        - $s_3$ says $s_5$ is a black hat (truthful)
        - $s_5$ can say anything, suppose $s_5$ says $s_3$ is a black hat
        - At least one says the other is a black hat → Discard both

      - Now, no students remain, but if we had started with a larger set, the process would continue recursively, always keeping at least one white hat per all-white-hat pair. Since white hats are the majority, at least one white hat will survive to the end.

      - This shows how the elimination process works: in each round, $n/2$ pairwise tests reduce the problem size by about half, and the majority of white hats is preserved among the survivors.



*6b.* Consider the problem of finding a single white hat, assuming strictly more than $n/2$ of the students are white hats. Show that $n/2$ pairwise interviews is enough to reduce the problem size by a constant fraction.

- *Answer:*
  - Here, $>n/2$ students are white hats and they always tell the truth. In such case, if we do the pairwise test to determine a white hat student we can reduce the problem size by a constant fraction with $n/2$ pairwise interviews. 
  - Example: 
    - Let the student set is $S = \{s_1, s_2, s_3, s_4, s_5\}$ with $n=5$. Black hat and white hat sets are $S_b = \{s_1, s_5\}$ and $S_w = \{s_2, s_3, s_4\}$, respectively. Here, $|S_b| < n/2$ and $|S_w| > n/2$. 


    - Lets do pairwise tests to try to determine a white hat student (let's say $s_3$). Here is how the pairwise tests could go, assuming the black hats conspire:

      - Test $s_3$ (white hat) vs $s_1$ (black hat):
        - $s_3$ says $s_1$ is a black hat (truthful)
        - $s_1$ (black hat) can say anything, but to conspire, $s_1$ says $s_3$ is a black hat
        - Outcome: Both accuse each other of being black hats → "at least one is bad"

      - Test $s_2$ vs $s_4$ (white hat):
        - $s_2$ says $s_4$ is a white hat
        - $s_4$ says $s_2$ is a white hat
        - Outcome: Both say the other is a white hat → "both are good, or both are bad"

    - Here we can safely remove the $s_3$ and $s_1$ pair, because both accuse each other (at least one is bad). As majority is white hats, we can keep one of $s_2$ and $s_4$. Lets keep $s_2$ from here. Lets carry $s_5$. But then the set size of the next round will be $<n/2$. That's why we can keep both $s_2$ and $s_4$. Hence final set for next round : $S_{next} = \{ s_2, s_4, s_5 \}$. Here also the majority white hat persist. 

    - This means that after each round, the number of candidates is reduced by a constant fraction (specifically, at most half remain), which is why the process is efficient and completes in $O(\log n)$ rounds. .



*6c.* Using the above show that all white hats can be identified using $\Theta(n)$ pairwise interviews.

