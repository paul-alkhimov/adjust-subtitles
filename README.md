# adjust-subtitles
Adjusts wrong timestamps of subtitles in case the framerate was changed and possibly video was cut in the beginning

To run the program find the subtitle in the very beginning of the video and identify its correct time (in milliseconds), do the same with on subtitle in the very end of the video.

Then run the program as follows:  
`python adjust-subtitles.py -b1 44177 -e1 3695258 -b2 47000 -e2 3855000 -i input-file.srt > output-file.srt`

Please note, that "srt" extension is misleading here. The format of the subtitles is described in the script itself (one line per timestamp).
