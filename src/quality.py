def check_quality(quality):
    if quality == 240:
        return '/240p/'

    elif quality == 720:
        return '/HD_720p/'

    else:
        return '/hq/'
