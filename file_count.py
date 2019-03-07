#encoding=utf-8
import os

def count_py_lines(file_path):
    line_count = 0
    space_count=0
    annotation_count=0
    flag =True
    try:
        fp = open(file_path,"r",encoding="utf-8")
        encoding_type="utf-8"
        for i in fp:
            pass
        fp.close()
    except:
        #print(file_path)
        encoding_type="gbk"

    with open(file_path,"r",encoding=encoding_type,errors="ignore") as fp:
        #print(file_path)
        """try:
            fp.read()
        except:
            fp.close()"""
        for line in fp:           
            if line.strip() == "":
                space_count+=1
            else:
                if line.strip().endswith("'''") and flag == False:
                    annotation_count+=1
                    #print(line)
                    flag = True
                    continue
                if line.strip().endswith('"""') and flag == False:
                    annotation_count+=1
                    #print('结尾双引',line)
                    flag = True
                    continue
                if flag == False:
                    annotation_count+=1
                    #print("z",line)
                    continue  
                """if flag == False:
                    annotation_count+=1
                    print("z",line)"""
                if line.strip().startswith("#encoding") \
                        or line.strip().startswith("#-*-"):
                    line_count += 1
                elif line.strip().startswith('"""') and line.strip().endswith('"""') and line.strip() != '"""':
                    annotation_count+=1
                    #print(line)
                elif line.strip().startswith("'''") and line.strip().endswith("'''") and line.strip() != "'''":
                    annotation_count+=1
                    #print(line)
                elif line.strip().startswith("#"):
                    annotation_count+=1
                    #print(line)
                elif line.strip().startswith("'''") and flag == True:
                    flag = False
                    annotation_count+=1
                    #print(line)
                elif line.strip().startswith('"""') and flag == True:
                    flag = False
                    annotation_count+=1
                    #print('开头双引',line)
                else:
                    line_count += 1
    return line_count,space_count,annotation_count

#path=input("请输入您要统计的绝对路径：")
#file_types=input("请输入您要统计的文件类型：")

#print("整个%s有%s类型文件%d个，共有%d行代码"%(path,file_types,len(code_dict),codes))
#print("代码最多的是%s，有%d行代码"%(max_code[1],max_code[0]))

def count_javafile_lines(file_path):
    line_count = 0
    space_count=0
    annotation_count=0
    flag =True
    #read_type=''
    try:
        fp = open(file_path,"r",encoding="utf-8")
        encoding_type="utf-8"
        for i in fp:
            pass
        fp.close()
    except:
        #print(file_path)
        encoding_type="gbk"

    with open(file_path,"r",encoding=encoding_type) as fp:
        #print(file_path)
        for line in fp:           
            if line.strip() == "":
                space_count+=1
            else:
                if line.strip().endswith("*/") and flag == False:
                    flag = True
                    annotation_count+=1
                    continue
                if flag == False:
                    annotation_count+=1
                    continue
                elif line.strip().startswith('/*') and line.strip().endswith('*/'):
                    annotation_count+=1
                elif line.strip().startswith('/**') and line.strip().endswith('*/'):
                    annotation_count+=1                
                elif line.strip().startswith("//") and flag == True:
                    flag = False
                    continue
                else:
                    line_count += 1
    return line_count,space_count,annotation_count
