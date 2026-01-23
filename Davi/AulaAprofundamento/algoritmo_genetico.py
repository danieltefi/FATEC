from deap import base, creator, tools, algorithms

import random

def fitness(individuo):
    beneficios = [10, 5, 8, 6, 7]
    return (sum(b * i for b, i, in zip(beneficios, individuo)),)

def fitness_2(individuo):
    beneficios = [10, 5, 8, 6, 7]
    total_atividades = sum(individuo)

    if total_atividades > 3:
        return (-1000, )
    
    valor_total = 0
    for b, i in zip(beneficios, individuo):
        valor_total = valor_total + (b * i)
    
    return (valor_total,)

creator.create("FitnessMax", base.Fitness, weights=(1.0, ))

creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

toolbox.register("gene", random.randint, 0,1)

toolbox.register(
    "individual",
    tools.initRepeat,
    creator.Individual,
    toolbox.gene,
    n=5
)

toolbox.register(
    "population",
    tools.initRepeat,
    list,
    toolbox.individual
)

toolbox.register("evaluate", fitness)

toolbox.register("mate", tools.cxTwoPoint)

toolbox.register("mutate", tools.mutFlipBit, indpb=0.1)

toolbox.register("select", tools.selTournament, tournsize=3)

populacao = toolbox.population(n=20)

algorithms.eaSimple(
    populacao,
    toolbox,
    cxpb=0.7,
    mutpb=0.2,
    ngen=30,
    verbose=True
)

melhor = tools.selBest(populacao, 1)[0]

print('Melhor solução encontrada:')
print('Indivíduo:', melhor)
print('Fitness:', melhor.fitness.values)