import numpy as np
import random
import time as time


class Genetic_Algo:
    """
    This is a class for mathematical operations on complex numbers.

    Attributes:
    	sentence (string) : Sentence given in 3-CNF form
        population_size (int),
        mutation_p (int): mutation rate
    """
    
    def __init__(self, sentence, population_size, mutation_p):
        self.sentence = sentence
        self.n = population_size

        self.population = np.random.randint(0, 2, (self.n, 50))

        self.mutation_p = mutation_p

        self.weights = []
        self.fitnessValues = np.zeros(self.n)

    
    def FitnessFunction(self, individual):
        clauseCount = len(self.sentence)
        satCount = 0

        for clause in self.sentence :
            isSat = False
            for x in clause:
                if  x < 0:
                    if(individual[-x-1] == 1):
                        isSat |= False
                    else:
                        isSat |= True
                else:
                    if(individual[x-1] == 1):
                        isSat |= True
                    else:
                        isSat |= False

            if isSat == True:
                satCount += 1

        fitnessScore = 100.0 * satCount / clauseCount

        return fitnessScore
        

    def RandomSelection(self):
        choice = random.choices(self.population, self.weights, k = 1)
        return choice

    def Reproduce(self,x,y):
        
        cp = random.randint(1,self.n)
        
        child = np.concatenate( (x[0:cp], y[cp:]), axis= None)
        
        return child


    def Mutate(self,child):
        for i in range(len(child)):
            p = random.random()
            if p < self.mutation_p:
                child[i] = 1 - child[i]

        return child

    def GenerateModel(self):
        start_time = time.time()
        close_time = time.time() + 44
        result = self.population[0]
        
        fitnessResult = self.FitnessFunction(result)
        countSameResult = 0

        while True:
            print(fitnessResult)
            if close_time < time.time() or fitnessResult == 100 or countSameResult > 200:
                time_taken = time.time() - start_time
                break

            for i in range(self.n):
                self.fitnessValues[i] = self.FitnessFunction(self.population[i])

            sumFitnessValues = sum(self.fitnessValues)

            self.weights = []
            for i in range(self.n):
                self.weights.append(self.fitnessValues[i] / sumFitnessValues)
        


            new_population = []
            for i in range(len(self.population)):
                x = self.RandomSelection()
                y = self.RandomSelection()

                child = self.Reproduce(x,y)
                child = self.Mutate(child)
                new_population.append(child)
            
            
            for i in self.population:
                new_population.append(i)
            
            new_population = sorted(new_population, key = self.FitnessFunction, reverse = True)
            
            self.population = new_population[0:self.n]            
            
            flag = 0
            for i in self.population:
                _fitness = self.FitnessFunction(i)
                
                if( _fitness > fitnessResult ):
                    result = i
                    fitnessResult = _fitness
                    flag = 1

            if flag == 1:
                countSameResult = 0
            else :
                countSameResult += 1
        
        for i in range(len(result)):
            
            if result[i] == 0:
                result[i] = -(i+1)
            else:
                result[i] = i+1

        return result,fitnessResult,time_taken
