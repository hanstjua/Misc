import os
import numpy as np
import matplotlib.pyplot as plt

wd = '/Users/johantjuatja/'
os.chdir(wd)

dataKeyword = 'xypts'

def calcAngle(data):
    # setup relevant vectors
    refAxisVec = data[:,0:2] - data[:,2:4]
    R3Vec = data[:,4:6] - data[:,2:4]
    R2Vec = data[:,6:8] - data[:,2:4]
    R1Vec = data[:,8:10] - data[:,2:4]
    L3Vec = data[:,10:12] - data[:,2:4]
    L2Vec = data[:,12:14] - data[:,2:4]
    L1Vec = data[:,14:16] - data[:,2:4]

    # calculate magnitudes of vectors
    refAxisNorm = np.linalg.norm(refAxisVec, axis=1)
    R3Norm = np.linalg.norm(R3Vec, axis=1)
    R2Norm = np.linalg.norm(R2Vec, axis=1)
    R1Norm = np.linalg.norm(R1Vec, axis=1)
    L3Norm = np.linalg.norm(L3Vec, axis=1)
    L2Norm = np.linalg.norm(L2Vec, axis=1)
    L1Norm = np.linalg.norm(L1Vec, axis=1)

    # calculate leg angles using definition of vector dot product
    R3Ang = np.arccos(np.sum(R3Vec*refAxisVec, axis=1)/(refAxisNorm*R3Norm))*180/np.pi
    R2Ang = np.arccos(np.sum(R2Vec*refAxisVec, axis=1)/(refAxisNorm*R2Norm))*180/np.pi
    R1Ang = np.arccos(np.sum(R1Vec*refAxisVec, axis=1)/(refAxisNorm*R1Norm))*180/np.pi
    L3Ang = np.arccos(np.sum(L3Vec*refAxisVec, axis=1)/(refAxisNorm*L3Norm))*180/np.pi
    L2Ang = np.arccos(np.sum(L2Vec*refAxisVec, axis=1)/(refAxisNorm*L2Norm))*180/np.pi
    L1Ang = np.arccos(np.sum(L1Vec*refAxisVec, axis=1)/(refAxisNorm*L1Norm))*180/np.pi

    return [('R3',R3Ang), ('R2',R2Ang), ('R1',R1Ang), ('L3',L3Ang), ('L2',L2Ang), ('L1',L1Ang)]
    
def main():
    plotData = []

    for f in os.listdir():

        # process every file with keyword in its name
        if os.path.isfile(f) and dataKeyword in f:
            fData = np.genfromtxt(f, delimiter=',')

            rawData = []
            for row in fData:
                # check if there is any NaN in the row
                if True in np.isnan(row):
                    continue
                rawData.append(row)

            plotData.append((f,np.array(rawData)))

    # setup graph plotting
    for data in plotData:
        fig, axs = plt.subplots(6, 1, sharex=True)
        fig.suptitle(data[0])
        fig.set_figheight(8)
        fig.set_figwidth(9)
        
        print('No of cols: ',len(data[1][0]))
        angleTuples = calcAngle(data[1])
        
        for i in range(6):
            if i%2==0: color = 'red'
            else: color = 'blue'
            
            axs[i].plot(angleTuples[i][1], color=color)
            axs[i].set_title(angleTuples[i][0])
            axs[i].set_ylabel('Angles (deg)')

        # plt.show()
        plt.subplots_adjust(hspace=0.4)
        plt.savefig(data[0]+".png",bbox_inches='tight')

if __name__ == "__main__":
    main()
