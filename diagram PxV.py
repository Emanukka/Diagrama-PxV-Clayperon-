import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt


n=1 #kmol
R=8.314 #kPa*m^3/kmol*K
T=300 #kelvin

#defining a function P that correlates V,P values at a correspondate T

def P(V):
    P=(n*R*T)/V
    return P

#crating Work function, which will be the integral of  P(V);
#futhermore, this function will plot a graph based of integral limits (V_i,V_f.
def W(P,V_i,V_f):
    w=integrate.quad(P,V_i,V_f)
        
    # 1) ploting the curve P(V)=(nRT)/V
    
    #1.1) creating a loop which inverts Vf,Vi if it's W<0 (gas compression),
    #     and be possible to calculate the values
    while 0!=1: 
        if V_f-V_i>0:
         
            x= np.arange(1,V_f+6)
            y=[P(V) for V in x]
            fig,ax= plt.subplots()
            ax.plot(x, y)
            ax.set_title(" PxV graph; Constant temperature=${0}K$".format(T),fontsize=15)
            ax.set_xlabel("Volume (m^3)",fontsize=12)
            ax.set_ylabel("Pressure (kPa)",fontsize=12)
            
            #2) ploting the area
        
            x_1=np.arange(V_i,V_f+1)
            y_1=[P(V) for V in x_1]
            
            #2.1)  this  function will be responsible to plot the area
            ax.fill_between(x_1,y_1,alpha=0.5)
            
            #2.2) this function will delimites the area
            plt.vlines(V_f,0,P(V_f), linestyles="dotted")
            plt.vlines(V_i,0,P(V_i), linestyles="dotted")
            
            ax.text((V_i+V_f)/4+4, 1500, ' Curve: $PV=nRT$', fontsize=15)
            ax.text((V_i+V_f)/4+4, 2000, ' Area: W={0}kJ '.format(round(w[0])), fontsize=15)
            
            return w, plt.show()
            break
        
        elif V_f-V_i<0:
            V_i,V_f=V_f,V_i
            continue

        


