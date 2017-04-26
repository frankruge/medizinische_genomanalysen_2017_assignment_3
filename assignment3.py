#! /usr/bin/env python2

import vcf
from vcf import utils #vcf.utils.walk_together doesnt work
import hgvs
hgvs.__version__
import hgvs.dataproviders.uta
import hgvs.parser
import hgvs.variantmapper
from bioutils.assemblies import make_name_ac_map
__author__ = 'Frank Ruge'


def compare_two_vcf(a, b):
    lst = []
    if a.CHROM == b.CHROM and a.POS == b.POS:
        return a
        print(b)
    else:
        return 0
class Assignment3:
    
    def __init__(self):
        ## Check if pyvcf is installed
        print("PyVCF version: %s" % vcf.VERSION)
        ## Check if hgvs is installed
        #print("HGVS version: %s" % hgvs.__version__)
        #mother
        self.mother_vcf = vcf.Reader(open("AmpliseqExome.20141120.NA24143.vcf"))
        #self.m_records = list([i for i in self.mother_vcf])
        self.header = self.mother_vcf._header_lines
        #father
        self.father_vcf = vcf.Reader(open("AmpliseqExome.20141120.NA24149.vcf"))
        #self.f_records = list([i for i in self.father_vcf])
        self.header = self.father_vcf._header_lines
        #son
        self.son_vcf = vcf.Reader(open("AmpliseqExome.20141120.NA24385.vcf"))
        #self.s_records = list([i for i in self.son_vcf])
        self.header = self.son_vcf._header_lines

    def get_total_number_of_variants_mother(self):
        count = 0
        for record in self.mother_vcf:
            count += 1
        return count

    def get_total_number_of_variants_father(self):
        count = 0
        for record in self.father_vcf:
            count += 1
        return count
        '''
        Return the total number of identified variants in the mother
        :return: 
        '''
        
        
    def get_total_number_of_variants_son(self):
        count = 0
        for record in self.son_vcf:
            count += 1
        return count
        '''
        Return the total number of identified variants in the father
        :return: 
        '''

       
        
    def get_variants_shared_by_father_and_son(self):
        self.father_vcf = vcf.Reader(open("AmpliseqExome.20141120.NA24149.vcf"))
        self.son_vcf = vcf.Reader(open("AmpliseqExome.20141120.NA24385.vcf"))
        shared = utils.walk_together(self.father_vcf, self.son_vcf)
        #FS_list=[]
        count=0
        for i in shared:
            if i[0] == i[1]:
                #FS_list.append(i)
                count+=1
            else:
                pass
        #print(len(FS_list))
        return count #FS_list
        


    def get_variants_shared_by_mother_and_son(self):
        MS_list = []
        self.mother_vcf = vcf.Reader(open("AmpliseqExome.20141120.NA24143.vcf"))
        self.son_vcf = vcf.Reader(open("AmpliseqExome.20141120.NA24385.vcf"))
        shared = utils.walk_together(self.mother_vcf, self.son_vcf)
        count=0
        for i in shared:
            if i[0] == i[1]:
                count +=1 #MS_list.append(i)
            else:
                pass
        #print(len(MS_list))
        return count #MS_list

    def get_variants_shared_by_trio(self):
        self.father_vcf = vcf.Reader(open("AmpliseqExome.20141120.NA24149.vcf"))
        self.mother_vcf = vcf.Reader(open("AmpliseqExome.20141120.NA24143.vcf"))
        self.son_vcf = vcf.Reader(open("AmpliseqExome.20141120.NA24385.vcf"))
        shared = utils.walk_together(self.father_vcf, self.son_vcf, self.mother_vcf)
        count = 0 #FSM_list = []
        for i in shared:
            if i[0] == i[1] == i[2]: #makes sure that the variants are the same
                count += 1 #FSM_list.append(i)
            else:
                pass
        #print(len(FSM_list))
        return count #FSM_list
        

    def merge_mother_father_son_into_one_vcf(self):
        self.father_vcf = vcf.Reader(open("AmpliseqExome.20141120.NA24149.vcf"))
        self.mother_vcf = vcf.Reader(open("AmpliseqExome.20141120.NA24143.vcf"))
        self.son_vcf = vcf.Reader(open("AmpliseqExome.20141120.NA24385.vcf"))
        FS = open("FSM.vcf", "w")
        FSVCF = vcf.Writer(FS, self.son_vcf, "\n")
        shared = utils.walk_together(self.father_vcf, self.son_vcf, self.mother_vcf)
        count = 0
        for i in shared:
            if i[0] or i[1] or i[2]:  #
                if i[0] is None:
                    if i[1] is None:
                        FSVCF.write_record(i[2]);count += 1
                    elif i[2] is None:
                        FSVCF.write_record(i[1]);count += 1
                    else: #if i[2] and i[1] are true
                        FSVCF.write_record(i[1]);count += 1
                elif i[1] is None:
                    if i[0] is None:
                        FSVCF.write_record(i[2]);count += 1
                    elif i[2] is None:
                        FSVCF.write_record(i[0]);count += 1
                    else: #if i[2] and i[0] are true
                        FSVCF.write_record(i[2]);count += 1
                elif i[2] is None:
                    if i[0] is None:
                        FSVCF.write_record(i[1]);count += 1
                    elif i[1] is None:
                        FSVCF.write_record(i[0]);count += 1
                    else:  # if i[1] and i[0] are true
                            FSVCF.write_record(i[0]);count += 1
                else:
                    FSVCF.write_record(i[0]);count += 1

        FSVCF.close()
        FS.close()
        print("the three have " + str(count) + " variants\n they are saved in FSM.vcf") #53227
        return
        '''
        Creates one VCF containing all variants of the trio (merge VCFs)
        :return: 
        '''
        





    def convert_first_variants_of_son_into_HGVS(self):
        hdp = hgvs.dataproviders.uta.connect()
        vm = hgvs.variantmapper.VariantMapper(hdp)
        count=0
        # Used for parsing
        hgvsparser = hgvs.parser.Parser()  # Parser
        file=open('son_100.hgvs', 'a')
        for entry in self.son_vcf:
            count+=1
            print(str(entry.CHROM) + ' ' + str(entry.POS) + ' ' + str(entry.QUAL))
            if count == 3:
                break
            NC_no = make_name_ac_map("GRCh37.p13")[entry.CHROM]
            #print(NC_no)

        print("Starting conversion. Please wait.")
        return

    def print_summary(self):

        #print(vcf)
        a = assignment1.get_total_number_of_variants_mother(); print('total_number_of_variants_mother: '+str(a))
        b = assignment1.get_total_number_of_variants_father(); print('total_number_of_variants_father: '+str(b))
        c = assignment1.get_total_number_of_variants_son(); print('total_number_of_variants_son: '+str(c))
        nr_shared_FS = assignment1.get_variants_shared_by_father_and_son(); print("variants shared by father and son: "+str(nr_shared_FS))
        nr_shared_MS = assignment1.get_variants_shared_by_mother_and_son(); print("variants_shared by mother and son: "+str(nr_shared_MS))
        shared_FSM = assignment1.get_variants_shared_by_trio(); print("variants shared by trio: "+str(shared_FSM))
        merged_File= assignment1.merge_mother_father_son_into_one_vcf()
        #hgvs does not work
        #hgvs_part=assignment1.convert_first_variants_of_son_into_HGVS();print(hgvs_part)



if __name__ == '__main__':
    print("Assignment 3")
    assignment1 = Assignment3()
    assignment1.print_summary()

