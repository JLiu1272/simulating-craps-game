# What is the probability of winning Craps?

## Methodology for computing the probability

I recently went to Vegas, and wanted to compute the probability that
I would win a craps game if I just played the Pass Line Bet.

I simulated the game, and made the computer play it x times. That number
is adjustable. I computed the number of times I would win versus the number
of times I would lose. Thanks to the [Law of Large Numbers](https://en.wikipedia.org/wiki/Law_of_large_numbers), if you play the
game enough times, you will be able to determine the probability of winning
the game.

I played the game as described in this [article](https://entertainment.howstuffworks.com/craps4.htm).

Come Out Point = If you roll a 7 or an 11 on the first roll
Point = If you roll a 4, 5, 6, 8, 9 twice (doesn't have to be consecutively) before rolling a 7.

If you manage to score a point using either of those results, that is considered a win. Therefore, a win is the summation of "Come Out Point" and "Point".

Sevens Out = If you roll a 4, 5, 6, 8, 9, but you rolled a 7 before you rolled managed to roll that number the second time

Craps = If you roll a 2, 3, or 12 on the first roll

If a Sevents Out or Craps event happened, that is considered a lose. Therefore, a lose is the summation of "Sevens Out" and "Craps".

The probability of winning this game is thus computed using this formula.

((# of wins) / (# of wins + # of losses)) \* 100

## Results

You can produce the same result by setting the [times=1000000](https://github.com/JLiu1272/simulating-craps-game/blob/master/craps.py#L252), and running `craps.py`. It might be a few percentage point off, but on average the probability of winning craps merely playing "Pass Line Bet" is ~35%.

Here are the raw results, when running the program once.

You played this game 1000000 times, and these are your wins and losses

---

Wins: <br/>
Come Out Point: 222338 <br/>
Point: 51478

Losses: <br/>
Craps: 111294 <br />
Sevens Out: 392347 <br />

---

You won 273816 times, and loss 503641 times. Your winning probability is 35.21943978895296%

You are more likely to win scoring ComeOutPoint than Point
