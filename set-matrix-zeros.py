        matC=[]
        matR=[]
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if matrix[i][j]==0:
                    matC.append(i)
                    matR.append(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in matC or j in matR:
                    matrix[i][j]=0