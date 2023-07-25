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
    #* 用于选择运行的设备
    if device == "cuda":
        return torch.device("cuda" if torch.cuda.is_available() else "cpu")
    else:
        return torch.device("cpu")


def Normalize(Vector):
    #* 用于单位化向量
    length = torch.linalg.vector_norm(Vector)
    return Vector / length


def EpsilonJPossible(i, j, k, EpsilonInputArray, v_Vectors, SystemMatrixes,
                     Lambdas):
    #* 用于计算$\varepsilon_{j}$可能的取值
    # i,j,k表示公式中的i,j,k下标，从1开始
    # EpsilonInputArray是计算时候输入的$\epsilon_{k}$的序列，不断迭代更新
    # SystemMatrixes表示线性切换系统子系统的系统矩阵
    # $v_{j}$等表示求maximal invarient flag时对应的特征向量，合并为v_Vectors
    # $\lambda_{i,j}$表示共同的特征向量对应的特征值，放到一个下三角的Lambdas矩阵里
    # 系统的维数$n$靠几个输入量读出来
    n = torch.tensor(v_Vectors.shape[0])
    vkConjTransAivj = v_Vectors[:, k - 1].conj().T @ SystemMatrixes[
        j - 1] @ v_Vectors[:, j - 1]
    return EpsilonInputArray[k - 1] * torch.pow(
        n - 1, 2) * vkConjTransAivj / (torch.abs(Lambdas[i - 1, j - 1].real) *
                                       torch.abs(Lambdas[i - 1, k - 1].real))


def IsEqual(vector1, vector2, tol=1e-5):
    #* 检查两个向量是否相等，若相减后二范数小于tol，则返回True
    return (torch.linalg.vector_norm(vector1 - vector2)).numpy() - tol < 0


def GetCommonEigenInfo(MatrixSet, Blacklist=None, tol=1e-5):
    #* 用于求解一系列矩阵共同的特征向量，以及对应的特征值
    #? 返回除了Blacklist之外，第一个特征向量，及对应的特征值
    # MatrixSet是所有矩阵的元组

    # 初始化
    MatrixNum = len(MatrixSet)
    n = MatrixSet[0].shape[0]
    EigenVectors = torch.zeros((MatrixNum, n, n))
    EigenValues = torch.zeros((n, MatrixNum))

    # 计算所有矩阵的特征值和特征向量
    for i in range(MatrixNum):
        EigenValues[:,
                    i], EigenVectors[i, :, :] = torch.linalg.eig(MatrixSet[i])

    # 单位化特征向量
    for i in range(MatrixNum):
        for j in range(n):
            EigenVectors[i, :, j] = Normalize(EigenVectors[i, :, j])

    # 去掉所有Blacklist中的向量
    if Blacklist != None:
        for i in range(Blacklist.shape[1]):
            for j in range(MatrixNum):
                for k in range(n):
                    if IsEqual(Blacklist[:, i], EigenVectors[j, :, k], tol):
                        EigenValues[k, j] = 0

    # 查特征向量出现的次数
    # 查找对应特征值不为0的特征向量
    for i in range(MatrixNum):
        for j in range(n):
            if EigenValues[j, i]:
                # 统计该特征向量出现次数
                OccurTimes = 0
                # 统计特征向量对应的特征值
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
        # matrixset是子系统的系统矩阵
        # Tol是检验向量是否相等时的容许误差
        # 默认使用CPU计算
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
