#!/usr/bin/env python3  
# -*- coding: utf-8 -*-

'IDBM KPI报告函数库'

__author__ = 'Xuanyu Wang'

def _Net_Revenue (GroSaleRev, CusDisc):
    if not isinstance(GroSaleRev, (int, float)) & isinstance(CusDisc, (int, float)):
        raise TypeError('Data Type Error')
    return GroSaleRev-CusDisc

def _GP_I (Net_Rev, GP_I):
    if not isinstance(Net_Rev, (int, float)) & isinstance(GP_I, (int, float)):
        raise TypeError('Data Type Error')
    return GP_I/Net_Rev

def _GP_15 (Net_Rev, GP_15):
    if not isinstance(Net_Rev, (int, float)) & isinstance(GP_15, (int, float)):
        raise TypeError('Data Type Error')
    return GP_15/Net_Rev

def _GP_III (Net_Rev, GP_III):
    if not isinstance(Net_Rev, (int, float)) & isinstance(GP_III, (int, float)):
        raise TypeError('Data Type Error')
    return GP_III/Net_Rev

def _GP_IV (Net_Rev, GP_IV):
    if not isinstance(Net_Rev, (int, float)) & isinstance(GP_IV, (int, float)):
        raise TypeError('Data Type Error')
    return GP_IV/Net_Rev

def _OveExp (DirCst, InDirExp, FinRes, Net_Rev):
    #if not isinstance(Net_Rev, (int, float)) & isinstance(DirCst, (int, float)) & isinstance(InDirExp, (int, float)) & isinstance(FinRes, (int, float)):
        #raise TypeError('Data Type Error')
    return ((DirCst+InDirExp-FinRes)/Net_Rev)

def CusService (GroSaleRev, CusDisc, GP_I, GP_15, GP_III, GP_IV):
    return _Net_Revenue, _GP_I, _GP_15, _GP_III, _GP_IV


#类型为__xxx__的函数或变量为特殊变量，可以直接引用但有特殊用途
#类型为_xxx或xxx_的函数或变量为private，不应被直接引用。以上面的函数为例，CusService为public函数，其中包含诸多private函数相当于隐藏了CusService的内部逻辑，只需调用CusService即可
#外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。
