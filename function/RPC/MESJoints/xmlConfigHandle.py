from xml.dom import minidom
import xml.etree.ElementTree as ET
import os
CONFIG_VERSION = ""
xsi="http://www.w3.org/2001/XMLSchema-instance"
xsd="http://www.w3.org/2001/XMLSchema"
PAR_TYPE_LIST = ['Config','COMs','Servers','Clients']

class DotConfig(object):
    class sysConfig(object):
        # 胶阀使能，1为使能，0为禁用，编号1-4
        #"""UI需要通过以下参数初始化胶阀编号选择的下拉框，将使能的胶阀变化添加进该下拉框"""
        valve1Enable_B = {"value":1,"account":"1号胶阀使能，1为使能，0为禁用"}
        valve2Enable_B = {"value":0,"account":"2号胶阀使能，1为使能，0为禁用"}
        valve3Enable_B = {"value":0,"account":"3号胶阀使能，1为使能，0为禁用"}
        valve4Enable_B = {"value":0,"account":"4号胶阀使能，1为使能，0为禁用"}

        valve1_airType_I = {"value": 2, "account": "胶阀1气源控制方式:0-无 1-比例阀控制 2-电磁阀控制"}
        valve2_airType_I = {"value": 2, "account": "胶阀2气源控制方式:0-无 1-比例阀控制 2-电磁阀控制"}
        valve3_airType_I = {"value": 0, "account": "胶阀3气源控制方式:0-无 1-比例阀控制 2-电磁阀控制"}
        valve4_airType_I = {"value": 0, "account": "胶阀4气源控制方式:0-无 1-比例阀控制 2-电磁阀控制"}
        #
        isSingleMachine_B = {"value":1,"account":"是否是单机运行模式"}
        # ，编号1-2
        conveyor1Enable_B = {"value":1,"account":"1号轨道使能，1为使能，0为禁用"}
        conveyor2Enable_B = {"value":1,"account":"2号轨道使能，1为使能，0为禁用"}
        # ，编号1-2
        conveyor1HeatEnable_B = {"value":1,"account":"1号轨道加热使能，1为使能，0为禁用"}
        conveyor2HeatEnable_B = {"value":1,"account":"2号轨道加热使能，1为使能，0为禁用"}
        #
        conveyor1Dir_I = {"value":1,"account":"1号轨道传送方向  1为从左往右  -1为从右往左"}
        conveyor1InTimeOut_D = {"value":10.0 ,"account":"1号轨道进料超时时间设置 单位 秒(s)"}
        conveyor1OutTimeOut_D = {"value":10.0 ,"account":"1号轨道出料超时时间设置 单位 秒(s)"}
        conveyor2Dir_I = {"value": 1,"account":"2号轨道传送方向  1为从左往右  -1为从右往左"}
        conveyor2InTimeOut_D = {"value":10.0,"account":"2号轨道进料超时时间设置 单位:秒(s)"}
        conveyor2OutTimeOut_D = {"value":10.0,"account":"2号轨道出料超时时间设置 单位:秒(s)"}
        # 轴名，编号0-5
        #"""UI需要通过以下参数初始化轴名"""
        axis0Name_S = {"value":'X',"account":"轴0名称"}
        axis1Name_S = {"value":'Y',"account":"轴1名称"}
        axis2Name_S = {"value":'Z',"account":"轴2名称"}
        axis3Name_S = {"value":'Z2',"account":"轴3名称"}
        axis4Name_S = {"value":'V',"account":"轴4名称"}
        axis5Name_S = {"value":'W',"account":"轴5名称"}
        # 运动轴的使能，1为使能，0为禁用，编号0-5
        #"""UI需要通过以下参数使能手动界面和坐标显示的各个轴的状态"""
        axis0Enable_B = {"value":1,"account":"轴0使能"}
        axis1Enable_B = {"value":1,"account":"轴1使能"}
        axis2Enable_B = {"value":1,"account":"轴2使能"}
        axis3Enable_B = {"value":0,"account":"轴3使能"}
        axis4Enable_B = {"value":0,"account":"轴4使能"}
        axis5Enable_B = {"value":0,"account":"轴5使能"}
        #轴Jog运动的软限位设置
        axis0Limit_P_Pos_D = {"value": 10,"account":"轴0正向软件限位"}
        axis0Limit_N_Pos_D = {"value": -420,"account":"轴0负向软件限位"}
        axis1Limit_P_Pos_D = {"value": 800,"account":"轴1正向软件限位"}
        axis1Limit_N_Pos_D = {"value": -10,"account":"轴1负向软件限位"}
        axis2Limit_P_Pos_D = {"value": 0,"account":"轴2正向软件限位"}
        axis2Limit_N_Pos_D = {"value": -45,"account":"轴2负向软件限位"}
        axis3Limit_P_Pos_D = {"value": 10,"account":"轴3正向软件限位"}
        axis3Limit_N_Pos_D = {"value": -350,"account":"轴3负向软件限位"}
        axis4Limit_P_Pos_D = {"value": 10,"account":"轴4正向软件限位"}
        axis4Limit_N_Pos_D = {"value": -350,"account":"轴4负向软件限位"}
        axis5Limit_P_Pos_D = {"value": 10,"account":"轴5正向软件限位"}
        axis5Limit_N_Pos_D = {"value": -350,"account":"轴5负向软件限位"}
        # ZMQ端口
        #"""系统各模块ZMQ初始化的端口"""
        Logic_REP_port_I = {"value": 7150 ,"account":"Logic层的REP端bind的端口，GUI层的REQ端应该connect此端口"}  #
        Vision_REP_port_I = {"value": 7250,"account":"Vision层的REP端bind的端口，Logic层的REQ端应该connect此端口"}   #
        Logic_PUB_port_I = {"value": 7350,"account":"Logic层的PUB端bind的端口，GUI层的SUB端应该connect此端口"}   #
        GUI_PUB_port_I = {"value": 7450,"account":"GUI层的PUB端bind的端口，Logic层的SUB端应该connect此端口"}   #
        GUI_REP_port_I = {"value": 7550,"account":"GUI层的REP端bind的端口，Logic层的REQ端应该connect此端口"}   #
        Vision_PUB_port_I = {"value": 7650 ,"account":"Vision层的pub端bind的端口，Logic层的REQ端应该connect此端口"}  #
        distanceDataFile_S = {"value":"D:\isac\lav\lav\Dispensing" ,"account":"飞拍飞点的坐标数据保存文件路径"}   #
        #————————————————————————————————————————————
        #"""UI界面需要根据以下参数初始对应功能或文件选择"""
        language_S = {"value":"EN" ,"account":"语言包 EN-English,CH-中文简体"}       #
        defaultUser_I = {"value": 0,"account":"默认用户：0位操作员，1为管理员，2为开发者"}   #
        openProgram_B = {"value":0 ,"account":"程序运行时默认是否打开上一次的工程  0为不打开，1为打开"}   #
        programFile_S = {"value": 'D:\PythonApp\IAS566_soft\Program',"account":"工程文件夹路径"}   #
        preProgramName_S = {"value": 'FlyTest2_',"account":"记录上一次打开的工程文件名"}  #
        #————————————————————————————————————————————
        useCVHome_B = {"value":0 ,"account":"使用视觉原点  0为不使用，1为使用"}    #
        CVHomeXPos_D = {"value":-10.766 ,"account":"视觉原点的X坐标"} #
        CVHomeYPos_D = {"value":32.109  ,"account":"视觉原点的Y坐标"}  #
        hostValve_I = {"value":1 ,"account":"设置主阀编号"}  #
        valve_CV_XOffset_D = {"value":107.377 ,"account":"胶枪1偏移X方向的量   胶阀点胶中心距离相机中心的X轴偏移量"}  #
        valve_CV_YOffset_D = {"value":22.863 ,"account":"胶枪1偏移Y方向的量   胶阀点胶中心距离相机中心的Y轴偏移量"}  #
        valve2_CV_XOffset_D = {"value":87.377 ,"account":"胶枪2偏移X方向的量   胶阀点胶中心距离相机中心的X轴偏移量"}   #
        valve2_CV_YOffset_D = {"value":22.863  ,"account":"胶枪2偏移Y方向的量   胶阀点胶中心距离相机中心的Y轴偏移量"}  #
        clearXPos_D = {"value":-256.81 ,"account":"胶阀1清洗位的X坐标"}   #
        clearYPos_D = {"value":58.534  ,"account":"胶阀1清洗位的Y坐标"}   #
        clearZPos_D = {"value":-29.136 ,"account":"胶阀1清洗点Z坐标"}   #
        clearXPos2_D = {"value": -256.81,"account":"胶阀2清洗位的X坐标"}  #
        clearYPos2_D = {"value": 58.534 ,"account":"胶阀2清洗位的Y坐标"}  #
        clearZPos2_D = {"value": -29.136,"account":"胶阀2清洗点Z坐标"}  #
        disXPos_D = {"value":-143.388,"account":"胶阀1排胶位的X坐标"}     #
        disYPos_D = {"value":59.91   ,"account":"胶阀1排胶位的Y坐标"}     #
        disZPos_D = {"value":-32.142 ,"account":"胶阀1排胶点Z坐标"}     #
        disXPos2_D = {"value":-143.388,"account":"胶阀2排胶位的X坐标"}    #
        disYPos2_D = {"value":59.91   ,"account":"胶阀2排胶位的Y坐标"}    #
        disZPos2_D = {"value":-32.142 ,"account":"胶阀2排胶点Z坐标"}    #
        XY_maxSpeed_I = {"value":12000,"account":"XY轴最大设定速度    mm/min"}    #
        Z_maxSpeed_I = {"value":6000 ,"account":"Z轴最大设定速度   mm/min"}     #
        U_maxSpeed_I= {"value":960,"account":"U轴最大设定速度   mm/min"}        #
        #Vision默认设置
        maxExposure_I = {"value":1500 ,"account":"曝光设置上限"}   #
        maxGain_I = {"value":15 ,"account":"增益设置上限"}        #
        CV_Exposure_I = {"value":120 ,"account":"曝光时间"}    #
        CV_Gain_I = {"value": 10 ,"account":"增益"}        #
        CV_Equivalent_D = {"value": 0.0133,"account":"像素当量  mm/pix"}     #
        CV_EquivalentXPos_D= {"value":-10.14 ,"account":"获取像素当量时 x轴坐标"} #
        CV_EquivalentYPos_D = {"value":31.958 ,"account":"获取像素当量时 y轴坐标"}   #
        CV_WaitTime_D = {"value": 2.0 ,"account":"拍照等待延时  ms"}     #
        CV_LightSource_Index_I = {"value": 14, "account": "棋盘光源编号"}  #
        CV_LightSource_Gain_I = {"value": 1, "account": "棋盘光源增益"}  #
        CV_LightSource_Exposure_I = {"value": 200, "account": "棋盘拍照曝光时间"}  #
        CV_LightSource_Pos_S = {"value":"(-50,50)", "account": "棋盘拍照坐标"}  #
        CV_LightSource_Gray_I = {"value": 120, "account": "棋盘灰度值"}
        #————————————————————————
        #"""UI界面需要根据以下参数初始化示教界面中不同胶阀对应的胶点单点重量和胶点半径"""
        dotWeight1_D = {"value":0.05  ,"account":"胶阀1胶点重量    单位mg"} #
        dotWeight2_D = {"value":0.05  ,"account":"胶阀2胶点重量    单位mg"} #
        dotRadius1_D = {"value":0.3892,"account":"胶阀1胶点半径    单位mm"}   #
        dotRadius2_D = {"value":0.50  ,"account":"胶阀2胶点半径    单位mm"} #
        #————————————————————————
        dotWeight_XPos_D = {"value":-57.895 ,"account":"胶阀1称重时x轴坐标"}  #
        dotWeight_YPos_D = {"value":60.204  ,"account":"胶阀1称重时Y轴坐标"}  #
        dotWeight_ZPos_D = {"value":-29.43  ,"account":"胶阀1称重时Z轴坐标"}  #
        dotWeight_XPos2_D = {"value": -57.895,"account":"胶阀2称重时x轴坐标"} #
        dotWeight_YPos2_D = {"value": 60.204 ,"account":"胶阀2称重时Y轴坐标"} #
        dotWeight_ZPos2_D = {"value": -29.43 ,"account":"胶阀2称重时Z轴坐标"} #
        C1_AdCurrentPos_D = {"value":141.0    ,"account":"轨道1调宽当前Y轴位置"}    #
        C2_AdCurrentPos_D = {"value":543.147  ,"account":"轨道2调宽当前Y轴位置"}    #
        C1_markedBoardWidth_D = {"value":114.5 ,"account":"轨道1调宽当前Y轴位置对应的板子宽度"}   #
        C2_markedBoardWidth_D = {"value":90.147,"account":"轨道2调宽当前Y轴位置对应的板子宽度"}   #
        LaserToZ_D = {"value":-32.0072,"account":"激光测高零点和Z轴坐标原点的距离 计算Z轴坐标公式为：zPos = LaserToZ - height + dis  height为测高数据，dis为距板面高度"}         #
        high_valveXPos_D= {"value":18.942,"account":"胶阀测高点的位置 X坐标"}      #
        high_valveYPos_D = {"value":65.453,"account":"胶阀测高点的位置 Y坐标"}     #
        high_valveZSafePos_D = {"value":-18.0,"account":"胶阀测高点的位置 Z轴安全位置"}  #
        high_valveZLimitPos_D = {"value":-30.0,"account":"胶阀测高点的位置 Z轴极限位置"} #
        high_valveZSafeVel_I = {"value":600,"account":"胶阀测高点的位置 Z轴安全速度（绝对走速度）"}    #
        high_valveZLimitVel_I = {"value":50,"account":"胶阀测高点的位置 Z轴速度（点动的速度）"}    #
        high_laserXPos_D= {"value":-76.581 ,"account":"激光测高点的位置 X坐标"} #
        high_laserYPos_D = {"value":-13.752 ,"account":"激光测高点的位置 Y坐标"}   #
        safeDoorEnable_B = {"value":1 ,"account":"安全门禁用或启用  1-启用 0-禁用"}  #
        cameraLEDTypeSum_I = {"value":1 ,"account":"相机光源类型总数"}  #
        safeZPos_D = {"value": -6.0,"account":"Z轴安全高度坐标"}  #
        TrackLimitEnable_B = {"value":1  ,"account":"是否启用轨道限位"}   #
        Track1UpperLimit_I = {"value":500,"account":"轨道1宽上限"}   #
        Track1LowerLimit_I = {"value":100,"account":"轨道1宽下限"}   #
        Track2UpperLimit_I = {"value":500,"account":"轨道2宽上限"}   #
        Track2LowerLimit_I = {"value":100,"account":"轨道2宽下限"}   #
        BarrierLockEnable_B = {"value":1 ,"account":"是否启用阻挡上升时XY轴锁"}    #
        MESTcpServerIp_S = {"value":'127.0.0.1' ,"account":"MES tcp服务器的IP地址"}    #
        MESTcpServerPort_I = {"value":8282  ,"account":"MES tcp服务器的端口号"}        #
        MESFileSavePath_S = {"value":"D:/files" ,"account":"MES文件保存路径"}   #
        ConveyorTest_B= {"value":0 ,"account":"轨道测试模式，0-禁用 1-启用 启用之后在在线(OnLine)模式下只会运行皮带逻辑，没有轴动作"}
    class workConfig(object):
        offLineRunTimes_I = {"value": -1,"account":"离线运行次数，0为不执行，-1为无限执行，>0的整数代表要求执行的次数"}  #
        defaultRunMode_I = {"value": 0,"account":"默认运行模式，-1为Online模式，0-5为Offline模式"}   #
        dryRunSpeed_I = {"value":800  ,"account":"空行是的最大速度 mm/s"}  #
        maxWorkSpeed_I = {"value":500 ,"account":"最大工作速度 mm/s"}   #
        bFlyMarkMode_B = {"value": 1,"account":"启用飞行拍Mark的模式  0为不启用 1为启用"}     #
        bFlyICMark_B = {"value":1 ,"account":"启用飞拍ICMark功能点  0-禁用 1-启用"}      #
        bPreHandleICMark_B = {"value":1 ,"account":"是否提前处理ICMark功能点 0-禁用 1-启用"} #
        bFlyAOICheck_B = {"value": 1  ,"account":"启用飞拍AOI功能点  0-禁用 1-启用"}    #
        bPreHandleAOICheck_B = {"value":  1,"account":"是否提前处理AOI功能点 0-禁用 1-启用"}#
        bFlyBarCode_B = {"value":1  ,"account":"启用飞拍条形码功能点  0-禁用 1-启用"}     #
        bPreHandleBarCode_B = {"value":1 ,"account":"是否提前处理条形码功能点 0-禁用 1-启用"} #
        flySpeed_I = {"value":40 ,"account":"飞拍速度  mm/s"}       #
        flyPhotoExposure_I = {"value":120 ,"account":"飞拍的曝光时间 um"} #
        flyPhotoGain_I = {"value":10 ,"account":"飞拍增益"}    #
        flyAxis_S = {"value":"X"  ,"account":"飞拍轴，即确定飞拍方向,仅限X或者Y轴方向"}       #
        flyPhotoLocation_B = {"value": 1,"account":"使用飞拍图像定位  1-启用  0-不启用（测试用，只拍图，不处理）"} #
        flyRasterDelay = {"value":0.8,"account":"飞行触发通讯延时 s"}   #
        dotComDelayX_D = {"value":8.2,"account":"X轴飞行点胶触发通讯延时 ms"}   #
        dotComDelayY_D = {"value":8.3,"account":"Y轴飞行点胶触发通讯延时 ms"}   #
        dotComDelayZ_D = {"value":8.3,"account":"Z轴飞行点胶触发通讯延时 ms"}   #
        arcComDelay_D = {"value": 8.0,"account":"圆弧地点胶触发通讯演示  ms"}    #
        flyComDelayX_D = {"value": 5.35,"account":"X轴飞行触发通讯延时 ms"}   #
        flyComDelayY_D = {"value":6.05 ,"account":"Y轴飞行触发通讯延时 ms"}   #
        flyComDelayZ_D = {"value":5.0  ,"account":"Z轴飞行触发通讯延时 ms"}   #
        pulseShifting_D = {"value": 0,"account":"脉冲偏移 ms  正值为滞后  负值为提前"}  #
        dotOnDelay_D = {"value":0.25 ,"account":"点胶开阀延时 ms"} #
        dotOffDelay_D = {"value":1.0 ,"account":"点胶关阀延时 ms"} #
        motionAMax_I = {"value":10000 ,"account":"XY轴最大加速度"}  #
        motionJerk_I = {"value":116500 ,"account":"XY轴jerk值（加加速）"} #
        LS_D = {"value":1.0 ,"account":"飞点直线轨迹提前距离 mm"}  #
        LE_D= {"value": 1.0,"account":"飞点直线轨迹延后距离 mm"}  #
        VP_I = {"value":1000 ,"account":"胶点喷射速度  mm/s"} #
        bHoldZPos_B = {"value": 1 ,"account":"点胶过程中是否使胶枪在空行轨迹时保持Z轴的点胶高度不变 0为否， 1为是"}       #
        bValveHeat_B = {"value": 1,"account":"是否启用胶阀加热  0为否 1为是"}       #
        bCoverPlateCheck_B = {"value":0 ,"account":"是否启用盖板检测  0为否 1为是"}   #
        valveTemperature_I  = {"value":40 ,"account":"胶阀工作温度  单位℃"}  #
        trackTemperature_I = {"value":80 ,"account":"轨道工作温度  单位℃"}  #
        conveyor1_X_D = {"value":0.1,"account":"轨道1的初始参考点X坐标值"}    #
        conveyor1_Y_D = {"value":0.1,"account":"轨道1的初始参考点Y坐标值"}    #
        conveyor2_X_D = {"value":0.1,"account":"轨道2的初始参考点X坐标值"}    #
        conveyor2_Y_D = {"value":0.1,"account":"轨道2的初始参考点Y坐标值"}    #
        bCheckGlue_B= {"value":0 ,"account":"是否禁用查询胶水剩余 1禁用 0 不禁用"} #
        cleanFreq_I = {"value":100 ,"account":"运行多少次去清洗，小于等于0 表示不清洗"}   #
        clearTimes_I = {"value":3 ,"account":"清洗转多少圈"}   #
        bAutoAdjustConveyor1_B = {"value":0 ,"account":"是否启用轨道1自动调节功能 0-禁用 1-启用"}
        MESEnable_B = {"value":1  ,"account":"是否启用MES"}  #
        MESTcpEnable_B = {"value":1 ,"account":"是否启用MES tcp客户端"}   #
        # MESComEnable_B = {"value":0 ,"account":"是否启用MES com端"}       #
        MESFileEnable_B = {"value":1 ,"account":"是否启用MES file端"}   #
        MESFileRecheck_B = {"value":1 , "account": "是否输出机器判定结果"}  #
        AOIManualCheck_B = {"value":0 ,"account":"是否启用AOI结果人工确认"}   #
        AOIPosCustomize_B = {"value":0 ,"account":"是否启用AOI图片位置自定义"}   #
        TrackUpperTemperature_D = {"value":90.0, "account": "轨道温度上限值"}   #
        TrackLowerTemperature_D = {"value":70.0, "account": "轨道温度下限值"}   #
        ValveUpperTemperature_D = {"value":60.0, "account": "胶阀温度上限值"}   #
        ValveLowerTemperature_D = {"value":30.0, "account": "胶阀温度下限值"}   #
        ptDotRefWeight_D = {"value": 0.039, "account": "单胶点参考重量值"}  #todo 加上参考值显示
        DotUpperWeight_D = {"value": 0.06, "account": "单胶点重量上限值"}  #
        DotLowerWeight_D = {"value": 0.02, "account": "单胶点重量下限值"}  #
        weightMethod_I = {"value":0, "account":"0：不称重 1：开机称重一次 2：固定时间点称重  3：固定时间间隔称重"}  #
        weightTime_S = {"value":'10:00:00,16:00:00', "account": "称重时间点 格式：'08:00:00,16:00:00'"}  #
        timeInterval_D = {"value": '4.0', "account": "固定称重时间间隔，单位：小时"}  #
        valveCheck_S = {"value": '2019-11-15', "account": "维护日期 格式: 2019-11-15"}  #
        valveCheckFreq_I = {"value": '30', "account": "下次维护时间间隔，单位：天"}  #
        lightCheck_S = {"value": '2019-11-15', "account": "光源检测日期 格式: 2019-11-15"}  #
        lightCheckFreq_I = {"value": '30', "account": "下次光源时间间隔，单位：天"}  #


    class valveConfig(object):
        MODE_I = {"value": 1, "account": "模式 1-定时  2-排胶  3-连续"}
        PULSE_D = {"value": 0.5, "account": "脉冲时间(ms)"}
        CYCLE_D = {"value": 2.0, "account": "周期(ms)"}
        COUNT_I = {"value": 1, "account": "计数"}
        Stroke_I = {"value": 90, "account": "行程 1-100"}
        UpRampTime_I = {"value": 100, "account": "up曲线时间 200-1600(us)"}
        DwnRampTime_I = {"value": 100, "account": "dwn曲线时间 250-500(us)"}
        CloseVoltage_I = {"value": 100, "account": "关闭电压 20-120(V)"}
        HeatSwitch_B = {"value": 1, "account": "加热开关"}
        HeatTemperature_D = {"value": 30.0, "account": "加热温度"}
        POWER_B = {"value": 0, "account": "胶阀驱动器电源开关"}

        MODE2_I = {"value":1,"account":"模式 1-定时  2-排胶  3-连续"}
        PULSE2_D = {"value":0.5,"account":"脉冲时间(ms)"}
        CYCLE2_D = {"value":2.5,"account":"周期(ms)"}
        COUNT2_I = {"value":1,"account":"计数"}
        Stroke2_I =  {"value":90,"account":"行程 1-100"}
        UpRampTime2_I = {"value":100,"account":"up曲线时间 200-1600(us)"}
        DwnRampTime2_I = {"value":100,"account":"dwn曲线时间 250-500(us)"}
        CloseVoltage2_I= {"value":100,"account":"关闭电压 20-120(V)"}
        HeatSwitch2_B = {"value":1,"account":"加热开关"}
        HeatTemperature2_D = {"value":30.0,"account":"加热温度"}
        POWER2_B = {"value":0,"account":"胶阀驱动器电源开关"}

    class IOConfig(object):
        #"""----------------------------------INPUT----------------------------------------"""
        IN_GE_Stop = {"value":"nCNC$gEStop","account":"急停信号 True为正常 False为急停被触发"}   # 
        IN_Soft_Limit = {"value":"nCNC$limSwError","account":"软限位报警信号"}  #
        IN_C1_BlockS0 = {"value":"nConv$con1_cylSensor0","account":"皮带线1阻挡气缸1到位传感器信号"} #
        IN_C1_BlockS1 = {"value":"nConv$con1_cylSensor1","account":"皮带线1阻挡气缸1到位传感器信号"} #
        IN_C1_BlockS2 = {"value":"nConv$con1_cylSensor2","account":"皮带线1阻挡气缸2到位传感器信号"} #
        IN_C1_BlockMS = {"value":"nConv$con1_cylMSensor","account":"皮带线1移动边阻挡气缸到位传感器信号"} #
        IN_C1_PushWS = {"value":"nConv$con1_cylCorrectSensorExt","account":"皮带线1推板气缸伸出到位传感器信号"} #
        IN_C1_PushBS = {"value":"nConv$con1_cylCorrectSensorRet","account":"皮带线1推板气缸缩回到位传感器信号"} #
        IN_C1_PressUS = {"value":"nConv$con1_cylUpSensor","account":"皮带线1压板顶升气缸到位传感器信号"} #
        IN_C1_PressMUS = {"value":"nConv$con1_cylMUpSensor","account":"皮带线1移动边压板顶升气缸到位传感器信号"}#
        IN_C1_Cyl1ASF = {"value":"nConv$con1_cylMAdjustSensorFix","account":"皮带线1调宽气缸1锁紧传感器信号"} #
        IN_C1_Cyl1ASR = {"value":"nConv$con1_cylMAdjustSensorRelase","account":"皮带线1调宽气缸1松开传感器信号"} #
        IN_C1_Cyl2ASF = {"value":"nConv$con1_cyl2MAdjustSensorFix","account":"皮带线1调宽气缸2锁紧传感器信号"} #
        IN_C1_Cyl2ASR = {"value":"nConv$con1_cyl2MAdjustSensorRelase","account":"皮带线1调宽气缸2松开传感器信号"} #

        IN_C2_BlockS1 = {"value":"nConv$con2_cylSensor1","account":"皮带线2阻挡气缸1到位传感器信号"}    #
        IN_C2_BlockS2 = {"value":"nConv$con2_cylSensor2","account":"皮带线2阻挡气缸2到位传感器信号"}    #
        IN_C2_BlockMS = {"value":"nConv$con2_cylMSensor","account":"皮带线2移动边阻挡气缸到位传感器信号"}    #
        IN_C2_PressUS = {"value":"nConv$con2_cylUpSensor","account":"皮带线2压板顶升气缸到位传感器信号"}    #
        IN_C2_PressMUS = {"value": "nConv$con2_cylMUpSensor","account":"皮带线2移动边压板顶升气缸到位传感器信号"}   #
        IN_C2_Cyl1ASF = {"value":"nConv$con2_cylMAdjustSensorFix","account":"皮带线2调宽气缸1锁紧传感器信号"}    # 
        IN_C2_Cyl1ASR = {"value":"nConv$con2_cylMAdjustSensorRelase","account":"皮带线2调宽气缸1松开传感器信号"}    #
        IN_C2_Cyl2ASF = {"value":"nConv$con2_cyl2MAdjustSensorFix","account":"皮带线2调宽气缸2锁紧传感器信号"}    #
        IN_C2_Cyl2ASR = {"value":"nConv$con2_cyl2MAdjustSensorRelase","account":"皮带线2调宽气缸2松开传感器信号"}    #

        IN_InsertExtS1 = {"value": "nConv$InsertExtSensor1","account":"调宽插销气缸1下降传感器信号"}   #
        IN_InsertExtS2 = {"value": "nConv$InsertExtSensor2","account":"调宽插销气缸2下降传感器信号"}   #
        IN_InsertRetS1 = {"value":"nConv$InsertRetSensor1" ,"account":"调宽插销气缸1上升感器信号"}   #
        IN_InsertRetS2 = {"value":"nConv$InsertRetSensor2" ,"account":"调宽插销气缸2上升感器信号"}   #

        IN_ZAxisExtS = {"value":"nConv$ZAxisCylExtSensor","account":"Z轴升降气缸降到位传感器信号"} #
        IN_ZAxisRetS = {"value":"nConv$ZAxisCylRetSensor","account":"Z轴升降气缸升到位传感器信号"} #

        IN_C1_S1 = {"value":"nConv$con1_sensor1","account":"皮带线1左往右第1个物料感应信号"} #
        IN_C1_S2 = {"value":"nConv$con1_sensor2","account":"皮带线1左往右第2个物料感应信号"} #
        IN_C1_S3 = {"value":"nConv$con1_sensor3","account":"皮带线1左往右第3个物料感应信号"} #
        IN_C1_S4 = {"value":"nConv$con1_sensor4","account":"皮带线1左往右第4个物料感应信号"} #
        IN_C1_MP = {"value":"nConv$con1_motorPos","account":"皮带线1左往右（正向）转动标志位"} #
        IN_C1_MN = {"value":"nConv$con1_motorNeg","account":"皮带线1右往左（反向）转动标志位"} #

        IN_C2_S1 = {"value":"nConv$con2_sensor1" ,"account":"皮带线2左往右第1个物料感应信号"} 
        IN_C2_S2 = {"value":"nConv$con2_sensor2" ,"account":"皮带线2左往右第2个物料感应信号"} 
        IN_C2_S3 = {"value":"nConv$con2_sensor3" ,"account":"皮带线2左往右第3个物料感应信号"} 
        IN_C2_S4 = {"value":"nConv$con2_sensor4" ,"account":"皮带线2左往右第4个物料感应信号"} 
        IN_C2_MP = {"value": "nConv$con2_motorPos","account":"皮带线2左往右（正向）转动标志位"}
        IN_C2_MN = {"value": "nConv$con2_motorNeg","account":"皮带线2右往左（反向）转动标志位"}
        IN_CameraLED1 = {"value":"nCNC$CameraLed1","account":"相机光源1"}   # 
        IN_CameraLED2 = {"value":"nCNC$CameraLed2","account":"相机光源2"}   # 

        IN_CoverPlate_S = {"value": "nCNC$HightCoverSen","account":"盖板合起感应信号"}   # 
        IN_FrontSafeDoor = {"value": "nCNC$FrontSafeDoor", "account": "前安全门感应信号"}  #
        IN_BackSafeDoor = {"value": "nCNC$BackSafeDoor", "account": "后安全门感应信号"}  #


       # """----------------------------------OUTPUT----------------------------------------"""
        OUT_C1_Run = {"value": "nConv$conveyor1$AutoInBeltRun","account":"皮带1转动"}  #  1位转动，0为停止
        OUT_C1_Cyl0U = {"value": "nConv$conveyor1$cyl0$baseEx","account":"皮带线1固定端阻挡气缸0升"}   #
        OUT_C1_Cyl0D= {"value": "nConv$conveyor1$cyl0$workEx","account":"皮带线1固定端阻挡气缸0降"}   #
        OUT_C1_Cyl1U = {"value": "nConv$conveyor1$cyl1$baseEx","account":"皮带线1固定端阻挡气缸1升"}   #
        OUT_C1_Cyl1D= {"value": "nConv$conveyor1$cyl1$workEx","account":"皮带线1固定端阻挡气缸1降"}   #
        OUT_C1_PushB = {"value": "nConv$conveyor1$cylCorrect$baseEx"  ,"account":"皮带线1推板气缸缩回"} #
        OUT_C1_PushW = {"value":"nConv$conveyor1$cylCorrect$workEx" ,"account":"皮带线1推板气缸伸出"}   #
        OUT_C1_UpD = {"value":"nConv$conveyor1$cylUp$baseEx" ,"account":"皮带线1顶板顶升气缸降"}   #
        OUT_C1_UpU = {"value": "nConv$conveyor1$cylUp$workEx" ,"account":"皮带线1顶板顶升气缸升"}  #
        OUT_C1_Cyl2U = {"value":"nConv$conveyor1$cyl2$baseEx" ,"account":"皮带线1固定端阻挡气缸2升"}   #
        OUT_C1_Cyl2D = {"value":"nConv$conveyor1$cyl2$workEx"  ,"account":"皮带线1固定端阻挡气缸2降"}  #
        OUT_C1_CylMJW = {"value":"nConv$conveyor1$cylMadjust$workEx" ,"account":"皮带线1调宽气缸松"} #
        OUT_C1_CylMJB = {"value":"nConv$conveyor1$cylMadjust$baseEx" ,"account":"皮带线1调宽气缸锁"} #
        OUT_C2_Run = {"value":"nConv$conveyor1$_motorRun"  ,"account":"皮带2转动"}  #   1位转动，0为停止
        OUT_C2_Cyl1U = {"value":"nConv$conveyor2$cyl1$baseEx" ,"account":"皮带线2固定端阻挡气缸1升"}   #
        OUT_C2_Cyl1D = {"value":"nConv$conveyor2$cyl1$workEx"  ,"account":"皮带线2固定端阻挡气缸1降"}  #
        OUT_C2_UpD = {"value":"nConv$conveyor2$cylUp$baseEx" ,"account":"皮带线2顶板顶升气缸降"}   #
        OUT_C2_UpU = {"value":"nConv$conveyor2$cylUp$workEx" ,"account":"皮带线2顶板顶升气缸升"}   #
        OUT_C2_Cyl2U = {"value":"nConv$conveyor2$cyl2$baseEx" ,"account":"皮带线2固定端阻挡气缸2升"}   #
        OUT_C2_Cyl2D = {"value":"nConv$conveyor2$cyl2$workEx" ,"account":"皮带线2固定端阻挡气缸2降"}   #
        OUT_C2_CylMJW = {"value":"nConv$conveyor2$cylMadjust$workEx","account":"皮带线2调宽气缸松"} #
        OUT_C2_CylMJB = {"value":"nConv$conveyor2$cylMadjust$baseEx","account":"皮带线2调宽气缸锁"} #
        OUT_InsertCylW = {"value": "nConv$InsertCyl$workEx","account":"调轨插销气缸降"}   #
        OUT_InsertCylB = {"value": "nConv$InsertCyl$baseEx","account":"调轨插销气缸升"}   #
        OUT_ZAxisCylW = {"value": "nConv$ZAxisCyl$workEx" ,"account":"Z轴升降气缸降"}    #
        OUT_ZAxisCylB = {"value": "nConv$ZAxisCyl$baseEx" ,"account":"Z轴升降气缸升"}    #
        OUT_Light_LED = {"value": "nCNC$Led","account":"机舱照明"}  #
        OUT_GreenLED = {"value":"nCNC$GreenLed","account":"三色灯---绿"}   #
        OUT_RedLED = {"value":"nCNC$RedLed","account":"三色灯---红"}       #
        OUT_YellowLED = {"value":"nCNC$YellowLed","account":"三色灯---黄"} #
        OUT_Dispensing1Enable = {"value":"nCNC$OpenDispensing1" ,"account":"胶阀1点胶使能IO  1使能  0禁用"}   #
        OUT_Dispensing2Enable = {"value":"nCNC$OpenDispensing2" ,"account":"胶阀2点胶使能IO  1使能  0禁用"}   #
        OUT_ValveAirOpen = {"value":"nCNC$OpenDispensingAirSource" ,"account":"胶阀气源开关IO"}  #
        OUT_Valve2AirOpen = {"value": "nCNC$OpenDispensingAirSource2","account":"胶阀2气源开关IO"}   #

