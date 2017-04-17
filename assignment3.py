#! /usr/bin/env python2

import vcf
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
        self.mother_vcf = vcf.Reader(open("AmpliseqExome.20141120.NA24143.vcf"))
        self.m_records = list([i for i in self.mother_vcf])
        self.header = self.mother_vcf._header_lines
        #father
        self.father_vcf = vcf.Reader(open("AmpliseqExome.20141120.NA24149.vcf"))
        self.f_records = list([i for i in self.father_vcf])
        self.header = self.father_vcf._header_lines
        #son
        self.son_vcf = vcf.Reader(open("AmpliseqExome.20141120.NA24385.vcf"))
        self.s_records = list([i for i in self.son_vcf])
        self.header = self.son_vcf._header_lines

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
        FS_list=[]
        for i, j in zip(self.f_records, self.s_records):

            if i.CHROM == j.CHROM and i.POS == j.POS and i.REF == j.REF and i.ALT == j.ALT:
                FS_list.append(i)
                print(i)
            else:
                pass
        print(len(FS_list))
        return (FS_list)
        '''
        Return the number of identified variants shared by father and son
        :return: 
        '''
        print("TODO")
        


    def get_variants_shared_by_mother_and_son(self):
        MS_list = []
        for i, j in zip(self.m_records, self.s_records):

            if i.CHROM == j.CHROM and i.POS == j.POS and i.REF == j.REF and i.ALT == j.ALT:
                MS_list.append(i)
                print(i)
            else:
                pass
        print(len(MS_list))
        return (MS_list)
        '''
        Return the number of identified variants shared by mother and son
        :return: 
        '''
        
    def get_variants_shared_by_trio(self, m, f):
        #to make it quicker I'll input the results of the mother_son and father_son
        #basically the same as above
        trio_list = []
        for i, j in zip(m, f):

            if i.CHROM == j.CHROM and i.POS == j.POS and i.REF == j.REF and i.ALT == j.ALT:
                trio_list.append(i)
                print(i)
            else:
                pass
        print(len(trio_list))
        return (trio_list)

        '''
        Return the number of identified variants shared by father, mother and son
        :return: 
        '''
        print("TODO")
        

    def merge_mother_father_son_into_one_vcf(self, m_s, f_s):
        file = open("triomerge", 'w')
        mom = []
        dad = []
        son = []
        for i, j in zip(self.m_records, m_s):
            if i.CHROM == j.CHROM and i.POS == j.POS and i.REF == j.REF and i.ALT == j.ALT:
                pass
            else:
                MS.append(i)
        for i, j in zip(MS, f_s):
            if i.CHROM == j.CHROM and i.POS == j.POS and i.REF == j.REF and i.ALT == j.ALT:
                pass
            else:
                MS.append(i)
                vcf.Writer(i, , lineterminator='\n')
        print(len(MS_list))
        return (MS_list)
        '''
        Creates one VCF containing all variants of the trio (merge VCFs)
        :return: 
        '''
        print("TODO")
        

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
        #shared_FS = assignment1.get_variants_shared_by_trio(nr_shared_MS, nr_shared_FS);#print(shared_FS) #1   Record(CHROM=chr1, POS=871334, REF=G, ALT=[T])

        assignment1.merge_mother_father_son_into_one_vcf()
        #print(len(shared_MS))


if __name__ == '__main__':
    print("Assignment 3")
    assignment1 = Assignment3()
    assignment1.print_summary()

