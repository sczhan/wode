# GUI介绍
- GraphicalUserInterface,
- GUI for Python: Tkinter, wxPython, pyQt
- Tkinter:
    - 绑定的是TK GUI工具集, 用途Python包装的Tcl代码
- PyGTK
    - Tkinter的替代品
- wxPython
    - 跨平台的Python GUI
- PyOt
    - 跨平台的
    - 商业授权可能有问题
- 推荐资料
    - 辛星GUI, 辛星Python
    - Python GUI Programming cookbook
    - Tkinter reference a GUI for python
    
    
# 测试tkinter包是否好用
import tkinter
tkinter._test() 


# hello world
import tkinter

base = tkinter.Tk()
base.title("hello world")
# 消息循环
base.mainloop()


### Tkinter 常用组件
- 按钮
        Button             按钮组件就
        RadioButton        单选框组件
        CheckButton        选择按钮组件
        Listbox            列表框组件
        
- 文本输入组件
        Entry              单行文本框组件
        Text               多行文本框组件
        
- 标签组件
        Label              标签组件, 可以显示图片和文字
        Message            标签组件, 可以根据内容将文字换行

- 菜单
        Menu               菜单组件
        MenuButton         菜单按钮组件, 可以使用Menu代替

- 滚动条
        scale              滑块组件
        Scrollbar          滚动条组件
        
- 其他组件
        Canvas             画布组件
        Frame              框架组件, 将多个组件编组
        Toplevel           创建子窗口容器组件
        
### 组件的大致使用步骤
1. 创建总面板
2. 创建面板上的各种组件
    1. 指定组件的父组件, 即依附关系
    2. 利用相应的属性对组件进行设置
    3. 给组件安排布局
3. 同步骤2相似, 创建好多个组件
4. 最后, 启动总面板的消息循环



# Label 的例子1
import tkinter

base = tkinter.Tk()

# 负责标题
base.wm_title("Label Test")

lb = tkinter.Label(base, text="Python")

# 给相应组件指定布局
lb.pack()
base.mainloop()



# Label 的例子2
import tkinter

base = tkinter.Tk()
base.title("Label Test")

# 支持属性很多background, font, underline等
# 第一个参数, 制定所属
lb1 = tkinter.Label(base, text="Python AI")
lb1.pack()

lb2 = tkinter.Label(base, text="绿色背景", background="green")
lb2.pack()

lb3 = tkinter.Label(base, text="蓝色背景", background="blue")
lb3.pack()
base.mainloop()



# Button的案例
import tkinter

def showLabel():
    global baseFrame
    # 在函数中定义了一个label
    # label 的父组件是baseFrame
    lb = tkinter.Label(baseFrame, text="显示Label")
    lb.pack()
    
baseFrame = tkinter.Tk()
# 生成一个按钮
# command参数指示, 当按钮被按下的时候,执行那个函数
btn = tkinter.Button(baseFrame, text="show Label", command=showLabel,  background="blue")
# btn = tkinter.Button(baseFrame, text="show Label", background="blue")
btn.pack()

baseFrame.mainloop()
