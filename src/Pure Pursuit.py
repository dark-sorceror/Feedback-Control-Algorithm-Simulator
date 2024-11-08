# Injection Algorithm
import numpy as np

def pointInjectionAlgorithm(points:list[tuple], spacing:int = 1):
    newPoints = []

    for i in range(len(points) - 1):
        endPoint = np.array(points[i + 1], dtype=float)
        startPoint = np.array(points[i], dtype=float)
        
        vector = endPoint - startPoint
        
        numPointsThatFit = int(np.linalg.norm(vector) / (spacing if spacing > 0 else 1))
        unitOfVector = vector / (numPointsThatFit if numPointsThatFit > 0 else 1)
        
        for j in range(round(numPointsThatFit if numPointsThatFit > 0 else 1)):
            newPoints.append(tuple((points[i] + unitOfVector * j).tolist()))
            
    newPoints.append(tuple(points[-1]))

    return newPoints