# Vampires vs. wolves agent
Adversarial search agent implementation on Vamps vs Werewolves board game

The bot won 20 games out of 23 games in the tounament. It managed to always play within 2 seconds and preform smart
actions.

Heuristic function can be changed in the heuristic.py file:

$$ Heuristic = 100(\text{max kill}) + 10(\text{species diff}) + \text{max eat diff + random bias + end of game} $$

Proximity of search can also be changed

![alt text](https://github.com/Mouuaadd/Vamps.vs.wolves_agent/blob/master/prox.JPG?raw=true)

## Launch server with docker

```
bash scripts/build.sh
bash scripts/run.sh
```

## Launch player

```
python -m main localhost 5555 name
```