class DotCOMs(object):
    name = ''  # 串口名
    enable=1
    portName=''#串口编号
    dataBits = 0  # 位长
    baudRate = 0  # 波特率
    parity = 0  # 奇偶校验位    0：无   1：奇校验   2：偶校验
    stopBits = 0  # 停止位

    def __init__(self,name,enable=1,portName="COM1",dataBits = 8,baudRate=9600,parity=0,stopBits=0):
        super(DotCOMs,self).__init__()
        self.name = str(name)                 #串口名
        self.enable = int(enable)
        self.portName = str(portName)         #串口编号
        self.dataBits = int(dataBits)         #位长
        self.baudRate = int(baudRate)         #波特率
        self.parity = int(parity)   #奇偶校验位    0：无   1：奇校验   2：偶校验
        self.stopBits = int(stopBits)           #停止位
        


MODULE_NAME_LIST = ['DOT']
COM_DICT = dict.fromkeys(MODULE_NAME_LIST,[])   #初始值：{'DOT':[]}

def addModuleForConfigXML(moduleName):
    if moduleName not in MODULE_NAME_LIST:
        MODULE_NAME_LIST.append(moduleName)
        COM_DICT.setdefault(moduleName,[])
def addComForModule(module,*COMs):
    if module not in COM_DICT.keys():
        raise Exception("'%s' is not in MODULE_NAME_LIST "%module)
    for com in COMs:
        if com in COM_DICT[module]:continue
        COM_DICT[module].append(com)


