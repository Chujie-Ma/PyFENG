import numpy as np
import sys
sys.path.insert(0, 'E:/github/PyFENG')
import time
import pyfeng as pf
import matplotlib.pyplot as plt
import scipy.stats as spst
import scipy.optimize as spop
#dddd
start_time = time.time()

strike = np.linspace(80,120,num=21)
T = np.array([0.1, 0.2, 0.5, 1, 1.5, 2])
sigma, vov, mr, rho, spot, theta, alpha = 0.0392, 0.331, 0.1, -0.681, 100, 0.3156, 0.62
m = pf.sv_fft.RoughHestonFft(sigma, vov=vov, mr=mr, rho=rho, alpha=alpha)

row = len(T)
col = len(strike)
# price = m.price(strike, spot, texp=0.1)
price = np.zeros((row,col))

for i in range(row):
    price[i] = m.price(strike, spot, T[i])
# mvol = m.vol_smile(strike, spot, texp=0.5)
# plt.plot(np.log(strike/spot), mvol, 'bo-')
plt.plot(np.log(strike/spot), price[0, :], color = 'b', marker = 'x', markersize=3, linewidth=1, label='T=0.1')
plt.plot(np.log(strike/spot), price[1, :], color = 'g', marker = 'x', markersize=3, linewidth=1, label='T=0.2')
plt.plot(np.log(strike/spot), price[2, :], color = 'r', marker = 'x', markersize=3, linewidth=1, label='T=0.5')
plt.plot(np.log(strike/spot), price[3, :], color = 'k', marker = 'x', markersize=3, linewidth=1, label='T=1.0')
plt.plot(np.log(strike/spot), price[4, :], color = 'y', marker = 'x', markersize=3, linewidth=1, label='T=1.5')
plt.plot(np.log(strike/spot), price[5, :], color = 'm', marker = 'x', markersize=3, linewidth=1, label='T=2.0')
plt.ylabel('Call option prices')
plt.xlabel('log-moneyness')
plt.legend(loc = 'upper right')
plt.show()

m_vol = m.vol_smile(strike, spot, texp = 0.2)
# plt.plot(np.log(strike/spot), np.sqrt(m_vol), color = 'b', marker = 'x', markersize=3, linewidth=1, label='T=1.0')
# # plt.plot(np.log(strike/spot), mvol[1, :], color = 'g', marker = 'x', markersize=3, linewidth=1, label='T=1.0')
# # plt.plot(np.log(strike/spot), mvol[2, :], color = 'r', marker = 'x', markersize=3, linewidth=1, label='T=1.5')
# # plt.plot(np.log(strike/spot), mvol[3, :], color = 'k', marker = 'x', markersize=3, linewidth=1, label='T=2.0')
# plt.ylabel('Implied volatility')
# plt.xlabel('log-moneyness')
# plt.legend(loc = 'upper right')
# plt.show()
# #
end_time = time.time()

run_time = end_time - start_time
#
print('Processing time is', run_time , 's.')
print(price)
print(m_vol)
