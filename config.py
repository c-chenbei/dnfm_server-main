#############################################################
#                                                           #
#                       游戏配置清单                         #
#                                                           #
#    以下配置带有'★'的必须根据自己设备进行配置，否则无法运行    #
#           不带'★'的属于游戏性配置,可以不用修改              #
#                                                           #
#############################################################


#############################################################
# 版本（不要修改）
VERSION = '1.3.3B'
# 
# 运行环境配置, GPU环境配置等
# 见requirements.txt
#############################################################


#############################################################
# 游戏分辨率配置
#
# 该参数是指从手机采集的单帧画面大小，画面越大模型推理耗时越长
# 画面越小推识别准确率越低，根据电脑性能设置1500+-500综合最佳
# 低配电脑降低游戏分辨率可以降低性能消耗
# 设置成 0 会使用和手机一样的分辨率
# 例如我的手机是 3200*1440, 配置成1500*675，画面缩小5倍
# 显著降低运算时间
# （该参数并不是窗口大小，窗口可以拖拽边框改变大小）
# （2024/9/24 Issue:使用了opencv模版匹配后，配置分辨率低于1000时
#   部分小图标无法精确识别，建议配置1500+）
# 
#
# 单帧画面宽度（无需配置高度，高度会自动根据手机分辨率计算）
FRAME_WIDTH = 1500
#
# 窗口缩放比例，只影响窗口显示画面大小，不影响推理识别
# 1为单帧画面多大就显示多大，值越小窗口越小
# 也可以手动拖拽窗口边框改变大小，不想每次进入游戏都拖就配置该默认值
WINDOW_SCALE = 0.75
# 画面帧数，每秒采集多少次屏幕画面
# 15即可正常运行，电脑性能高可适当提高
# 使用CPU运算建议30以下，使用GPU运算可提高到最高60
# 如果设置过高，运行时会自动降频到合适的频率
# 如果要跑30帧以上，游戏设置->图像里要开启性能优先模式（不开锁30帧）
# （2024/10/7测试发现实际只能跑到50，因为游戏性能优先模式锁50帧）
FPS = 60
#
#############################################################


#############################################################
# ★小地图房间识别配置★
#
# 先配置下面两个坐标，然后运行游戏，可以看到小地图上的小红点
# 外围小红点必须对齐每个房间中心，否则房间识别不准确
# 调整下面两个参数直到完全对齐为止
# 配置完成后可以设置SHOW_MAP_POINT=False隐藏锚点
# 以下是我的手机(3200*1440)的参数供参考
#
# （如果进图发现人物原地不动，就是该地图坐标没配好）
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
# ★技能按键配置★
#
# 打开/button.json给每个技能按钮配置屏幕坐标
# 
# 设置为True会在屏幕上显示配置的按钮位置和区域，帮助你排查配置问题
# 确认配置无误后可以设为False关闭
SHOW_BUTTON = False
# 随机抖动
# 为避免脚本检测，每次点击屏幕位置时会对点击位置进行随机偏移
# 偏移单位为像素，根据不同分辨率手机设置不同的值
# 不要超过按钮的半径，否则会点到按钮外
# SHOW_BUTTON设为True时，红点半径即是抖动范围
JITTER = 20
#
#############################################################


#############################################################
# ★布万加员工配置★
#
# key:1,2,3..对应的是选择角色界面的位置，目前只支持配置第一行的英雄
# 可以配置多个，也可以间隔比如1,3,4 按顺序靠前的先上班
# value是该英雄的职业，新增职业需要在hero.py中创建对应实例，
# 未创建会使用奶妈的配置作为默认保底
WORKERS = {
    1:"奶妈",
    2:"鬼泣",
    3:"剑魂",
    6:"暗帝",
    4:"剑宗",
    # 5:"剑豪",
}
#
#############################################################


