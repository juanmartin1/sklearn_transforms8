class Coding():
    def __init__(self, p):
        self.p = p

    def decode(self):
        self.p1 = np.array([])
        for i in range(0,len(self.p)):
            if self.p[i] <= 1.0:
                self.p1 = np.append(self.p1, "EXCELENTE")
            if self.p[i] == 2.0:
                self.p1 = np.append(self.p1, "MUITO_BOM")
            if self.p[i] == 3.0:
                self.p1 = np.append(self.p1, "HUMANAS")
            if self.p[i] == 4.0:
                self.p1 = np.append(self.p1, "EXATAS")
            if self.p[i] >= 5.0:
                self.p1 = np.append(self.p1, "DIFICULDADE")
        return self.p1

    def code(self):
        self.p1 = np.array([])
        for i in range(0,len(self.p)):
            if self.p[i] == "EXCELENTE":
                self.p1 = np.append(self.p1, 1)
            if self.p[i] == "MUITO_BOM":
                self.p1 = np.append(self.p1, 2)
            if self.p[i] == "HUMANAS":
                self.p1 = np.append(self.p1, 3)
            if self.p[i] == "EXATAS":
                self.p1 = np.append(self.p1, 4)
            if self.p[i] == "DIFICULDADE":
                self.p1 = np.append(self.p1, 5)
        return self.p1