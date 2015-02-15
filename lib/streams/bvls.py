from ..utils import bitly, xbmcutil
from . import veetle

sourceSite='http://www.bvls2013.com/'

def addStreams():
    pBar = xbmcutil.createProgressBar('Dutch Sports Streams', 'Laden van streams...')

    xbmcutil.updateProgressBar(pBar, 19, 'BVLS - Stream 1')
    bvls1 = bitly.getLink('bvls1', sourceSite)
    veetle.addChannel('BVLS - Stream 1', bvls1, 'bvls')

    xbmcutil.updateProgressBar(pBar, 38, 'BVLS - Stream 2')
    bvls2 = bitly.getLink('bvls2', sourceSite)
    veetle.addChannel('BVLS - Stream 2', bvls2, 'bvls')

    xbmcutil.updateProgressBar(pBar, 57, 'BVLS - Stream 3')
    bvls3 = bitly.getLink('bvls3', sourceSite)
    veetle.addChannel('BVLS - Stream 3', bvls3, 'bvls')

    xbmcutil.updateProgressBar(pBar, 76, 'BVLS - Stream 4')
    bvls4 = bitly.getLink('bvls4', sourceSite)
    veetle.addChannel('BVLS - Stream 4', bvls4, 'bvls')

    xbmcutil.updateProgressBar(pBar, 95, 'BVLS - Stream 5')
    bvls5 = bitly.getLink('bvls5', sourceSite)
    veetle.addChannel('BVLS - Stream 5', bvls5, 'bvls')

    xbmcutil.updateProgressBar(pBar, 100,'Gereed!')
    xbmcutil.endOfList()
