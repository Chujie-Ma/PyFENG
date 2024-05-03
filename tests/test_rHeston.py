import numpy as np
import sys
sys.path.insert(0, 'E:/github/PyFENG')
import time
import pyfeng.ex as pfex
import matplotlib.pyplot as plt
import scipy.stats as spst
import scipy.optimize as spop
#dddd
start_time = time.time()

strike = np.linspace(80,120,num=11)
T = np.array([0.1, 0.2, 0.5, 1.0, 1.5, 2.0])
sigma, vov, mr, rho, spot, theta, alpha = 0.04, 0.1, 1, -0.65, 100, 0.04, 0.6
m = pfex.RoughHestonFft(sigma, vov=vov, mr=mr, rho=rho, alpha=alpha)
# price = m.price_fft(strike, spot, texp = 0.01)
# print(price)
# im_vol = m.impvol(price, strike, spot, texp = 1)


row = len(T)
col = len(strike)
price = np.zeros((row,col))
m_vol = np.zeros((row,col))

for i in range(row):
    price[i] = m.price_fft(strike, spot, T[i])
    m_vol[i] = m.vol_smile(strike, spot, T[i], model='bsm')
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

plt.plot(np.log(strike/spot), m_vol[0, :], color = 'b', marker = 'x', markersize=3, linewidth=1, label='T=0.1')
plt.plot(np.log(strike/spot), m_vol[1, :], color = 'g', marker = 'x', markersize=3, linewidth=1, label='T=0.2')
plt.plot(np.log(strike/spot), m_vol[2, :], color = 'r', marker = 'x', markersize=3, linewidth=1, label='T=0.5')
plt.plot(np.log(strike/spot), m_vol[3, :], color = 'k', marker = 'x', markersize=3, linewidth=1, label='T=1.0')
plt.plot(np.log(strike/spot), m_vol[4, :], color = 'y', marker = 'x', markersize=3, linewidth=1, label='T=1.5')
plt.plot(np.log(strike/spot), m_vol[5, :], color = 'm', marker = 'x', markersize=3, linewidth=1, label='T=2.0')
plt.ylabel('Implied volatility')
plt.xlabel('log-moneyness')
plt.legend(loc = 'upper right')
plt.show()
# # #
end_time = time.time()

run_time = end_time - start_time

print('Processing time is', run_time , 's.')
print(price)
print(m_vol)