weighCom = DotCOMs('W',portName='COM7')   #称重
heightCom = DotCOMs('H',portName='COM6')  #测高
temperatureCom1 = DotCOMs('T1',portName='COM5')#轨道1加热温度控制
temperatureCom2 = DotCOMs('T2',portName='COM5',enable=0)#轨道2加热温度控制
barCode1Com = DotCOMs('S1',portName='COM1',enable=0) #条码枪1
barCode2Com = DotCOMs('S2',portName='COM2',enable=0) #条码枪1
valveCom1 = DotCOMs('G1',portName='COM8',baudRate=115200,enable=0)    #胶阀加热
valveCom2 = DotCOMs('G2',portName='COM9',baudRate=115200,enable=0)    #胶阀加热
addModuleForConfigXML('DOT')
addComForModule('DOT',valveCom1,valveCom2,weighCom,heightCom,barCode1Com,barCode2Com,temperatureCom1,temperatureCom2)

def reCreateConfigXML(fileName):
    '''
    重新生成参数配置文件(XML)
    :param str fileName:文件名(含路径)
    :return:
    '''
    impl = minidom.getDOMImplementation()
    # 创建一个xml dom
    # 三个参数分别对应为 ：namespaceURI, qualifiedName, doctype
    doc = impl.createDocument(None, None, None)
    # 创建根元素
    rootElement = doc.createElement('configuration')
    rootElement.setAttribute('version',CONFIG_VERSION)
    rootElement.setAttribute('xmlns:xsi', xsi)
    rootElement.setAttribute('xmlns:xsd', xsd)

    for module in COM_DICT.keys():
        moduleElement = doc.createElement('Module')
        moduleElement.setAttribute('name',module)
        rootElement.appendChild(moduleElement)
        for parType in PAR_TYPE_LIST:
            parTypeElement = doc.createElement(parType)
            moduleElement.appendChild(parTypeElement)
            config_Class = None
            if module == "DOT": config_Class = DotConfig
            elif module == "ALC":pass
            elif module == "TM":pass
            else:pass

            if parType == 'Config' and config_Class is not None:
                 for item, val in vars(config_Class).items():
                    if item[0]=='_':continue
                    itemElement = doc.createElement('Item')
                    itemElement.setAttribute('name', str(item))
                    for key, value in vars(val).items():
                        if key[0]=='_':continue
                        addElement = doc.createElement('add')
                        addElement.setAttribute('key', str(key))
                        addElement.setAttribute('value', str(value.get("value",None)))
                        addElement.setAttribute('account', str(value.get("account",None)))
                        itemElement.appendChild(addElement)
                        doc.appendChild(rootElement)
                    # 将子元素追加到根元素中
                    parTypeElement.appendChild(itemElement)
            elif parType == 'COMs':
                for com in COM_DICT[module]:
                    comElement = doc.createElement('com')
                    if isinstance(com,DotCOMs):
                        for key, value in vars(com).items():
                            if key[0]=='_':continue
                            comElement.setAttribute(key, str(value))
                        parTypeElement.appendChild(comElement)
                        doc.appendChild(rootElement)
            elif parType == 'Servers':pass
            elif parType == 'Clients':pass
            else:pass

    doc.appendChild(rootElement)
    # 文件名存在就先备份
    if os.path.exists(fileName):
        if os.path.exists(fileName + ".back.xml"):
            os.remove(fileName + ".back.xml")
        os.rename(fileName, fileName + ".back.xml")
    # 打开test.xml文件 准备写入
    f = open(fileName, 'a',encoding='utf-8')
    # 写入文件
    doc.writexml(f, encoding='utf-8',addindent='\t', newl='\n')
    # 关闭
    f.close()