#############################################################
# 匹配细度微调（谨慎调整）
#
# 该脚本会根据设备分辨率自动对匹配模版进行调整使其支持不同设备
# 理论上无需进行任何修改
# 但不同设备依然可能存在未知因素使调整策略未能完美兼容
# 所以开放此参数，TUNING_MATCH 对自动调整策略的结果进行二次微调
# （该参数并非必须调整，如果脚本运行正常不需要修改此参数）
# 使用方法：
# 1.设置 LOG_MATCH = True, 打开匹配日志输出
# 2.运行游戏,在赛利亚房间点start,查看控制台输出的‘匹配精度’
# 3.如果匹配精度低于0.7则说明失败,调整TUNING_MATCH (0.90-1.10)
# 4.调整TUNING_MATCH需要重新运行脚本,直到精度达到0.9左右
# （TUNING_MATCH设置为1时，不会进行微调）
# （0.90-1.10并非强制范围，但大多数情况取值应该在这个范围）
# （游戏过程中匹配精度偶尔低于0.7，甚至更低属正常情况）
TUNING_MATCH = 1.00
# 是否输出匹配日志
LOG_MATCH = False
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
# 随机的方向是上方，就会再过5秒再随机一次，直到随机到下方脱离卡位
#
BLOCKER_TIME_OUT = 5000
#
#############################################################


#############################################################
# 自动维修装备
#
# 每通关几次维修一次（首次进入副本也会维修）
REPAIR_TIMES = 5
#
#############################################################


#############################################################
# 摸鱼配置
#
# 设置窗口透明度（0-1的小数）最低到0.01
#
ALPHA = 1
#
#############################################################


##########################################################################################################################
# 
# TODO LIST
#
# 1.卡位优化：目前卡位检测仅在没有怪的时候触发，目前发现部分英雄（导师套鬼泣）会偶尔被识别成怪物导致卡位机制失效
#   还有一种情况，第二个房间的冰元素，在人物被卡住时有时候不会主动来攻击，导致一直僵持
#   解决方案，打算将有怪物的情况也包含在卡位检测中，但这样会导致打怪时也会5秒触发一次卡位补救影响过图速度
#   方案二是单独为有怪的情况计时，不管有没有怪，1分钟内（狮子头房2分钟）没过图就认为被卡位
#   （已完成）
#   
# 2.布万加上路：虽然目前的脚本不支持上路，如果进入了上路房间角色会自行返回，但是如果在上路连续进错两个房间，就无法识别当前位置了
#   导致人物失去导航，考虑更新房间算法，把上路房间也包括进去
#
# 3.选择角色页面，目前只能支持选择第一排的英雄，有待优化
# 4.广告页面，切换角色时经常弹出广告，需要对广告做识别并关闭（已完成）
# 5.模版匹配优化，目前匹配是全屏匹配，性能有浪费，对精度也有影响，需要进行优化使用蒙板技术做局部匹配（已完成）
# 6.疲劳检查，在没有引入文字识别库之前，目前没有比较好的方案，需要把FRAME_WIDTH配置到1500+才能有比较好的精准度
# 7.300疲劳弹窗，需要识别并关闭（已完成）
# 8.Issue:自动修装备，物品栏满了的时候无法识别（已完成）
# 9.英雄职业配置切换（已完成）
# 10.9.25更新后狮子头房出来进入6号房时，有时候会把左门识别成右门，导致人物反复进出（已完成）
# 11.人物行为优化，自动战斗时人物朝怪靠近时经常跑过，可以考虑把Y轴的位移时间根据距离换算（已完成，待测试）
# 12.模版匹配有小概率会失败，应该加入一个全局的重试机制，避免卡流程
# 13.scrcpy内置了adb，考虑移除对外部环境adb的依赖，使用内置adb发送命令（已完成）
# 14.设置的FRAME_WIDTH和实际画面有几个像素的差距，应该使用实际画面宽，虽然只有几个像素但不舒服
# 15.职业识别，自动识别职业使用该职业配置
# 16.修装备，没有勾选'穿戴装备'选项时无法修理（已完成）
# 17.找怪逻辑优化，目前找怪是以向目标矩形底边中心点为目标移动，最终结果是和怪重叠，实际应该以目标矩形最近的近角为目的，走到目标正前方
# 18.维修时自动分解出售装备（分解白装，出售蓝紫装）（已完成）
# 
##########################################################################################################################