import os
from set_image.generateClock import buildClock
from set_image.generateThumb import buildThumbnail
from set_image.cropRoundBg import removeBackGround

def main():
    removeBackGround()
    buildClock()
    buildThumbnail()


if __name__ == '__main__':
    main()