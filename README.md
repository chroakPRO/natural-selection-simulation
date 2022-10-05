# Welcome
Hello there Peter or anyone else who reads this. I hope this medium length markdown will help you understand the structure a bit more and see clear goals.

## Introduction
The purpose of this project is to create a fully custom simulation enviorment and agents to display metrics/results. To see optimizations etc.

## Classes

1. **Enviorment**: `The Arena/Array` <br>
   1. FOUND in engine
2. **Prey**: `Prey agent, used as metric` 
   1. FOUND in agents
3. **Hunter**: `Hunter agent, used as metric` 
   1. FOUND in agents
4. **Genes**: `Struct that defines agents genes construction` 
   1. FOUND in models
5. **Game**: `Loop` 
   1. FOUND in engine
6. **GameManager**: `States` 
   1. FOUND in maangers
7. **GameConditions** `extra features to Enviroment` 
   1. FOUND in engine/GameConditions


## Fitness function
```python
def calc_FITNESS(self, gen_array: List[int], days_survived: int) -> int:
    self.days_survived = days_survived
    self.GENES = gen_array
    """
    Fitness function
    It's quite simple it looks at how many days the prey 
    has been alive and how many enemy close it has. 
    Bad fitness function

    """
    self.FITNESS = (self.days_survived / 0,45) * (self.GENES[0] / 0.09) * (self.enemy_close / 0.02)
    # Returns float
    return self.FITNESS
```

## Mutation
Just read about crossover-point mutation. It's quite straightforward.<br>
[Crossover-point Mutation](https://www.sciencedirect.com/topics/computer-science/point-crossover)

## Enviroment Class
`That class is very well documented, read it.`


# Currently working on:
`END GOAL`: `Finish Enviorment`
Steps:<br>
1. Generate World
2. Setup initial conditions
   1. Weather
   2. Challenges


# Ask me on discord
If you have any question just contact me and I will try to help you.





