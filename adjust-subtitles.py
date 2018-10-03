from __future__ import print_function
import sys
import os
import re
import argparse

'''
Format of subtitles (you can check it in regex):
 1 00:00:03,986  -->  00:00:31,966 text text
 2 00:00:15,644  -->  00:00:31,966 text text text
'''

def main():
   parser = argparse.ArgumentParser(
      description="Adjusts the timestamps of the subtitles using the "
                  "provided input parameters (in milliseconds, i.e. 1 hr = 3600000 ms)")
   parser.add_argument("-b1", "--begin-old", required=True, help="Begin of the old subtitles")
   parser.add_argument("-e1", "--end-old", required=True, help="End of the old subtitles") 
   parser.add_argument("-b2", "--begin-new", required=True, help="Begin of the new subtitles")
   parser.add_argument("-e2", "--end-new", required=True, help="End of the new subtitles") 
   parser.add_argument("-i", "--input-file", required=True, help="Input file")
   args = parser.parse_args()

   if not os.path.isfile(args.input_file):
       print("File path {} does not exist. Exiting...".format(args.input_file))
       sys.exit()

   len_old = int(args.end_old) - int(args.begin_old)
   len_new = int(args.end_new) - int(args.begin_new)
   speedup = 1.0 * len_new / len_old

   p = re.compile('^\s+(\d+)\s+(\d+):(\d+):(\d+),(\d+) --> (\d+):(\d+):(\d+),(\d+) (.*)')

   with open(args.input_file) as f:
      for line in f:
         m = p.match(line)

         n_left = int(m.group(1))
         h_left = int(m.group(2))
         m_left = int(m.group(3))
         s_left = int(m.group(4))
         ms_left = int(m.group(5))
         h_right = int(m.group(6))
         m_right = int(m.group(7))
         s_right = int(m.group(8))
         ms_right = int(m.group(9))

         time_left_input = ((h_left*60+m_left)*60+s_left)*1000+ms_left
         time_right_input = ((h_right*60+m_right)*60+s_right)*1000+ms_right

         time_left_output = int((time_left_input - int(args.begin_old)) * speedup + int(args.begin_new))
         time_right_output = int((time_right_input - int(args.begin_old)) * speedup + int(args.begin_new))

         out_s_left, out_ms_left = divmod(time_left_output, 1000)
         out_m_left, out_s_left = divmod(out_s_left, 60)
         out_h_left, out_m_left = divmod(out_m_left, 60)

         out_s_right, out_ms_right = divmod(time_right_output, 1000)
         out_m_right, out_s_right = divmod(out_s_right, 60)
         out_h_right, out_m_right = divmod(out_m_right, 60)

         out_left_stamp = str(out_h_left).zfill(2)+':'+str(out_m_left).zfill(2)+':'+str(out_s_left).zfill(2)+','+str(out_ms_left).zfill(3)
         out_right_stamp = str(out_h_right).zfill(2)+':'+str(out_m_right).zfill(2)+':'+str(out_s_right).zfill(2)+','+str(out_ms_right).zfill(3)

         print(m.group(1)+'  '+out_left_stamp+'  -->  '+out_right_stamp+' '+m.group(10))

if __name__ == '__main__':  
   main()
