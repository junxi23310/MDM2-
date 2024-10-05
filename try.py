import numpy as np
import matplotlib.pyplot as plt

# 定义多项式系数，例如 y = 2x^2 + 3x + 1
coeffs = [2, 3, 1]  # 这里的 coeffs 是 [2, 3, 1]

# 计算自变量 x 的值
x = np.linspace(-1, 2, 100)  # 在 -1 到 2 之间生成 100 个点

# 使用 polyval 计算对应的 y 值
y = np.polyval(coeffs, x)

# 绘制结果
plt.plot(x, y, label='Polynomial: 2x^2 + 3x + 1')
plt.title('Polynomial Evaluation with numpy.polyval')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='gray', lw=0.5, ls='--')  # 添加水平线 y=0
plt.axvline(0, color='gray', lw=0.5, ls='--')  # 添加垂直线 x=0
plt.legend()
plt.grid()
plt.show()
