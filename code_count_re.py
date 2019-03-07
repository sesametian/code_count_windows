#encoding=utf-8
import os,sys
import file_count

def code_count(path,file_types):
    if os.path.exists(path):
        os.chdir(path)
    else:
        #messagebox.showwarning("您输入的路径不存在！")
        print("您输入的路径不存在！")
        #sys.exit()
    
    files_path=[]
    file_types=file_types.split()
    line_count=0
    space_count=0
    annotation_count=0
    file_lines_dict=dict()
    for root,dirs,files in os.walk(path):
        for f in files:
            files_path.append(os.path.join(root,f))

    for file_path in files_path:
        #print(os.path.splitext(file_path)[1][1:])
        file_type=os.path.splitext(file_path)[1][1:]
        if file_type in file_types:
            if file_type.lower()=="java":
                line_num,space_num,annotation_num=file_count.count_javafile_lines(file_path)
                line_count+=line_num
                space_count+=space_num
                annotation_count+=annotation_num
                file_lines_dict[file_path]=line_num,space_num,annotation_num
            if file_type.lower()=="py":
                line_num,space_num,annotation_num=file_count.count_py_lines(file_path)
                line_count+=line_num
                space_count+=space_num
                annotation_count+=annotation_num
                file_lines_dict[file_path]=line_num,space_num,annotation_num
                #file_info=file_show(line_num,space_num,annotation_num)
                #print(file_info[0])
    return line_count,file_lines_dict,space_count,annotation_count
