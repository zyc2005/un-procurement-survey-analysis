import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 'Microsoft YaHei' 为微软雅黑
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

def main():
    # 创建图形和轴对象
    font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=10)

    fig, ax = plt.subplots(figsize=(12, 18), dpi=200, subplot_kw={'projection': ccrs.PlateCarree()})
    
    # 添加地图特征
    ax.add_feature(cfeature.LAND)
    ax.add_feature(cfeature.OCEAN)
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS, linestyle=':')
    ax.add_feature(cfeature.LAKES, alpha=0.5)
    ax.add_feature(cfeature.RIVERS)
    
    # 设置地图范围
    ax.set_extent([73, 135, 18, 55])  # [西经, 东经, 南纬, 北纬]

    # 城市和坐标
    cities = {
        "北京": (116.407396, 39.904200),
        "上海": (121.473701, 31.230416),
        "苏州": (120.585316, 31.298886),
        "杭州": (120.155070, 30.274085),
        "嘉兴": (120.755486, 30.746129),
        "福州": (119.296494, 26.074508),
        "衢州": (118.859457, 28.970079),
        "池州": (117.491568, 30.664800),
        "武汉": (114.305392, 30.593099),
        "威海": (122.120420, 37.513068),
        "台州": (121.420757, 28.656386),
        "金华": (119.647444, 29.079059),
        "天津": (117.200983, 39.084158),
        "济宁": (116.587245, 35.414590),
        "郑州": (113.625368, 34.746600),
        "合肥": (117.227239, 31.820586),
        "宁波": (121.549792, 29.868388),
        "南京": (118.796877, 32.060255),
        "青岛": (120.382639, 36.067082),
        "石家庄": (114.514859, 38.042307),
        "西安": (108.940174, 34.341568),
        "广州": (113.264385, 23.129112),
        "长沙": (112.938814, 28.228209),
        "乌鲁木齐": (87.616848, 43.825592),
        "深圳": (114.057868, 22.543099),
        "平顶山": (113.192661, 33.766169),
        "昆明": (102.832891, 24.880095),
        "晋城": (112.851831, 35.490701)
    }

    # 在地图上标记城市
    for city, (lon, lat) in cities.items():
        ax.plot(lon, lat, marker='o', color='red', markersize=2, transform=ccrs.Geodetic())
        ax.text(lon + 0.5, lat - 0.5, city, fontsize=4, transform=ccrs.Geodetic())

    plt.title('Distribution of surveyed companies in China')
    plt.show()

if __name__ == "__main__":
    main()
