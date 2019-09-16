
import win32com.client as wc
#启动Excel应用
excel_app = wc.Dispatch('Excel.Application')
#连接excel
workbook = excel_app.Workbooks.Open(r'C:/Users/eas/source/repos/PengboNewsApi/PengboNewsApi/epplus_bug.xlsx' )
#写入数据
workbook.ActiveSheet.Cells(11,11).Style.Locked = 1;
workbook.ActiveSheet.Protect("123", 1);

#关闭并保存
#excel_app.Visible =1
workbook.Save( )
excel_app.Application.Quit()