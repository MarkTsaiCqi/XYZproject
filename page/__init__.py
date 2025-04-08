from selenium.webdriver.common.by import By



"""
    **************档案管理，列表路径**************
"""
# -------左侧菜单:档案管理---------//*[@id="app"]/div/section/aside/div/ul/li[1]/div
FILE_MANAGE =By.XPATH, "//*[@id='app']/div/section/aside/div/ul/li[1]/div"
# -------档案管理列表下的数据---------
MAINTENANCE_UNITY = By.XPATH, "//*[@id='app']/div/section/aside/div/ul/li[1]/ul/a[1]"
PERSONNEL_UNITY = By.XPATH, "//*[@id='app']/div/section/aside/div/ul/li[1]/ul/a[2]"
PROPERTY_UNITY = By.XPATH, "//*[@id='app']/div/section/aside/div/ul/li[1]/ul/a[3]"
RESCUE_UNITY = By.XPATH, "//*[@id='app']/div/section/aside/div/ul/li[1]/ul/a[4]"
INSTALL_UNITY = By.XPATH, "//*[@id='app']/div/section/aside/div/ul/li[1]/ul/a[5]"
FACTORY_UNITY = By.XPATH, "//*[@id='app']/div/section/aside/div/ul/li[1]/ul/a[6]"
INSURANCE_UNITY = By.XPATH, "//*[@id='app']/div/section/aside/div/ul/li[1]/ul/a[7]"
OTHER_UNITY = By.XPATH, "//*[@id='app']/div/section/aside/div/ul/li[1]/ul/a[8]"


"""
    **************电梯数据，列表路径**************
"""
# -------左侧菜单:电梯数据---------
ELEVATOR_DATE = By.XPATH, "//*[@id='app']/div/section/aside/div/ul/li[2]"
# -------电梯数据列表下的数据---------
ELEVATOR_BRAND = By.XPATH, "//*[@id='app']/div/section/aside/div/ul/li[2]/ul/a[1]/li"
ELEVATOR_VIDEO = By.XPATH, "//*[@id='app']/div/section/aside/div/ul/li[2]/ul/a[2]/li"
ELEVATOR_INFORMATION = By.XPATH, "//*[@id='app']/div/section/aside/div/ul/li[2]/ul/a[3]/li"
ELEVATOR_DISTRIBUTE = By.XPATH, "//*[@id='app']/div/section/aside/div/ul/li[2]/ul/a[4]/li"
ELEVATOR_MONITOR = By.XPATH, "//*[@id='app']/div/section/aside/div/ul/li[2]/ul/a[5]/li"


"""
    **************电梯维保，列表路径**************
"""
# -------左侧菜单:电梯维保---------
ELEVATOR_MAINTENANCE =By.XPATH, "//*[@id='app']/div/section/aside/div/ul/li[3]"
# -------电梯维保列表下的数据---------
MAINTENANCE_RULE =By.XPATH, "//*[@id='app']/div/section/aside/div/ul/li[3]/ul/a[1]/li"
MAINTENANCE_MANAGE =By.XPATH, "//*[@id='app']/div/section/aside/div/ul/li[3]/ul/a[2]/li"
ELEVATOR_MAINTENANCE_TWO =By.XPATH, "//*[@id='app']/div/section/aside/div/ul/li[3]/ul/a[3]/li"
MAINTENANCE_OVERDUE =By.XPATH, "//*[@id='app']/div/section/aside/div/ul/li[3]/ul/a[4]/li"
MAINTENANCE_RECORD =By.XPATH, "//*[@id='app']/div/section/aside/div/ul/li[3]/ul/a[5]/li"
MAINTENANCE_PLAN =By.XPATH, "//*[@id='app']/div/section/aside/div/ul/li[3]/ul/a[6]/li"
MAINTENANCE_CALENDAR =By.XPATH, "//*[@id='app']/div/section/aside/div/ul/li[3]/ul/a[7]/li"


"""
    **************信息管理，列表路径**************
"""
# -------左侧菜单:信息管理---------
INFORMATION_MANAGE =By.XPATH, "//*[@id='app']/div/section/aside/div/ul/li[4]"
# -------信息管理列表下的数据---------
CONTRACT_MANAGE = By.XPATH, "//*[@id='app']/div/section/aside/div/ul/li[4]/ul/a[1]"
MAINTENANCE_KNOWLEDGE = By.XPATH, "//*[@id='app']/div/section/aside/div/ul/li[4]/ul/a[2]"
NOTICE = By.XPATH, "//*[@id='app']/div/section/aside/div/ul/li[4]/ul/a[3]"



"""
    **************报警管理，列表路径**************
"""
# -------左侧菜单:报警管理---------
POLICE_MANAGE =By.XPATH, "//*[@id='app']/div/section/aside/div/ul/li[5]"
# -------报警管理列表下的数据---------


"""
    **************应急管理，列表路径**************
"""
# -------左侧菜单:应急管理---------
RESUCE_MANAGE =By.XPATH, "//*[@id='app']/div/section/aside/div/ul/li[6]"
# -------应急管理列表下的数据---------
RESUCE_MANAGE2 =By.XPATH, "//*[@id='app']/div/section/aside/div/ul/li[6]/ul/a/li"

"""
    **************故障申报，列表路径**************
"""
# -------左侧菜单:故障申报---------
FAILURE_DECLARE =By.XPATH, "//*[@id='app']/div/section/aside/div/ul/li[7]"
# -------故障申报列表下的数据---------
FAILURE_DECLARE2 =By.XPATH, "//*[@id='app']/div/section/aside/div/ul/li[7]/ul/a/li"


"""
    **************系统设置，列表路径**************
"""
# -------左侧菜单:系统设置---------
SYSTEM_SET =By.XPATH, "//*[@id='app']/div/section/aside/div/ul/li[8]"
# -------系统设置列表下的数据---------
USER_MANAGE =By.XPATH, "//*[@id='app']/div/section/aside/div/ul/li[8]/ul/a[1]/li"
ROLE_MANAGE =By.XPATH, "//*[@id='app']/div/section/aside/div/ul/li[8]/ul/a[2]/li"











