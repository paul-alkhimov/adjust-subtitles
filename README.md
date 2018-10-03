# adjust-subtitles
Adjusts wrong timestamps of subtitles in case the framerate was changed and possibly video was cut in the beginning

To run the program find the subtitle in the very beginning of the video and identify its correct time (in milliseconds), do the same with on subtitle in the very end of the video.

Then run the program as follows:  
`python adjust-subtitles.py -b1 44177 -e1 3695258 -b2 47000 -e2 3855000 -i input-file.srt > output-file.srt`

Please note, that "srt" extension is misleading here. The format of the subtitles is described in the script itself (one line per timestamp).

Here is the help message:  
`python adjust-subtitles.py --help`  
`usage: adjust-subtitles.py [-h] -b1 BEGIN_OLD -e1 END_OLD -b2 BEGIN_NEW -e2 END_NEW -i INPUT_FILE`  
  
`Adjusts the timestamps of the subtitles using the provided input parameters`  
`(in milliseconds, i.e. 1 hr = 3600000 ms)`  
  
`optional arguments:`  
`  -h, --help            show this help message and exit`  
`  -b1 BEGIN_OLD, --begin-old BEGIN_OLD`  
`                        Begin of the old subtitles`  
`  -e1 END_OLD, --end-old END_OLD`  
`                        End of the old subtitles`  
`  -b2 BEGIN_NEW, --begin-new BEGIN_NEW`  
`                        Begin of the new subtitles`  
`  -e2 END_NEW, --end-new END_NEW`  
`                        End of the new subtitles`  
`  -i INPUT_FILE, --input-file INPUT_FILE`  
`                        Input file`