def readAllConfigXML(fileName):
    """
    将参数配置文件(XML格式)读取到对应类中
    :param str fileName: 文件名(含路径)
    :return:
    """
    # 文件名存在就抛异常
    if not os.path.exists(fileName):
        if os.path.exists(fileName + ".back.xml"):
            os.rename(fileName + ".back.xml", fileName)
        else:
            raise Exception("'%s' is not exist" % fileName)

    tree = ET.parse(fileName)
    root = tree.getroot()
    # 一个节点有tag、attrib、text三个值
    # tag是标签的名字
    # text是标签的内容
    # attrib是标签属性的字典，通过字典的get('key')来获取对应的属性的值

    #判断文件是否符合格式要求
    if root.tag != 'configuration':
        raise Exception('Wrong format!')
    if root.attrib.get('version') != CONFIG_VERSION:
        raise Exception('Version mismatch!')
    # 直接for chile in parent 来遍历节点下的子节点
    for module in root:
        config_Class = None
        if module.attrib.get('name') not in MODULE_NAME_LIST:continue
        if module.attrib.get('name')== 'DOT': config_Class = DotConfig
        elif module.attrib.get('name')=='ALC':pass
        elif module.attrib.get('name')=='TM':pass
        else:pass
        for parType in module:
            if parType.tag == 'Config':
                for ITEM in parType:
                    for item, val in vars(config_Class).items():
                        if ITEM.attrib.get('name') == item:
                            for add in ITEM:
                                for key,value in vars(val).items():
                                    if add.attrib.get('key') == key:
                                        strCmd = "%s.%s.%s ={'value': %s,'account':'%s'}" % (
                                        config_Class.__name__, ITEM.attrib.get('name'), add.attrib.get('key'), add.attrib.get('value'),add.attrib.get("account",value.get("account",None)))
                                        if isinstance(value["value"],str):
                                            strCmd = """%s.%s.%s = {"value":"%s","account":"%s"}"""% (
                                            config_Class.__name__, ITEM.attrib.get('name'), add.attrib.get('key'), add.attrib.get('value'),add.attrib.get("account",value.get("account",None)))
                                        exec(strCmd)

            elif parType.tag == 'COMs':
                comList = COM_DICT[module.attrib.get('name')]
                for com in parType:
                    if comList == []:continue
                    for COM in comList:
                        if not isinstance(COM,DotCOMs):continue
                        if com.attrib.get('name') == COM.name:
                            for key in com.attrib.keys():
                                strCmd = "COM.%s = %s"%(key,com.attrib.get(key))
                                strCmd1 = """isinstance(COM.%s,str)""" % (
                                    key)
                                if eval(strCmd1):
                                    strCmd = "COM.%s = '%s'" % (key, com.attrib.get(key))
                                exec(strCmd)
            elif parType.tag == 'Servers':pass
            elif parType.tag == 'Clients':pass
            else:pass

