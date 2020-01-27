# coding=utf-8
'''
Created on Mar 29, 2019

@author: miki
'''






from copy import deepcopy

import InOutFile
import formula


class dataset(object):
    '''
    classdocs
    '''
    #inputfile_path = 'file.xlsx'
    
    #input_data_oxides_sample_mineral_OX_list = [] 
    
    #recalc_data_oxides_cats_OX__list = []
    
    #recalc_data_oxides_cats_OX_by_mineral_list = []
    
    
    
    def __init__(self, inputfile_path):
    
        
        input_data_oxides_sample_mineral_OX_list = InOutFile.readFILE_E_ESTRAI_DATI_MA_CONTROLLA_MINLABEL_SET_OX(inputfile_path)  
        print("DATASET2_1 input_data_oxides_sample_mineral_OX_list", input_data_oxides_sample_mineral_OX_list)
        
        recalc_data_oxides_cats_OX_list = formula.formula_for_a_list_of_dict_oxides(input_data_oxides_sample_mineral_OX_list)
        print("DATASET2_2 recalc_data_oxides_cats_OX_list ", recalc_data_oxides_cats_OX_list)
        
        new_list = deepcopy(recalc_data_oxides_cats_OX_list)
        
        recalc_data_oxides_cats_OX_by_mineral_list = formula.extract_check_calc_specific_sites(new_list)
#        recalc_data_oxides_cats_OX_by_mineral_list = formula.extract_check_calc_specific_sites(recalc_data_oxides_cats_OX_list)
       # print("\nDATASET2_3 recalc_data_oxides_cats_OX_by_mineral_list ", recalc_data_oxides_cats_OX_by_mineral_list)
        
        ##recalc_data_oxides_cats_OX_by_mineral_with_specific_list = formula.XXXXXX(recalc_data_oxides_cats_OX_list)
        
        fileOUT = InOutFile.write_out_base_data(recalc_data_oxides_cats_OX_list, inputfile_path)
        print("WRITE TO EXCEL FILE BASIC RECALC + TAB transpose")
       # InOutFile.write_out_data_by_mineral_with_specific_sites(recalc_data_oxides_cats_OX_by_mineral_list, fileOUT)
        
        InOutFile.write_out_data_by_mineral_with_specific_sites2(recalc_data_oxides_cats_OX_by_mineral_list, fileOUT)
        print("WRITE TO THE SAME EXCEL FILE worksheets, one for each mineral group")
        
        
        InOutFile.writeAX_formatted_input(recalc_data_oxides_cats_OX_by_mineral_list, fileOUT)
        print("WRITE TO EXCEL a last worksheet with same INPUT BUT in AX format")
        
        
        return
    
    
  

#===============================================================================



#     datset_name = ""
#     mineral_analyses_list = []
#     fileData =""
#     file_output = ""
#     oxides_dict_list = []
#     cations_dict_list = []
#     row_oxides = 0
#     col_oxides = 0
#     row_cations = 0
#     col_cations = 0
#     data_input_OX_list = []
#     lista_di_minerali_separati =[]


