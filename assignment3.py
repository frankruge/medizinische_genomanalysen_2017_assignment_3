#! /usr/bin/env python2

import vcf
from vcf import utils #vcf.utils.walk_together doesnt work
#import hgvs
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
        #self.mother_vcf = vcf.Reader(open("AmpliseqExome.20141120.NA24143.vcf"))
        #self.m_records = list([i for i in self.mother_vcf])
        #self.header = self.mother_vcf._header_lines
        #father
        #self.father_vcf = vcf.Reader(open("AmpliseqExome.20141120.NA24149.vcf"))
        #self.f_records = list([i for i in self.father_vcf])
        #self.header = self.father_vcf._header_lines
        #son
        #self.son_vcf = vcf.Reader(open("AmpliseqExome.20141120.NA24385.vcf"))
        #self.s_records = list([i for i in self.son_vcf])
        #self.header = self.son_vcf._header_lines

    def get_total_number_of_variants_mother(self):
        count = 0
        for record in self.m_records:
            count += 1
        return count

    def get_total_number_of_variants_father(self):
        count = 0
        for record in self.f_records:
            count += 1
        return count
        '''
        Return the total number of identified variants in the mother
        :return: 
        '''
        
        
    def get_total_number_of_variants_son(self):
        count = 0
        for record in self.s_records:
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
        FS_list=[]
        for i in shared:
            if i[0] == i[1]:
                FS_list.append(i)
            else:
                pass
        print(len(FS_list))
        return FS_list
        


    def get_variants_shared_by_mother_and_son(self):
        MS_list = []
        self.mother_vcf = vcf.Reader(open("AmpliseqExome.20141120.NA24143.vcf"))
        self.son_vcf = vcf.Reader(open("AmpliseqExome.20141120.NA24385.vcf"))
        shared = utils.walk_together(self.mother_vcf, self.son_vcf)
        for i in shared:
            if i[0] == i[1]:
                MS_list.append(i)
            else:
                pass
        print(len(MS_list))
        return MS_list

    def get_variants_shared_by_trio(self):
        self.father_vcf = vcf.Reader(open("AmpliseqExome.20141120.NA24149.vcf"))
        self.mother_vcf = vcf.Reader(open("AmpliseqExome.20141120.NA24143.vcf"))
        self.son_vcf = vcf.Reader(open("AmpliseqExome.20141120.NA24385.vcf"))
        shared = utils.walk_together(self.father_vcf, self.son_vcf, self.mother_vcf)
        FSM_list = []
        for i in shared:
            if i[0] == i[1] == i[2]: #makes sure that the variants are the same
                FSM_list.append(i)
            else:
                pass
        print(len(FSM_list))
        return FSM_list
        

    def merge_mother_father_son_into_one_vcf(self):
        self.father_vcf = vcf.Reader(open("AmpliseqExome.20141120.NA24149.vcf"))
        self.mother_vcf = vcf.Reader(open("AmpliseqExome.20141120.NA24143.vcf"))
        self.son_vcf = vcf.Reader(open("AmpliseqExome.20141120.NA24385.vcf"))
        FS = open("FS.vcf", "w")
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
        print(count) #53227
        return
        '''
        Creates one VCF containing all variants of the trio (merge VCFs)
        :return: 
        '''
        

    def convert_first_variants_of_son_into_HGVS(self):
        '''
        Convert the first 100 variants identified in the son into the corresponding transcript HGVS.
        Each variant should be mapped to all corresponding transcripts. Pointer:
        - https://hgvs.readthedocs.io/en/master/examples/manuscript-example.html#project-genomic-variant-to-a-new-transcript
        :return: 
        '''
        print("TODO")
        
    
    def print_summary(self):

        #print(vcf)
        #a = assignment1.get_total_number_of_variants_mother(); print(a)
        #a = assignment1.get_total_number_of_variants_father(); print(a)
        #a = assignment1.get_total_number_of_variants_son(); print(a)
        #nr_shared_FS = assignment1.get_variants_shared_by_father_and_son();#print(nr_shared_FS)     #152
        #nr_shared_MS = assignment1.get_variants_shared_by_mother_and_son();#print(nr_shared_MS)   #91
        #shared_FS = assignment1.get_variants_shared_by_trio(); print(shared_FS) #1   Record(CHROM=chr1, POS=871334, REF=G, ALT=[T])
        merged_File= assignment1.merge_mother_father_son_into_one_vcf()
        #assignment1.merge_mother_father_son_into_one_vcf()
        #print(len(shared_MS))


if __name__ == '__main__':
    print("Assignment 3")
    assignment1 = Assignment3()
    assignment1.print_summary()

