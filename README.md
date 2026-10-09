# Python Quiz

#### Video Demo: https://youtu.be/UjjHDnnqqAM

#### Description:

For my CS50P final project, I decided to make a simple Python quiz. The
idea is pretty straightforward: the program asks multiple-choice questions
about Python and basic computer science, and the user answers by entering
1, 2, or 3.

I chose a quiz because I wanted to make something interactive instead of
just writing a program that prints information. It also gave me a chance to
use several of the things I learned during CS50P in one project.

The main file is `project.py`. It contains the quiz itself and the functions
used by the program. `show_question()` displays the question and its options.
`check_answer()` checks whether the answer entered by the user is correct.
`calculate_score()` updates the score when an answer is correct, and
`get_result()` calculates the percentage and gives a short message depending
on the final result.

I also used the `random` module to shuffle the questions. This means that
the questions can appear in a different order each time the program is
run. I thought this would make the quiz a little more interesting and less
predictable.

One thing I wanted to make sure of was that the program would not crash if
the user entered something unexpected. For example, if the user enters
letters instead of a number, the program asks them to enter a valid number.
It also checks that the number is between 1 and 3.

At the end, the program shows the user's score and percentage. It then gives
one of three results: "Excellent!", "Good!", or "Keep practicing". I kept
the scoring system simple because the main purpose of the project was to
practice Python rather than make a complicated grading system.

The second file, `test_project.py`, contains tests for some of the functions
in `project.py`. I test `check_answer()`, `calculate_score()`, and
`get_result()` to make sure they return the values I expect.

While making the project, I decided to split the code into different
functions instead of putting everything inside `main()`. This made the code
easier for me to follow and also made it possible to test individual parts
of the program.

This project is fairly simple, but it represents what I learned during
CS50P and gave me an opportunity to put those concepts together in a
program that I could actually run and use.