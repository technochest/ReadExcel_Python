import ReadWriteExcel as rwXL

Sheet_Name = "Student Names"

List_of_Names = rwXL.Get_Names(Sheet_Name)
for _Names in List_of_Names:
    print(Names)