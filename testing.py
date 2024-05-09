for item in ['/usr/local/bin/dolby_vision_professional_tools/cm_analyze', '-m' ,'21' ,'-r', 'FRAMERATE', '-f', 'FRAMERATESTART-ENDFRAME', '--source-format', "u10 p422 lsb32rev",\
                             "le", "422", "ycbcr_bt2020", "video", "pq",\
                             "bt2020", '--aspect-ratios', \
                             'ASPECTRATIO', '--bda', 'INPUT', 'XML_LOC'+".xml"]:
    print(item, end=" ")
