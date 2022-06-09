def merge(names_of_input_files,name_of_output_file):
    output_file = open(name_of_output_file,"w")
    for name_of_input_file in names_of_input_files:
        input_file = open(name_of_input_file,"r")
        for i in input_file:
            output_file.write(i)
        input_file.close()
    output_file.close()

merge(["input1.txt","input2.txt","input3.txt","input4.txt"],"merge_result.txt")