def readAConfigFromXML(fileName,configType,key,module='DOT'):
    '''
    读取参数配置文件中指定参数值
    :param str fileName: 文件名（含路径）
    :param str module: 指定的module名
    :param str configType: 指定的config类型
    :param str key: 指定的参数名
    :return str val: 返回对应参数的值(字符串)
    '''
    # 文件名存在就先删除掉
    if not os.path.exists(fileName):
        raise Exception("'%s' is not exist" % fileName)

    tree = ET.parse(fileName)
    root = tree.getroot()
    if root.tag != 'configuration':
        raise Exception('Wrong format!')
    if root.attrib.get('version') != CONFIG_VERSION:
        raise Exception('Version mismatch!')

    val = 'ERROR'
    for Module in root:
        if Module.attrib.get('name') == module:
            for config in Module.iter('Config'):
                for item in config:
                    if item.attrib.get('name') ==configType:
                        for add in item:
                            if add.attrib.get('key') == key:
                                val = {"value":add.attrib.get('value'),"account":add.attrib.get('account')}

    if val == 'ERROR':raise Exception('Parameter(%s.%s.%s) lookup failed'%(module,configType,key))
    return val

def writeConfigToXML(fileName,configType,key,value,module='DOT'):
    '''
    指定参数修改
    :param str fileName: 文件名(含路径)
    :param str configType: 参数类型
    :param str key: 参数名
    :param value: 参数要修改的值
    :param str module: 指定的module名
    :return:
    '''
    if not os.path.exists(fileName):
        raise Exception("'%s' is not exist" % fileName)

    tree = ET.parse(fileName)
    root = tree.getroot()
    if root.tag != 'configuration':
        raise Exception('Wrong format!')
    if root.attrib.get('version') != CONFIG_VERSION:
        raise Exception('Version mismatch!')

    for Module in root:
        if Module.attrib.get('name') == module:
            configClass = None
            if module =='DOT':configClass = DotConfig
            elif module == 'ALC':pass
            elif module == 'TM':pass
            else:pass
            for config in Module.iter('Config'):
                for item in config:
                    if item.attrib.get('name') ==configType:
                        for add in item:
                            if add.attrib.get('key') == key:
                                strCmd = """isinstance(configClass.%s.%s['value'],float) and isinstance(value,int)""" % (configType, key)
                                if eval(strCmd):
                                    value = float(value)
                                strCmd = """if not isinstance(configClass.%s.%s['value'],type(value)):
                                    raise Exception('Parameter type mismatch')
                                    """%(configType,key)
                                exec(strCmd,{'value':value,'configClass':configClass})
                                add.attrib['value']=str(value)
                                tree.write(fileName)
                                return
    raise Exception('Parameter(%s.%s.%s) lookup failed' % (module, configType, key))