#     def __init__(self, file_in):
#         
#         
#         ## DATASET
#         
#         print("DATASET setup")
#         print("DATASET filein: ", file_in)
#         self.fileData = file_in
#         newfile=excelXLSX(self.fileData)
#         
#         self.data_input_OX_list = newfile.readFileEXCEL2()
#         print("DATASET self.data_input_OX_list after READFILE EXCEL2()", self.data_input_OX_list)
#         
#         self.oxides_dict_list, self.cations_dict_list = formula_calc.formula_for_a_list_of_dict_oxides(self.data_input_OX_list)
# 
# 
#         
#         print("oxides_list BEFORE mineral=>",self.oxides_dict_list)
#         print("cations_list BEFORE mineral=>",self.cations_dict_list)
#           
#         for (ox, cat) in zip(self.oxides_dict_list, self.cations_dict_list):
#             ## aggiunge una classe per ogni set di dati
#             print("DATASET un mineral per ogni coppia di ox+sum= ", ox, " e cat+sum: ", cat)
#             mineral = mineral_analysis.mineralAnalysis(ox,cat)
#             ## aggiunge ogni classe mineral alla lista di minerali
#             print("DATASET lista di minerali e aggiunge ogni mineral")
#             self.mineral_analyses_list.append(mineral)
#             
#             print("DATASET questo è il MINERAL",mineral)
#             print("DATASET: questi gli oxides in mineral: ", mineral.oxides_dict)
#             print("DATASET: questi i cations in mineral: ", mineral.cations_dict)
#             print("DATASET: questi OX e CAT in mineral: ", mineral.mineral_oxides_cat_dict)
#             print("DATASET QUESTA E' LA lista di minerali in mineral")
#         
#             print("AMPH??? ", mineral.lista_amphibole)
#         
# 
#         
#         
#         #print("list of mineral in dataset\n",self.mineral_analyses_list)
#         
#         print("from DATASET....")
#         print("DATASET input file: ", self.fileData)
#         print("DATASET minerals_list =>",self.mineral_analyses_list)
#         print("DATASET oxides_list =>",self.oxides_dict_list)
#         print("DATASET cations_list =>",self.cations_dict_list)
#         self.show_oxides_list()
#         self.show_cations_list()
#         self.show_minerals_list()
#         
#         
#         #write on outpufile
#         self.writeOXHeaders()
#         self.appendOX2File()
#         self.appendCAT2File()
#         self.transpose_excel()
#         #append_by_mineral()
#         #formula.appendOXYGENS2File()
#         #formula.appendCAT2File()
#         #formula.transpose_excel(formula.file_output)
#         
#         
#         #self.lista_di_minerali_separati = self.extract_list_by_minerals(self.mineral_analyses_list)
#         
#         
#         for k in self.mineral_analyses_list:
#             print("OGNI self.mineral_analyses_list: ",k)
#             
#             
#         for k,v in self.mineral_analyses_list.items():
#             print("k ",k,"and v: ",v)
#             self.write_minerali_separati(k,v)
#     
#     
#     def get_mineral_analyses_list(self):
#         return self.mineral_analyses_list
#     
#     def get_oxides_list(self):
#         return self.oxides_dict_list
#     
#     def get_cations_list(self):
#         return self.cations_dict_list
#     
#     
#     
#     
#     def show_minerals_list(self):       
#         n=0
#         for dic in self.mineral_analyses_list:
#             print("minerals: ",n," = ", dic)
#             n=n+1
#             
#     def show_oxides_list(self):       
#         n=0
#         for dic in self.oxides_dict_list:
#             print("oxides: ",n," = ", dic)
#             n=n+1
#     
#     def show_cations_list(self):
#         n=0
#         for cat in self.cations_dict_list:
#             print("cations: ",n," = ", cat)
#             n=n+1
#     
#     
#     def write_minerali_separati(self, k,v):
#         
#         # k = nome minerale nel gruppo
#         # v = LISTA di dict
#         print("WRITING MMINERALI SEPARATI")
#         global wbook
#         global wsheet
#         #global file_input
# 
#         #OUTPUTFILE
#         print ("FILE INPUT ..."+ self.fileData)
#         file_output = self.removeEXT(self.fileData) +'_'+ k+'.xlsx'
#         print ("FILE OUTPUT ..."+ file_output)
#         #file_output = removeEXT(file_input) + '_OUT.xls'
#         
#         
#         # print ("WRITING HEADERS to FileOUT " + str(self.file_output))
#         wbook = xlsxwriter.Workbook(file_output)
#         wsheet = wbook.add_worksheet(k)
#         global row
#         global col
#         row = 0
#         col = 0
#         #print("DATASET write headers from oxides_dict_list...",self.oxides_dict_list)
# 
#         for l in v[0]:
#             wsheet.write(row, col, l)
#             row += 1
#         row = 0
#         col += 1
# 
# 
#         for mineral in v:
#             for k,v in mineral.items():
#                 wsheet.write(row, col, v)
#                 row += 1
#             col += 1
#             row = 0
#     
#         wbook.close()
#         
#     
#     
#     def writeOXHeaders(self):
#     
#         global wbook
#         global wsheet
#         #global file_input
#     
#     #    file_output = os.path.splitext(os.path.basename(file_input))[0]+'_OUT.xls'
#         print ("FILE INPUT ..."+ self.fileData)
#         self.file_output = self.removeEXT(self.fileData) + '_OUT.xlsx'
#         print ("FILE OUTPUT ..."+ self.file_output)
#         #file_output = removeEXT(file_input) + '_OUT.xls'
#         print ("WRITING HEADERS to FileOUT " + str(self.file_output))
#         #filename = 'A_output.xls'
#     #    workbook = openpyxl.Workbook(filename)
#     # OK    workbook = xlsxwriter.Workbook('A_output.xls')
#     
#         wbook = xlsxwriter.Workbook(self.file_output)
#     #    workbook = open_workbook(filename)
#         wsheet = wbook.add_worksheet("data")
#     #    worksheet = workbook.create_sheet(title="data")
#     
#     ## SCRIVE HEADERS
#         #global row_oxides
#         #global col_oxides
#     
#         row = 0
#         col = 0
#         print("DATASET write headers from oxides_dict_list...",self.oxides_dict_list)
#         print("DATASET write headers from self.data_input_OX_list",self.data_input_OX_list )
#         for k in self.oxides_dict_list[0]:
#             wsheet.write(row, col, k)
#     #        worksheet.append([row, col, k])
#             row += 1
#         row = 0
#         col += 1
#     
#         # for mineral in data_all_list:
#         #     for k,v in mineral.items():
#         #         worksheet.write(row, col, v)
#         #         row += 1
#         #     row = 0
#         #     col += 1
#     
#         print ("column = " + str(col))
#         print ("row = " + str(row))
#     
#         #workbook.close()
#         #workbook.save(filename)
#     
#         wbook.close()
#     
#         global headers_written
#         headers_written = True
#         self.row_oxides = row
#         self.col_oxides = col
#     
#     
#     def appendOX2File(self):
# 
# 
#         wbRD = xlrd.open_workbook(self.file_output)
#         sheets = wbRD.sheets()
#         # open the same file for writing (just don't write yet)
#         wb = xlsxwriter.Workbook(self.file_output)
#         # run through the sheets and store sheets in workbook
#         # this still doesn't write to the file yet
#         for sheet in sheets: # write data from old file
#             newSheet = wb.add_worksheet(sheet.name)
#             for row in range(sheet.nrows):
#                 for col in range(sheet.ncols):
#                     newSheet.write(row, col, sheet.cell(row, col).value)
# 
#         for mineral in self.oxides_dict_list:
#             for k,v in mineral.items():
#                 newSheet.write(self.row_oxides, self.col_oxides, v)
#                 self.row_oxides += 1
#             self.col_oxides += 1
#             self.row_oxides = 0
#     
#         wb.close()
#     
#     def appendCAT2File(self):
#         # open the file for reading
#         #global file_output
#         wbRD = xlrd.open_workbook(self.file_output)
#         sheets = wbRD.sheets()
#         # open the same file for writing (just don't write yet)
#         wb = xlsxwriter.Workbook(self.file_output)
#         # run through the sheets and store sheets in workbook
#         # this still doesn't write to the file yet
#         for sheet in sheets: # write data from old file
#             newSheet = wb.add_worksheet(sheet.name)
#             for row in range(sheet.nrows):
#                 for col in range(sheet.ncols):
#                     newSheet.write(row, col, sheet.cell(row, col).value)
# 
#         print ("data cations apfu CAT list:")
#         print (self.cations_dict_list)
#         starting_row = sheet.nrows+1
#         self.row_cations = starting_row
#         self.col_cations = 1
#     
#         
#         for k in self.cations_dict_list[1]:
#             ##AGGIUNGE HEADERS dei cationi PERO' METTE QUELLI DEL PRIMO IN LISTA
#             newSheet.write(self.row_cations, self.col_cations-1, k)
#             self.row_cations += 1
#         self.row_cations = starting_row
#         self.col_cations = 1
#        
#         for cations_dict in self.cations_dict_list:
# 
#             for k,v in cations_dict.items():
#                 newSheet.write(self.row_cations, self.col_cations, round(v,3))
#             #    newSheet.write(row_cations, col_cations, row_cations*col_cations)
#                 self.row_cations += 1
#     
#     
#             self.col_cations += 1
#             self.row_cations = starting_row
#     
#         wb.close()
#         return
# 
#     def transpose_excel(self):
#         df = pd.read_excel(self.file_output, sheet_name="data")
#         #df.as_matrix()
#         df.values
#         df.transpose()
#         print ("table")
#         print (str(df))
#         print ("transpose")
#         print (str(df.transpose()))
#         writer1 = pd.ExcelWriter(self.file_output)
#         df.to_excel(writer1, sheet_name='TAB', index=False)
#         df.transpose().to_excel(writer1,sheet_name='APPEND', header = False)
#         writer1.save()
#     
#         return
#     
#     def removeEXT(self, file_name_path):
#         filename = os.path.splitext(file_name_path)[0]
#         return filename
#     
#     
#     
#     def extract_list_by_minerals(self,list):
# 
#         self.mineral_analyses_list
#         a_args = []
# 
#         print(self.mineral_analyses_list)
# # alternativa piu' comoda per gestire tutti gli errori (e.g. se dict non 
# # contiene 'a') ma rischiosa se nel try except hai qualcosa di complesso
# #
# # for l in my_list: 
# #     try: 
# #         assert l['a'] not in a_args 
# #         a_args += [l['a']] 
# #     except: 
# #         pass 
#         lista = []
#         for each_analysis in self.mineral_analyses_list:
#             #for l in each_analysis.mineral_oxides_cat_dict:
#             lista.append(each_analysis.mineral_oxides_cat_dict)
#         print("LISTA ", lista)
# 
#         for l in lista:
#             print("l: ",l)
#             if l['mineral'] not in a_args:
#                 a_args += [l['mineral']] 
#         #       print("a_args: ", a_args)
#         
#                 new_list = [[]]*len(a_args)
#         #print("new_list ",new_list)
#         dict_of_list={}
#         for i in range(len(a_args)):
#             #print("i in range(len(a_args)): ",i)
#             
#             for l in [l for l in lista if l['mineral'] == a_args[i]]:
#                 new_list[i] = new_list[i]+[l]
#             
#                 sublist_list = new_list[i]
#             #   print("a_args IN ", a_args[i])
#             #print("sublist_list: ", sublist_list)
#             #print("a_args OUT ", a_args[i])
#             dict_of_list[a_args[i]] = sublist_list
#             #dict_of_list.update(sublist_list)
#         
#             #sublist_i2 = new_list[1]
#             #sublist_i3 = new_list[2]
#         
#         #sublist_a1 = new_list[0]
#         #sublist_a2 = new_list[1]
#         #sublist_a3 = new_list[2]
#         
#         #print(sublist_a1)
#         #print(sublist_a2)
#         #print(sublist_a3)
#         
#         #print("dict_of_list", dict_of_list)
#         
#         for mine, value in dict_of_list.items():
#             print("\nmineral group = ", mine,'is: ', value)
#             for single in value:
#                 print("every mineral analysis: ",single,"")
#                 
#         
#         
#         #print(dict_of_list)
#         return dict_of_list   
#         
# 
# 
#     
# def append_by_mineral():
#         
#     print("TEST TEST TEST append by mineral")
#         
#     return
#===============================================================================

      
if __name__ == '__main__':
    dataset()
    