def swapFileData():
    
    fileName =  input("Enter the file name:- ")
    fileName =  input("Enter the file name:- ")

     
    with open(file1, 'r') as a:
    data_a = a.read()

	with open(file2, 'r') as b:
    data_b = b.read()

    with open(file1, 'w') as a:
    a.write(data_b)

    with open(file2, 'w') as b:
    b.write(data_a)

swapFileData() 



   

