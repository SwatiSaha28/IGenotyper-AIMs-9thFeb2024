#!/bin/env python
import os
from helper import create_folders

class FileManager():
    def __init__(self,outdir,bam=None,tmp = "tmp"):
        self.outdir = outdir
        self.input_bam = bam
        self.tmp = tmp

        if tmp == "tmp":
            self.tmp = "%s/%s" % (self.outdir,tmp)

        self.folder_structure()
        self.file_structure()

    def folder_structure(self):
        self.preprocess = "%s/preprocessed" % self.outdir
        self.variants = "%s/variants" % self.outdir
        self.alignments = "%s/alignments" % self.outdir
        self.alleles = "%s/alleles" % self.outdir
        self.log = "%s/logs" % self.outdir
        self.package_directory = os.path.dirname(os.path.abspath(__file__))

        folders = [
            self.outdir,
            self.preprocess,
            self.alignments,
            self.variants,
            self.alleles,
            self.tmp,
            self.log
        ]

        create_folders(folders)

    def file_structure(self):
        self.ccs_bam = "%s/ccs.bam" % self.preprocess
        self.ccs_pbi = "%s/ccs.bam.pbi" % self.preprocess
        self.ccs_fastq = "%s/ccs.fastq" % self.tmp
        self.ccs_fastq_unedited = "%s/ccs.fastq" % self.tmp

        self.ref = "%s/data/reference.fasta" % self.package_directory
        self.target_regions = "%s/data/target_regions.bed" % self.package_directory

        self.subreads_to_ref = "%s/subreads_to_ref.sorted.bam" % self.preprocess
        self.subreads_to_ref_phased = "%s/subreads_to_ref_phased.sorted.bam" % self.alignments
        self.ccs_to_ref = "%s/ccs_to_ref.sorted.bam" % self.preprocess
        self.ccs_to_ref_phased = "%s/ccs_to_ref_phased.sorted.bam" % self.alignments

        self.snp_candidates = "%s/snvs_candidates.vcf" % self.tmp
        self.snvs_vcf = "%s/snvs_from_ccs.vcf" % self.variants
        self.phased_snvs_vcf = "%s/snvs_phased_from_ccs.vcf" % self.variants

        self.alleles_matches_in_ccs = "%s/alleles_matches_in_ccs.txt" % self.alleles

        self.phased_blocks = "%s/phased_blocks.txt" % self.variants
        self.input_args = "%s/args.json" % self.log
        self.assembly_script = "%s/data/assembly.sh" % self.package_directory
        self.scripts = "%s/scripts" % self.package_directory