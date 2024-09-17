
#############################################################
# 游戏分辨率配置
#
# 该参数是指从手机采集的单帧画面大小，画面越大模型推理耗时越长
# 画面越小推识别准确率越低，根据电脑性能设置800-1600综合最佳
# 低配电脑降低游戏分辨率可以降低性能消耗
# 设置成 0 会使用和手机一样的分辨率
# 例如我的手机是 3200*1440, 配置成1000*450，画面缩小10倍
# 显著降低能耗
# （该参数并不是窗口大小，窗口可以拖拽边框改变大小）
# 
# 
#
# 单帧画面宽度（无需配置高度，高度会自动根据手机分辨率计算）
FRAME_WIDTH = 1000
#
#############################################################


#############################################################
# 小地图房间识别配置
#
# 先配置下面两个坐标，然后运行游戏，可以看到小地图上的小红点
# 外围小红点必须对齐每个房间中心，否则房间识别不准确
# 调整下面两个参数直到完全对齐为止
# 配置完成后可以设置SHOW_MAP_POINT=False隐藏锚点
# 以下是我的手机(3200*1440)的参数供参考
#
# （寻路模式目前只支持布万加下路，意外进入上路房间会自行返回下路）
#
# 显示锚点，初次配置建议开启
SHOW_MAP_POINT = True
# 小地图中心点坐标（蓝色小人）
CENTER_POINT = (2950, 174)
# 小地图中心点距相邻房间中心点距离（=房间直径）
OFFSET_ROOM = 77
#
#############################################################


#############################################################
# 卡位补救配置
#
# 卡位超时时间：毫秒
#（超过这个时间无法进门会被判定为卡位，并执行补救措施）
# 补救算法：
# 随机朝一个方向移动一段距离，可能需要多次触发才能脱离卡位
# 比如：走进了一个只能往下走才能出来的角落，卡位补救超时触发
# 随机的方向是上方，就会再过5秒再随机一次，直到随机到下方
#
BLOCKER_TIME_OUT = 5000
#
#############################################################


#############################################################
# 再次挑战点击坐标
#
# 暂时还没写，先配个坐标再说
# 再次挑战
AGAIN = (2814, 189)
# 返回城镇
GOHOME = (2814, 482)
#
#############################################################


#############################################################
# 技能配置
#
# 打开/button.json给每个技能按钮配置屏幕坐标
# 
# 设置为True会在屏幕上显示配置的按钮位置和区域，帮助你排查配置问题
# 确认配置无误后可以设为False关闭
SHOW_BUTTON = True
# 随机抖动
# 为避免脚本检测，每次点击屏幕位置时会对点击位置进行随机偏移
# 偏移单位为像素，根据不同分辨率手机设置不同的值
# 不要超过按钮的半径，否则会点到按钮外
# SHOW_BUTTON设为True时，红点半径即是抖动范围
JITTER = 20
#
#############################################################


#############################################################
# 摸鱼配置
#
# 设置窗口透明度（0-1的小数）最低到0.01
#
ALPHA = 0.9
#
#############################################################