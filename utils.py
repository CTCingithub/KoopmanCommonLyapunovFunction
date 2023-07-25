"""
Author: CTC 2801320287@qq.com
Date: 2023-07-25 09:51:38
LastEditors: CTC 2801320287@qq.com
LastEditTime: 2023-07-25 10:48:19
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
"""
import torch


def SelectDevice(device="cpu"):
    #* ����ѡ�����е��豸
    if device == "cuda":
        return torch.device("cuda" if torch.cuda.is_available() else "cpu")
    else:
        return torch.device("cpu")


def Normalize(Vector):
    #* ���ڵ�λ������
    length = torch.linalg.vector_norm(Vector)
    return Vector / length


def EpsilonJPossible(i, j, k, EpsilonInputArray, v_Vectors, SystemMatrixes,
                     Lambdas):
    #* ���ڼ���$\varepsilon_{j}$���ܵ�ȡֵ
    # i,j,k��ʾ��ʽ�е�i,j,k�±꣬��1��ʼ
    # EpsilonInputArray�Ǽ���ʱ�������$\epsilon_{k}$�����У����ϵ�������
    # SystemMatrixes��ʾ�����л�ϵͳ��ϵͳ��ϵͳ����
    # $v_{j}$�ȱ�ʾ��maximal invarient flagʱ��Ӧ�������������ϲ�Ϊv_Vectors
    # $\lambda_{i,j}$��ʾ��ͬ������������Ӧ������ֵ���ŵ�һ�������ǵ�Lambdas������
    # ϵͳ��ά��$n$������������������
    n = torch.tensor(v_Vectors.shape[0])
    vkConjTransAivj = v_Vectors[:, k - 1].conj().T @ SystemMatrixes[
        j - 1] @ v_Vectors[:, j - 1]
    return EpsilonInputArray[k - 1] * torch.pow(
        n - 1, 2) * vkConjTransAivj / (torch.abs(Lambdas[i - 1, j - 1].real) *
                                       torch.abs(Lambdas[i - 1, k - 1].real))


def IsEqual(vector1, vector2, tol=1e-5):
    #* ������������Ƿ���ȣ�������������С��tol���򷵻�True
    return (torch.linalg.vector_norm(vector1 - vector2)).numpy() - tol < 0


def GetCommonEigenInfo(MatrixSet, Blacklist=None, tol=1e-5):
    #* �������һϵ�о���ͬ�������������Լ���Ӧ������ֵ
    #? ���س���Blacklist֮�⣬��һ����������������Ӧ������ֵ
    # MatrixSet�����о����Ԫ��

    # ��ʼ��
    MatrixNum = len(MatrixSet)
    n = MatrixSet[0].shape[0]
    EigenVectors = torch.zeros((MatrixNum, n, n))
    EigenValues = torch.zeros((n, MatrixNum))

    # �������о��������ֵ����������
    for i in range(MatrixNum):
        EigenValues[:,
                    i], EigenVectors[i, :, :] = torch.linalg.eig(MatrixSet[i])

    # ��λ����������
    for i in range(MatrixNum):
        for j in range(n):
            EigenVectors[i, :, j] = Normalize(EigenVectors[i, :, j])

    # ȥ������Blacklist�е�����
    if Blacklist != None:
        for i in range(Blacklist.shape[1]):
            for j in range(MatrixNum):
                for k in range(n):
                    if IsEqual(Blacklist[:, i], EigenVectors[j, :, k], tol):
                        EigenValues[k, j] = 0

    # �������������ֵĴ���
    # ���Ҷ�Ӧ����ֵ��Ϊ0����������
    for i in range(MatrixNum):
        for j in range(n):
            if EigenValues[j, i]:
                # ͳ�Ƹ������������ִ���
                OccurTimes = 0
                # ͳ������������Ӧ������ֵ
                Lambdas = torch.zeros((MatrixNum, 1))
                for k1 in range(MatrixNum):
                    for k2 in range(n):
                        if IsEqual(EigenVectors[i, :, j],
                                   EigenVectors[k1, :, k2], tol):
                            Lambdas[OccurTimes, :] = EigenValues[k2, k1]
                            OccurTimes = OccurTimes + 1
                if OccurTimes == MatrixNum:
                    return EigenVectors[i, :, j].reshape(-1, 1), Lambdas

    print("No Common Eigenvectors!")


class ObtainInvariantMaximalFlag:

    def __init__(self, matrixset, Tol=1e-5, device="cpu"):
        # matrixset����ϵͳ��ϵͳ����
        # Tol�Ǽ��������Ƿ����ʱ���������
        # Ĭ��ʹ��CPU����
        self.MatrixSetInput = matrixset
        self.tol = Tol
        self.device = SelectDevice(device)
        self.m = len(matrixset)
        self.n = matrixset[0].shape[0]

    def MatrixSet(self):
        MatrixSet = ()
        print(self.device)
        for i in range(self.m):
            if type(self.MatrixSetInput[i]) != torch.Tensor:
                temp = torch.from_numpy(self.MatrixSetInput[i])
            else:
                temp = self.MatrixSetInput[i]
            temp = temp.to(self.device)
            MatrixSet = MatrixSet + (temp, )
        return MatrixSet
    
    def ComputeMatrixSet(self,P):
        for i in range(self.m):
            pass

    def ComputeFlagInfo(self):
        for i in range(self.n):
            if i == 0:
                v_temp, lambda_temp = GetCommonEigenInfo(
                    self.MatrixSet(), self.tol)
                V_Matrix = v_temp.reshape(-1, 1)
                Lambda_Matrix = lambda_temp.reshape(1, -1)
                P_Matrix = V_Matrix @ torch.linalg.inv(
                    V_Matrix.conj().T @ V_Matrix) @ V_Matrix.conj().T
            else:
                pass