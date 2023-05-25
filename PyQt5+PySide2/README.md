
### 适应屏幕放大比例
使用方式如下：
```
if __name__ == "__main__":
  [QtCore.]QCoreApplication.setAttribute([QtCore.]Qt.AA_EnableHighDpiScaling)
  app = QApplication(sys.argv)
  ...
```
