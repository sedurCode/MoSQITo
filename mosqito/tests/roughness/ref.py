# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 11:22:22 2020

@author: wantysal
"""

import numpy as np
import matplotlib.pyplot as plt


def ref_roughness(fc, fmod):
    """ Give the reference value for roughness by linear interpolation from the data
        given in E. Zwicker, H. Fastl: Psychoacoustics, 1990 (figure 11.2) 
        
        Parameters
        ----------
        fc: integer
            carrier frequency
        fmod: integer
            modulation frequency
            
        Output
        ------
        R_ref: float
            reference roughness value
        """

    if fc == 125:
        fm = np.array([ 10.022323,  14.848474, 22.114502,  24.942839,  27.836662,
                       31.386786,  34.207447,  36.984425,  39.57145 ,  43.002625,
                       47.327793,  51.28128 ,  57.166443,  62.746964,  67.984726,
                       75.005325,  82.11216 ,  88.736916,  93.929695, 101.51012 ,
                       106.34942, 105.52151,  139.52977,  179.7899,   226.8836,
                       618.8289   ])

        R = np.array([0.08789206, 0.15167634, 0.2644867 , 0.29879957, 0.32463667,
                      0.3400558 , 0.34709367, 0.33893484, 0.3292617 , 0.31324393,
                      0.2748609 , 0.24245752, 0.20193195, 0.1835343 , 0.16109457,
                      0.12749602, 0.10928232, 0.09564932, 0.08615938, 0.07580507,
                      0.07027298, 0.070275314,0.04090890, 0.02875568, 0.018735673,
                      0.0032628998  ])



    if fc == 250:
        fm = np.array([  9.866886,  12.62216 ,  27.420376,  32.75557 ,  38.11424 ,
                        43.422382,  49.456688,  57.491714,  65.77677 ,  79.65614 ,
                        87.87329 , 105.86451 , 129.53415 , 156.846   , 166.90276 ,
                       164.31425,  194.89453,  236.00826,  320.22247,  996.67883   ])

        R = np.array([0.08789789, 0.12193831, 0.3708092 , 0.43099418, 0.4755579 ,
                      0.49039465, 0.47503302, 0.41672865, 0.34165177, 0.24969354,
                      0.20581095, 0.15120474, 0.10822188, 0.07665783, 0.07013886,
                      0.07014351 ,0.05207635, 0.037664894,0.022104176,0.0031560503 ])
        
    if fc == 500:
        fm = np.array([ 11.409495,  30.487507,  33.946957,  36.913254,  39.927513,
                        42.292023,  46.705784,  50.772938,  52.936295,  56.059425,
                        59.361572,  63.18659 ,  66.90265 ,  71.01811 ,  74.79408 ,
                        78.56848 ,  83.38223 ,  94.163795, 113.73634 , 149.61226 ,
                       228.0776,   269.4534,   343.64062,  438.18573,  536.22815,
                       1831.6288  ])
        
        R = np.array([0.10152269, 0.4159882 , 0.48784226, 0.53730124, 0.58255917,
                      0.61374336, 0.65500504, 0.67568153, 0.6826773 , 0.68430084,
                      0.6717034 , 0.6593232 , 0.6337642 , 0.6012624 , 0.56008166,
                      0.5258434 , 0.47217426, 0.38673645, 0.2821931 , 0.1763591 ,
                      0.08655889, 0.06439575, 0.04328783, 0.02805619, 0.020718602,
                      0.0024511195  ])
        
    if fc == 1000:              
        fm = np.array([ 11.087001,  13.655874,  17.425774,  22.323097,  28.37367 ,
                        34.94905 ,  42.370758,  49.96757 ,  56.425716,  63.209957,
                        69.42832 ,  74.194626,  81.15967 ,  87.05505 ,  95.19742 ,
                       103.28752 , 112.92756 , 137.10373 , 160.75127 , 193.66571 ,
                       220.964   , 246.33324 , 284.3601  , 332.1115, 402.6136,
                       472.69742,  578.35956,  700.3975,  2566.1887   ])

        R = np.array([0.10113691, 0.13728729, 0.19609652, 0.27899456, 0.39539358,
                      0.5409575 , 0.7005437 , 0.8453598 , 0.9321353 , 0.98051274,
                      0.99174285, 0.9837013 , 0.9491586 , 0.90162235, 0.80737907,
                      0.7173512 , 0.6151961 , 0.44188514, 0.34071133, 0.25057378,
                      0.19783457, 0.16634719, 0.13030091, 0.10086449, 0.07060981,
                      0.05522989, 0.03911979, 0.02859039, 0.0032180264  ])
        
    if fc == 2000:
        fm = np.array([  9.91285,  14.026899,  42.67351 ,  48.009727,  51.526123,  
                        55.798893, 58.02824,   63.2473  ,  68.39307 ,  73.18517 , 
                        78.91965 , 85.31508,   94.640015,  97.87623 , 112.84719 ,
                       116.1008 , 134.20557,  142.05911 , 176.54396 , 208.32822 , 
                       247.7417,  325.8978 ,  392.00952 , 472.19678 , 560.03955,
                       661.0346, 2300.151     ])
        
        R = np.array([0.0769564,  0.12057757, 0.5939494 , 0.68385667, 0.7424558 , 
                      0.78007925, 0.7985556 , 0.8280814 , 0.8409192 , 0.8384773 ,
                      0.8165356 , 0.78357395, 0.69696763, 0.65123534, 0.5195601 ,
                      0.49169108, 0.3902205 , 0.3513164 , 0.2457958 , 0.18558311, 
                      0.13721035, 0.08642737, 0.0607108,  0.043004807,0.031432506,
                      0.02523464, 0.0031944455   ])
        
    if fc == 4000:
        fm = np.array([ 11.3765,    15.561241,  43.589268,  47.646236,  51.401146,  
                        56.619133,  59.81015 ,  63.843525,  67.08531 ,  70.85759 ,
                        74.06288 ,  77.41061 ,  81.33141 ,  87.916466,  97.7758  ,
                       100.33316 , 115.681206, 119.01259 , 134.40422 , 148.2887  , 
                       177.72102 , 205.42125 , 235.5931  , 272.31946 , 296.5826,
                       330.12863,  406.07715,  481.70474,  562.59235, 1862.4557   ])
        
        
        R = np.array([0.07075734, 0.10967778, 0.4784683 , 0.52834743, 0.5683734 ,
                      0.6097778 , 0.6274577 , 0.6473149 , 0.6522843 , 0.6521323 , 
                      0.6452131 , 0.6333704 , 0.62010473, 0.57756937, 0.51043147,
                      0.48305747, 0.38639748, 0.36280885, 0.29872113, 0.2538336 , 
                      0.18619592, 0.1454662 , 0.11394783, 0.08948974, 0.07725139,
                      0.06268515, 0.04557176, 0.03472703, 0.026881821,0.003147697   ])

    if fc == 8000:
        fm = np.array([  9.403103,  17.80395 ,  55.790886,  61.60936 ,  66.79713 , 
                        70.92175 ,  76.48056 ,  82.46687 ,  90.54218 ,  94.376076,
                       105.48482 , 109.09549 , 122.24679 , 143.51547 , 183.9545  ,
                       219.89703,  266.57776,  336.44156,  435.79315,  561.5252,
                       1394.7712    ])
        
        R = np.array([0.03535737, 0.09006271, 0.40631378, 0.42686793, 0.43575785, 
                      0.4356466 , 0.42647484, 0.40776858, 0.3738506 , 0.35563606, 
                      0.29824737, 0.2837258 , 0.2342281 , 0.17965466, 0.11587502,
                      0.08544585, 0.05986661, 0.04003583, 0.026355661,0.017170433,
                      0.0031515576  ])

    return np.interp(fmod, fm, R)




# # Check plots

# fmod     = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110,120, 160,
#                       180, 200, 250, 300, 400])

# curve1 = ref_roughness(125, fmod)
# curve2 = ref_roughness(250, fmod)
# curve3 = ref_roughness(500, fmod)
# curve4 = ref_roughness(1000, fmod)
# curve5 = ref_roughness(2000, fmod)
# curve6 = ref_roughness(4000, fmod)
# curve7 = ref_roughness(8000, fmod)

# plt.figure()
# plt.plot(fmod,curve1)
# plt.plot(fmod,curve2)
# plt.plot(fmod,curve3)
# plt.plot(fmod,curve4)
# plt.plot(fmod,curve5)
# plt.plot(fmod,curve6)
# plt.plot(fmod,curve7)

# plt.xscale('log')
# plt.yscale('log')


    
    
    
    
    
    
    
    
    
    

