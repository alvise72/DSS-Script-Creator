#!/usr/bin/python

import argparse
import sys
import os

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Tool to produce DSS script file")
  parser.add_argument('-b',
                    '--bias',
                    type=str,
                    required=False,
                    dest='bias',
                    default=None,
                    help="Specify the folder containing the bias/offset frames")
  parser.add_argument('-d',
                    '--dark',
                    type=str,
                    required=False,
                    dest='dark',
                    help="Specify the folder containing the dark frames")
  parser.add_argument('-l',
                      '--light',
                      type=str,
                      required=False,
                      dest='light',
                      help="Specify the folder containing the light frames")
  parser.add_argument('-o',
                      '--output',
                      type=str,
                      dest='output',
                      required=False,
                      default="dss-script.txt",
                      help="Specify the filename of the siril script to create")
  parser.add_argument('-f',
                      '--flat',
                      type=str,
                      dest='flat',
                      required=False,
                      help="Specify the folder containing the flat/vignetting files")
  parser.add_argument('-R',
                      '--raw',
                      action='store_true',
                      dest='raw',
                      required=False,
                      default=False,
                      help="Specify if source files are RAW")
  parser.add_argument('dsoname',
                      metavar='DeepSpace Object Name',
                      type=str,
                      help="Specify the mandatory name of the deep sky object name")              
  parser.add_argument('-T',
                      '--templatefile',
                      metavar='Template file for settings',
                      type=str,
                      required=False,
                      default="%s/dss-template.txt" %os.environ['HOME'],
                      help="Specify the file containing the basic settings to be modified and merged with file list")
                      
  options = parser.parse_args()

  output = "DSS file list\nCHECKED	TYPE	FILE"

  #------------------------------------------------------------------------------------------------------------------------------

  lightfiles = ()
  biasfiles = ()
  flatfiles = ()
  darkfiles = ()
  lightfiles = os.listdir(options.light)
  
  if len(lightfiles) == 0:
    print("No lights to process. Stop.")
    sys.exit(1)
  
  for file in lightfiles:
    if file.startswith('.'):
        continue
    if ".cal.Info.txt" in file or ".Info.txt" in file or ".cal.tif" in file or ".stackinfo.txt" in file or "MasterOffset" in file or "MasterDark" in file:
      continue
    output += "\n1\tlight\t%s\%s" %(options.light.rstrip('/'),file)
    
  if options.bias is not None:
    biasfiles = os.listdir(options.bias)
    for file in biasfiles:
      if file.startswith('.'):
        continue
      if ".cal.Info.txt" in file or ".Info.txt" in file or ".cal.tif" in file or ".stackinfo.txt" in file or "MasterOffset" in file or "MasterDark" in file:
        continue
      output += "\n1\toffset\t%s\%s" %(options.bias.rstrip('/'),file)
      
  if options.dark is not None:
    darkfiles = os.listdir( options.dark )
    for file in darkfiles:
      if file.startswith('.'):
        continue
      if ".cal.Info.txt" in file or ".Info.txt" in file or ".cal.tif" in file or ".stackinfo.txt" in file or "MasterOffset" in file or "MasterDark" in file:
        continue
      output += "\n1\tdark\t%s\%s" %(options.dark.rstrip('/'),file)
      
  if options.flat is not None:
    flatfiles = os.listdir( options.flat )
    for file in flatfiles:
      if file.startswith('.'):
        continue
      if ".cal.Info.txt" in file or ".Info.txt" in file or ".cal.tif" in file or ".stackinfo.txt" in file or "MasterOffset" in file or "MasterDark" in file:
        continue
      output += "\n1\tflat\t%s\%s" %(options.flat.rstrip('/'),file)

  template = ""

  with open(options.templatefile) as f: template = f.read()

  output = output + "\n" + template

  with open(options.output, 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    print(output)
    f.close()
  sys.stdout = sys.__stdout__
  
  print("Please execute command: [wine /Applications/DeepSkyStacker\ \(64\ bit\)/DeepSkyStackerCL.exe /R /S /O:%s /OF32r %s]" %(options.dsoname, options.output) )
