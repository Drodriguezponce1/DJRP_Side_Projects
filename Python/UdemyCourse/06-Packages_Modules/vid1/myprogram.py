from vid1.mymodule import my_func

from MyMainPackage import some_main_script as m # type: ignore

from MyMainPackage.SubPackage import some_sub_script as s # type: ignore

my_func()

m.report_main()
s.sub_report()