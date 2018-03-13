#!/usr/bin/python
"""
FLASH   V1.0    martenhoogeveen@naturalis.nl

This is a wrapper for the tool FLASH (https://ccb.jhu.edu/software/FLASH/).
FLASH can merge paired-end sequencing data. The wrapper handles a zip file with one or more pairs.
"""
import sys, os, argparse
import glob
import string
from Bio import SeqIO
from subprocess import call, Popen, PIPE

# Retrieve the commandline arguments
parser = argparse.ArgumentParser(description='')
requiredArguments = parser.add_argument_group('required arguments')

requiredArguments.add_argument('-i', '--input', metavar='input zipfile', dest='inzip', type=str,
                               help='Inputfile in zip format', required=True)
requiredArguments.add_argument('-o', '--output', metavar='output', dest='out', type=str,
                               help='Output in zip format', required=True)
requiredArguments.add_argument('-ol', '--log_output', metavar='log output', dest='out_log', type=str,
                               help='Log file', required=True)
requiredArguments.add_argument('-t', '--input_type', metavar='FASTQ or GZ input', dest='input_type', type=str,
                               help='Sets the input type, gz or FASTQ', required=True)
requiredArguments.add_argument('-f', '--forward', metavar='Add non-megerd forward reads', dest='forward', type=str,
                               help='Adds the forward reads to the merged reads file. Option can be discard, add or seperate', required=True)
requiredArguments.add_argument('-m', '--min-overlap', metavar='minimum overlap', dest='minforward', type=str,
                               help='minimum overlap', required=True)
requiredArguments.add_argument('-x', '--mis-ratio', metavar='mismatch ratio', dest='mismatch', type=str,
                               help='mismatch ratio', required=True)
requiredArguments.add_argument('-M', '--max-overlap', metavar='max overlap', dest='maxoverlap', type=str,
                               help='maxoverlap', required=True)
args = parser.parse_args()

def admin_log(tempdir, out=None, error=None, function=""):
    with open(tempdir + "/adminlog.log", 'a') as adminlogfile:
        seperation = 60 * "="
        if out:
            adminlogfile.write("out "+ function + " \n" + seperation + "\n" + out + "\n\n")
        if error:
            adminlogfile.write("error " + function + "\n" + seperation + "\n" + error + "\n\n")

def make_output_folders(tempdir):
    call(["mkdir", tempdir + "/paired_files"])
    call(["mkdir", tempdir + "/merged_files"])
    call(["mkdir", tempdir + "/output"])

def get_files(tempdir):
    filetype = tempdir+"/paired_files/*.fastq"
    gzfiles = [os.path.basename(x) for x in sorted(glob.glob(filetype))]
    reverse=[]
    pairs={}
    for x in gzfiles:
        if x not in reverse:
            sample = x.partition("R1")[0]
            pairlist=[]
            for y in gzfiles:
                if sample == y[:len(sample)]:
                    pairlist.append(y)
                    if y[:(len(sample)+2)] == sample+"R2":
                        reverse.append(y)
            pairs[sample[:-1]] = pairlist
    return pairs

def gunzip(tempdir):
    filetype = tempdir + "/paired_files/*.gz"
    gzfiles = [os.path.basename(x) for x in sorted(glob.glob(filetype))]
    for x in gzfiles:
        call(["gunzip", tempdir + "/paired_files/" + x])
        gunzip_filename = os.path.splitext(x[:-3])
        call(["mv", tempdir + "/paired_files/" + x[:-3], tempdir + "/paired_files/" +gunzip_filename[0].translate((string.maketrans("-. " , "___")))+gunzip_filename[1]])

def flash(pairs, tempdir):
    for x in pairs:
        basename = pairs[x][0].split("_R1")[0]
        out, error = Popen(["flash", tempdir+"/paired_files/"+pairs[x][0], tempdir+"/paired_files/"+pairs[x][1],"-x", args.mismatch ,"-m", args.minforward, "-M", args.maxoverlap, "-d", tempdir+"/merged_files/" ,"-o", basename], stdout=PIPE, stderr=PIPE).communicate()
        admin_log(tempdir, out=out, error=error, function="flash")
        if args.forward == "add":
            with open(tempdir+"/output/"+basename+"_merged_forward.fastq", 'a') as outfile:
                call(["cat", tempdir+"/merged_files/"+basename+".extendedFrags.fastq", tempdir+"/merged_files/"+basename+".notCombined_1.fastq"],stdout=outfile)
        if args.forward == "seperate":
            call(["mv",  tempdir+"/merged_files/"+basename+".extendedFrags.fastq", tempdir+"/output/"+basename+"_merged.fastq"])
            call(["mv",  tempdir+"/merged_files/"+basename + ".notCombined_1.fastq", tempdir + "/output/" + basename + "_forward.fastq"])
        if args.forward == "discard":
            call(["mv",  tempdir+"/merged_files/"+basename + ".extendedFrags.fastq", tempdir + "/output/" + basename + "_merged.fastq"])

def zip_it_up(tempdir):
    #call(["mv", tempdir + "/adminlog.log", tempdir+"/output/adminlog.log"])
    call(["zip","-r","-j", tempdir+".zip", tempdir+"/output/"],stdout=open(os.devnull, 'wb'))
    call(["mv", tempdir + ".zip", args.out])
    call(["cp", tempdir+"/adminlog.log", args.out_log])


def main():
    tempdir = Popen(["mktemp", "-d", "/media/GalaxyData/files/XXXXXX"], stdout=PIPE, stderr=PIPE).communicate()[0].strip()
    make_output_folders(tempdir)
    zip_out, zip_error = Popen(["unzip", args.inzip, "-d", tempdir.strip() + "/paired_files"], stdout=PIPE,stderr=PIPE).communicate()
    admin_log(tempdir, zip_out, zip_error)
    if args.input_type == "gz":
        gunzip(tempdir)
    pairs = get_files(tempdir)
    flash(pairs, tempdir)
    zip_it_up(tempdir)
    call(["rm", "-rf", tempdir])




if __name__ == '__main__':
    main()



