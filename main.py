from CNF_Creator import *
from Genetic_Algorithm import *
import matplotlib.pyplot as plt


def main():
    cnfC = CNF_Creator(n=50) # n is number of symbols in the 3-CNF sentence
    # sentence = cnfC.CreateRandomSentence(m=120) # m is number of clauses in the 3-CNF sentence
    # print('Random sentence : ',sentence)


    # m_values = np.arange(100, 320, 20)
    # averageFitness = []
    # averageTime = []
    # for m in m_values:
    #     sum_score = 0
    #     total_time = 0
    #     iterations = 20
    #     for i in range(iterations):
    #         sentence = cnfC.CreateRandomSentence(m)
    #         gAlgo = Genetic_Algo(sentence,50,0.05)
    #         model,fitness,time_taken = gAlgo.GenerateModel()
    #         sum_score += fitness
    #         total_time += time_taken

    #     avg_score = sum_score/iterations
    #     avg_time = total_time/iterations
    #     print("avg_time:",avg_time)
    #     averageFitness.append(sum_score/iterations)
    #     averageTime.append(avg_time)
    #     print("avg_score:",avg_score)

    # plt.plot(m_values, averageFitness, marker="o", markerfacecolor="blue")
    # # plt.xlim(80,320)
    # plt.ylabel('Average fitness value')
    # plt.xlabel('Number of clauses (m)')
    # plt.show()
    # plt.plot(m_values, averageTime,  marker="o", markerfacecolor="blue")
    # # plt.xlim(80,320)
    # plt.ylabel('Average running time')
    # plt.xlabel('Number of clauses (m)')
    # plt.show()

    sentence = cnfC.ReadCNFfromCSVfile()
    gAlgo = Genetic_Algo(sentence,50,0.05)
    model,fitness,time_taken = gAlgo.GenerateModel()

    print('\n\n')
    print('Number of clauses in CSV file : ',len(sentence))
    print('Best model : ', model)
    print('Fitness value of best model : ',fitness)
    print('Time taken : ', time_taken)
    print('\n\n')
    
if __name__=='__main__':
    main()