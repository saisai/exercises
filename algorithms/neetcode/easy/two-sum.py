import logging

#logger = logging.getLogger(__name__)
logger = logging.getLogger(__name__)

'''
logging.basicConfig(
        level=logging.DEBUG,
        format='[%(levelname)s] (%(threadName)-10s) %(message)s',
        )
'''

logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter =  logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

ch.setFormatter(formatter)

logger.addHandler(ch)

class S:

    def __call__(self,  nums, target):

        prevMap = {} # val: index

        for i, n in enumerate(nums):
            diff = target - n
            logger.debug("prevMap %s " % (prevMap))
            if diff in prevMap:
                logger.debug("diff %s" % (diff))
                return [prevMap[diff], i]
            prevMap[n] = i
        return


nums = [2,7,11,15]
target = 9
print(S()(nums, target))

if __name__ == '__main__':
    nums = [3, 2, 4]
    target = 6
    print(S()(nums, target))