def readAComFromXML(fileName,comName,key=None,module='DOT'):
    '''
    读取参数配置文件中指定参数值
    :param str fileName: 文件名（含路径）
    :param str module: 指定的module名
    :param str configType: 指定的config类型
    :param str key: 指定的参数名
    :return str val: 返回对应参数的值(字符串)
    '''
    # 文件名存在就先删除掉
    if not os.path.exists(fileName):
        raise Exception("'%s' is not exist" % fileName)

    tree = ET.parse(fileName)
    root = tree.getroot()
    if root.tag != 'configuration':
        raise Exception('Wrong format!')
    if root.attrib.get('version') != CONFIG_VERSION:
        raise Exception('Version mismatch!')

    val = 'ERROR'
    for Module in root:
        if Module.attrib.get('name') == module:
            for config in Module.iter('COMs'):
                for com in config:
                    if com.attrib.get('name') ==comName:
                        if key != ''and key != None :
                            if key in com.attrib:
                                val = com.attrib.get(key)
                        else:val = str(com.attrib)

    if val == 'ERROR':raise Exception('Parameter(%s.%s.%s) lookup failed'%(module,comName,key))
    return val

def writeComParaToXML(fileName,comNmae,key,value,module='DOT'):
    '''
    指定参数修改
    :param str fileName: 文件名(含路径)
    :param str configType: 参数类型
    :param str key: 参数名
    :param value: 参数要修改的值
    :param str module: 指定的module名
    :return:
    '''
    if not os.path.exists(fileName):
        raise Exception("'%s' is not exist" % fileName)

    tree = ET.parse(fileName)
    root = tree.getroot()
    if root.tag != 'configuration':
        raise Exception('Wrong format!')
    if root.attrib.get('version') != CONFIG_VERSION:
        raise Exception('Version mismatch!')

    for Module in root:
        if Module.attrib.get('name') == module:
            comClass = None
            if module =='DOT':comClass = DotCOMs
            elif module == 'ALC':pass
            elif module == 'TM':pass
            else:pass
            for COMs in Module.iter('COMs'):
                for com in COMs:
                    if com.attrib.get('name') ==comNmae:
                        strCmd = '''if not isinstance(comClass.%s,type(value)):
                                    raise Exception('Parameter type mismatch')
                                    '''%key
                        exec(strCmd,{'value':value,'comClass':comClass})
                        com.attrib[key]=str(value)
                        tree.write(fileName)
                        return
    raise Exception('Parameter(%s.%s.%s) lookup failed' % (module, comNmae, key))

if __name__ == "__main__":
    # fileName = '../config/test.xml'
    fileName = '../config/DOTConfig.xml'

    reCreateConfigXML(fileName)
    # readAllConfigXML(fileName)
    # print(COM_DICT['DOT'][0].stopBits)
    try:

        print(type(DotConfig.sysConfig.high_valveXPos["value"]))
        # writeConfigToXML(fileName, 'sysConfig', 'high_valveXPos',float(0.1) )
    except Exception as e:
        print(e)
    # try:
    #     readAllConfigXML(fileName)
    #     conName = heightCom.name
    #     #heightCom.name = 'COM5'
    #     writeComParaToXML(fileName,conName,'name',heightCom.name)
    #     writeConfigToXML(fileName,'workConfig','dryRunSpeed',1500)
    #     print(readAConfigFromXML(fileName,'workConfig','dryRunSpeed'))
    #     print(readAComFromXML(fileName,heightCom.name))
    #
    # except Exception as e:
    #     print(e)